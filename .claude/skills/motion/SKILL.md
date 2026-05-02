---
name: motion
description: "Motion animation library skill. Use when creating animated HTML pages, React components, or landing pages with scroll effects, hover animations, entrance animations, spring physics, gestures, layout transitions, or scroll-linked effects. Actions: animate, transition, scroll, gesture, spring, keyframes, stagger, fade, slide, scale, drag, layout. Elements: div, button, navbar, hero, card, modal. Frameworks: React (motion/react), Vanilla JS (motion), Vue (motion-v)."
---

# Motion Animation Library

Motion is a high-performance animation library for React, JavaScript, and Vue. It delivers GPU-accelerated animations via a hybrid engine combining JavaScript with native browser APIs.

**npm:** `npm install motion`  
**CDN (vanilla JS/HTML):** `https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js`  
**CDN (React):** Use via npm — not directly CDN-importable for React  
**Docs:** https://motion.dev

---

## When to Use This Skill

- Creating landing pages with entrance animations or scroll-triggered effects
- Building React components with hover/tap gestures
- Adding spring physics or staggered list animations
- Scroll-linked parallax or progress indicators
- Page transitions and layout animations

---

## Core APIs

### React (motion/react)

```jsx
import { motion, AnimatePresence, useScroll, useTransform, useInView } from "motion/react"

// Basic animated element
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5, ease: "easeOut" }}
/>

// Hover + tap gestures
<motion.button
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.97 }}
/>

// Exit animations (requires AnimatePresence wrapper)
<AnimatePresence>
  {isVisible && (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    />
  )}
</AnimatePresence>

// Scroll-linked animation
const { scrollYProgress } = useScroll()
const opacity = useTransform(scrollYProgress, [0, 1], [0, 1])
<motion.div style={{ opacity }} />

// Animate when in view
const ref = useRef(null)
const isInView = useInView(ref, { once: true })
<motion.div ref={ref} animate={isInView ? { opacity: 1 } : { opacity: 0 }} />

// Staggered children
<motion.ul
  variants={{ visible: { transition: { staggerChildren: 0.1 } } }}
  initial="hidden"
  animate="visible"
>
  <motion.li variants={{ hidden: { opacity: 0 }, visible: { opacity: 1 } }} />
</motion.ul>
```

### Vanilla JavaScript (HTML pages)

```html
<script src="https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js"></script>
<script>
const { animate, scroll, inView, stagger } = Motion

// Basic animate
animate("#box", { x: 100, opacity: 1 }, { duration: 0.5 })

// Spring physics
animate("#card", { scale: 1.1 }, { type: "spring", stiffness: 300 })

// Scroll-triggered
inView("#hero", () => {
  animate("#hero", { opacity: 1, y: 0 }, { duration: 0.6 })
})

// Scroll-linked progress
scroll(({ y }) => {
  animate("#progress", { scaleX: y.progress })
})

// Stagger entrance
animate(".card", { opacity: 1, y: 0 }, { delay: stagger(0.1) })
</script>
```

---

## Transition Presets

```js
// Ease curves
{ ease: "easeIn" | "easeOut" | "easeInOut" | "linear" | "circOut" | "backOut" }

// Spring (feels physical)
{ type: "spring", stiffness: 200, damping: 20, mass: 1 }

// Duration-based
{ duration: 0.4, delay: 0.1 }

// Tween with custom curve
{ ease: [0.16, 1, 0.3, 1], duration: 0.6 }
```

---

## Common Patterns for Landing Pages

### Fade-up on scroll (Vanilla)
```js
inView("section", (el) => {
  animate(el, { opacity: [0, 1], y: [30, 0] }, { duration: 0.6, easing: [0.16, 1, 0.3, 1] })
})
```

### Hero entrance stagger (React)
```jsx
const container = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.12 } }
}
const item = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] } }
}
<motion.div variants={container} initial="hidden" animate="visible">
  <motion.h1 variants={item}>Headline</motion.h1>
  <motion.p variants={item}>Subline</motion.p>
  <motion.button variants={item}>CTA</motion.button>
</motion.div>
```

### Scroll progress bar
```jsx
const { scrollYProgress } = useScroll()
<motion.div style={{ scaleX: scrollYProgress, transformOrigin: "left" }} className="progress-bar" />
```

---

## Performance Rules

- Use `transform` properties (x, y, scale, rotate, opacity) — GPU-accelerated
- Avoid animating `width`, `height`, `top`, `left` — triggers layout reflow
- Use `layout` prop for layout transitions instead of animating dimensions
- Set `will-change: transform` on elements that animate frequently
- Prefer `useInView({ once: true })` to avoid repeated animations

---

## PAXA-Specific Usage Notes

When building PAXA landing pages or product pages:
- Use subtle fade-up entrances (20–30px y offset, 0.5–0.7s duration)
- Spring animations for interactive elements (buttons, cards) — feels premium
- Scroll-triggered reveals for testimonials and science-backed sections
- No excessive or distracting animations — calm authority aesthetic
- Stagger delay max 0.15s for lists to feel snappy not sluggish
