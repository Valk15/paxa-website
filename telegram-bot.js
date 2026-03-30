require('dotenv').config({ path: require('path').join(__dirname, '.env') });
const https = require('https');
const { execSync, spawn } = require('child_process');
const path = require('path');

// ─── Daemonise ────────────────────────────────────────────────────────────────
// When run directly, spawn a detached background child and exit.
// The child sets PAXA_BOT_CHILD=1 so it skips this block and runs the bot.
if (!process.env.PAXA_BOT_CHILD) {
  const child = spawn(process.execPath, [__filename], {
    detached: true,
    stdio: 'ignore',
    env: { ...process.env, PAXA_BOT_CHILD: '1' },
    cwd: __dirname
  });
  child.unref();
  console.log(`PAXA Telegram bot started in background (pid ${child.pid})`);
  process.exit(0);
}

// ─── Config ───────────────────────────────────────────────────────────────────
const BOT_TOKEN = process.env.BOT_TOKEN;
const ALLOWED_CHAT_IDS = process.env.ALLOWED_CHAT_IDS.split(',');
const CLAUDE = process.platform === 'win32' ? 'claude.cmd' : 'claude';
let lastUpdateId = 0;

// ─── Telegram ─────────────────────────────────────────────────────────────────
function sendMessage(chatId, text) {
  const truncated = text.length > 4000 ? text.slice(0, 4000) + '\n\n_[truncated]_' : text;
  const body = JSON.stringify({ chat_id: chatId, text: truncated, parse_mode: 'Markdown' });
  const options = {
    hostname: 'api.telegram.org',
    path: `/bot${BOT_TOKEN}/sendMessage`,
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
  };
  const req = https.request(options);
  req.on('error', (e) => console.error('sendMessage error:', e.message));
  req.write(body);
  req.end();
}

// ─── Claude ───────────────────────────────────────────────────────────────────
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

// ─── Poll loop ────────────────────────────────────────────────────────────────
function poll() {
  const options = {
    hostname: 'api.telegram.org',
    path: `/bot${BOT_TOKEN}/getUpdates?offset=${lastUpdateId + 1}&timeout=30`,
    method: 'GET'
  };

  const req = https.request(options, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
      try {
        const json = JSON.parse(data);
        if (json.ok && json.result.length > 0) {
          for (const update of json.result) {
            lastUpdateId = update.update_id;
            const msg = update.message;
            if (!msg || !msg.text) continue;

            const chatId = String(msg.chat.id);
            if (!ALLOWED_CHAT_IDS.includes(chatId)) {
              sendMessage(chatId, 'Unauthorised.');
              continue;
            }

            sendMessage(chatId, `Running: _${msg.text}_`);
            const response = runClaude(msg.text);
            sendMessage(chatId, response);
          }
        }
      } catch (e) {
        console.error('Poll parse error:', e.message);
      }
      poll();
    });
  });

  req.on('error', (e) => {
    console.error('Poll error:', e.message);
    setTimeout(poll, 5000);
  });

  req.end();
}

console.log('PAXA Telegram bot running...');
poll();
