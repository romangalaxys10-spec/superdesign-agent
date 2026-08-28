---
name: superdesign-agent
description: Autonomous design agent to generate responsive websites, landing pages, interactive 16:9 presentation slide decks, and product dashboards with zero paid credits.
version: 1.0.0
author: AI Agent Architect
---

# SuperDesign Agent · Autonomous UI & Presentation Engine

> "Design websites, interactive pitch decks, and product components without paying for superdesign.dev credits."

## 🎯 Activation Triggers
- `design website`
- `build landing page`
- `create slide deck`
- `generate pitch deck`
- `design product dashboard`
- `parallel design exploration`
- `superdesign`

---

## ⚡ Execution Workflow (Protocol)

1. **Identify Output Intent**:
   - **Website / Landing Page**: Hero, Metrics, Bento Grid Features, Pricing Cards, Accordion FAQ, Footer.
   - **16:9 Interactive Slide Deck**: Keynote title, Problem/Solution, Metric callout, 3-Pillar Architecture, Quote.
   - **Product UI / Dashboard**: Real-time KPI widgets, Chart.js graphs, event tables, sidebar navigation.
   - **4-Variant Exploration**: Parallel canvas rendering Modern SaaS, Apple Minimal, Cyberpunk Neon, and Neo-Brutalist styles.

2. **Select Theme Matrix**:
   - `modern_saas`: Slate 900, Indigo/Violet gradients, glassmorphism.
   - `apple_minimal`: Deep black `#000000`, SF typography, subtle `#2d2d2f` borders.
   - `cyberpunk_neon`: Black, Electric Cyan, Hot Pink, Monospace, neon glow.
   - `neo_brutalist`: Bold `#FFE600` / `#FF90E8`, 4px black borders, hard offset drop shadows.
   - `clean_editorial`: Warm cream `#f9f8f6`, serif typography, understated luxury.

3. **Generate Standalone Artifact**:
   - Uses Tailwind CSS CDN, Lucide icons, Chart.js, and pure vanilla JS.
   - 100% self-contained single HTML files that run immediately in any browser or webview without npm build steps.

4. **Verify & Preview**:
   - Open locally or serve via built-in server (`python3 cli/superdesign.py serve`).

---

## 🛡️ Failure Modes & Fallbacks
| Condition | Primary Action | Fallback |
|---|---|---|
| Ambiguous visual style | Generate 4-variant parallel comparison canvas | Prompt user to pick favourite aesthetic |
| Complex data charts requested | Inject Chart.js with responsive dark-theme options | Render fallback SVG data visualization |
| Offline / restricted CDN | Inline fallback CSS grid & standard SVG icons | Generate pure HTML/CSS bundle |
