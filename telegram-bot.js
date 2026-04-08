require('dotenv').config({ path: require('path').join(__dirname, '.env') });
const https = require('https');
const { execSync } = require('child_process');

const BOT_TOKEN = process.env.BOT_TOKEN;
const ALLOWED_CHAT_IDS = process.env.ALLOWED_CHAT_IDS.split(',');
const CLAUDE = process.platform === 'win32' ? 'claude.cmd' : 'claude';

let lastUpdateId = 0;
const pendingTasks = new Map(); // taskId -> { chatId, task }

// ─── Telegram API ─────────────────────────────────────────────────────────────

function apiRequest(method, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const options = {
      hostname: 'api.telegram.org',
      path: `/bot${BOT_TOKEN}/${method}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(data) }
    };
    const req = https.request(options, (res) => {
      let resp = '';
      res.on('data', chunk => resp += chunk);
      res.on('end', () => { try { resolve(JSON.parse(resp)); } catch (e) { resolve({}); } });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

function sendMessage(chatId, text, replyMarkup) {
  const truncated = text.length > 4000 ? text.slice(0, 4000) + '\n\n<i>[truncated]</i>' : text;
  const body = { chat_id: chatId, text: truncated, parse_mode: 'HTML' };
  if (replyMarkup) body.reply_markup = replyMarkup;
  return apiRequest('sendMessage', body).then(res => {
    if (res && !res.ok) console.error('sendMessage error:', JSON.stringify(res));
    return res;
  });
}

function editMessage(chatId, messageId, text) {
  return apiRequest('editMessageText', {
    chat_id: chatId,
    message_id: messageId,
    text,
    parse_mode: 'HTML'
  });
}

function answerCallback(callbackQueryId, text) {
  return apiRequest('answerCallbackQuery', { callback_query_id: callbackQueryId, text });
}

// ─── Approval system ──────────────────────────────────────────────────────────

function approvalKeyboard(taskId) {
  return {
    inline_keyboard: [[
      { text: '✅ Approve', callback_data: `approve:${taskId}` },
      { text: '❌ Cancel', callback_data: `cancel:${taskId}` }
    ]]
  };
}

async function requestApproval(chatId, description, task) {
  const taskId = Date.now().toString();
  pendingTasks.set(taskId, { chatId, task });
  await sendMessage(chatId, `<b>Approval required</b>\n\n${description}\n\nProceed?`, approvalKeyboard(taskId));
}

// ─── Claude runner ────────────────────────────────────────────────────────────

function runClaude(task) {
  try {
    const result = execSync(
      `"${CLAUDE}" --print --dangerously-skip-permissions "${task.replace(/"/g, '\\"')}"`,
      {
        timeout: 120000,
        encoding: 'utf8',
        cwd: __dirname,
        env: { ...process.env, PATH: process.env.PATH }
      }
    );
    return result.trim() || 'Done.';
  } catch (err) {
    return `Error: ${err.message}`;
  }
}

// ─── Commands ─────────────────────────────────────────────────────────────────

const HELP_TEXT = `<b>PAXA Bot — Commands</b>

/publish [slug] — publish content/[slug].md via paxa-content agent
/post — choose a content file to post
/seo [keyword] — SEO research for a keyword
/competitor — run weekly competitor research (local report)
/analytics — run weekly analytics report (local report)
/status — show Gate 2 status
/help — show this message

Any other message is passed directly to Claude Code.
Tasks that involve file changes require your approval first.`;

async function handleCommand(chatId, text) {
  const [cmd, ...args] = text.trim().split(/\s+/);
  const arg = args.join(' ');

  switch (cmd) {

    case '/help':
      await sendMessage(chatId, HELP_TEXT);
      break;

    case '/status':
      await sendMessage(
        chatId,
        '<b>Gate 2 Status</b>\n\nOrganic sales gate: 0/5 sales\nStatus: 🔴 Not passed — paid ads locked until 5 organic sales'
      );
      break;

    case '/post':
      await sendMessage(chatId, 'Which content file do you want to post? Send the slug, e.g. <code>tiktok-boring-goodbyes</code>');
      break;

    case '/publish': {
      if (!arg) {
        await sendMessage(chatId, 'Usage: <code>/publish [slug]</code>\nExample: <code>/publish tiktok-boring-goodbyes</code>');
        break;
      }
      await requestApproval(
        chatId,
        `Publish <code>content/${arg}.md</code> using the paxa-content agent`,
        `Use the paxa-content agent to publish the content file at content/${arg}.md`
      );
      break;
    }

    case '/seo': {
      if (!arg) {
        await sendMessage(chatId, 'Usage: <code>/seo [keyword]</code>\nExample: <code>/seo dog separation anxiety UK</code>');
        break;
      }
      await requestApproval(
        chatId,
        `Run SEO research for keyword: <i>${arg}</i>`,
        `Use the paxa-seo agent to research this keyword and produce a full SEO brief: ${arg}`
      );
      break;
    }

    case '/competitor':
      // Handled locally — no Claude Code invocation
      await sendMessage(
        chatId,
        '<b>Competitor Research</b>\n\nTo run the full weekly competitor report, use natural language:\n\n<i>"Run competitor research and save the report"</i>\n\nOr type a specific question like: <i>"What are PAXA\'s main UK competitors this week?"</i>'
      );
      break;

    case '/analytics':
      // Handled locally — no Claude Code invocation
      await sendMessage(
        chatId,
        '<b>Analytics Report</b>\n\nTo run the weekly analytics report, paste your data and use natural language:\n\n<i>"Here is this week\'s Gumroad data: [paste data]. Produce the weekly report."</i>\n\nOr: <i>"Run the analytics report"</i> if data files are already in the project.'
      );
      break;

    default:
      await sendMessage(chatId, `Unknown command: <code>${cmd}</code>\n\nType /help to see available commands.`);
  }
}

// ─── Natural language ─────────────────────────────────────────────────────────

const WRITE_PATTERN = /\b(edit|update|create|write|delete|remove|save|commit|push|publish|deploy|modify|change|rename|move|generate|add|insert)\b/i;

async function handleNaturalLanguage(chatId, text) {
  if (WRITE_PATTERN.test(text)) {
    await requestApproval(
      chatId,
      `Execute task:\n<i>${text}</i>`,
      text
    );
  } else {
    await sendMessage(chatId, `Running: <i>${text}</i>`);
    const response = runClaude(text);
    await sendMessage(chatId, response);
  }
}

// ─── Callback query handler ───────────────────────────────────────────────────

async function handleCallbackQuery(query) {
  const { id, data, message } = query;
  const chatId = String(message.chat.id);

  if (!ALLOWED_CHAT_IDS.includes(chatId)) {
    await answerCallback(id, 'Unauthorised.');
    return;
  }

  const colonIdx = data.indexOf(':');
  const action = data.slice(0, colonIdx);
  const taskId = data.slice(colonIdx + 1);
  const pending = pendingTasks.get(taskId);

  if (!pending) {
    await answerCallback(id, 'Task expired.');
    await editMessage(chatId, message.message_id, '⚠️ <i>Task expired or already handled.</i>');
    return;
  }

  pendingTasks.delete(taskId);

  if (action === 'cancel') {
    await answerCallback(id, 'Cancelled.');
    await editMessage(chatId, message.message_id, '❌ <i>Task cancelled.</i>');
    return;
  }

  if (action === 'approve') {
    await answerCallback(id, 'Running...');
    await editMessage(chatId, message.message_id, '⏳ <i>Running task...</i>');
    const response = runClaude(pending.task);
    await sendMessage(chatId, response);
  }
}

// ─── Message handler ──────────────────────────────────────────────────────────

async function handleMessage(msg) {
  if (!msg || !msg.text) return;

  const chatId = String(msg.chat.id);
  if (!ALLOWED_CHAT_IDS.includes(chatId)) {
    await sendMessage(chatId, 'Unauthorised.');
    return;
  }

  const text = msg.text.trim();
  if (text.startsWith('/')) {
    await handleCommand(chatId, text);
  } else {
    await handleNaturalLanguage(chatId, text);
  }
}

// ─── Poll loop ────────────────────────────────────────────────────────────────

function poll() {
  const req = https.request({
    hostname: 'api.telegram.org',
    path: `/bot${BOT_TOKEN}/getUpdates?offset=${lastUpdateId + 1}&timeout=30`,
    method: 'GET'
  }, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', async () => {
      try {
        const json = JSON.parse(data);
        if (json.ok && json.result.length > 0) {
          for (const update of json.result) {
            lastUpdateId = update.update_id;
            if (update.callback_query) {
              await handleCallbackQuery(update.callback_query);
            } else if (update.message) {
              await handleMessage(update.message);
            }
          }
        }
      } catch (e) {
        console.error('Poll error:', e.message);
      }
      poll();
    });
  });

  req.on('error', (e) => {
    console.error('Request error:', e.message);
    setTimeout(poll, 5000);
  });

  req.end();
}

console.log('PAXA Telegram bot running...');
poll();
