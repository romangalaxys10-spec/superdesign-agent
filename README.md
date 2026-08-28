# 🎨 SuperDesign Agent
### *Autonomous Design & Presentation Engine — Zero Paid Credits Required*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Zero Credits](https://img.shields.io/badge/Credits-100%25%20Free%20%26%20Local-brightgreen.svg)]()
[![Output: Tailwind & HTML](https://img.shields.io/badge/Output-Tailwind%20%2B%20Lucide%20%2B%20Chart.js-blue.svg)]()
[![Keynote 16:9](https://img.shields.io/badge/Slides-16%3A9%20Interactive-purple.svg)]()

> **SuperDesign Agent** is an autonomous AI design engine that creates production-grade landing pages, responsive websites, 16:9 interactive presentation slide decks, and product dashboards **locally and deterministically without relying on paid superdesign.dev credits**.

---

## 🚀 Key Capabilities

* 🌐 **Full-Stack Sites & Landing Pages:** Responsive layouts with floating glass navbars, dynamic hero headers, statistics grids, Bento-grid feature cards, monthly/annual pricing toggles, and accordion FAQs.
* 📊 **16:9 Interactive Slide Decks:** Fullscreen presentation decks with keyboard navigation ($\leftarrow / ightarrow$, Space, Home, End, `F` for fullscreen), progress bars, metric callout slides, quote slides, and presenter mode.
* 💻 **Product Dashboards & Telemetry UI:** Live Chart.js interactive graphs (area throughput, doughnut mix), real-time KPI cards with percentage trend indicators, and event audit tables.
* 🎨 **Theme Matrix Design System:**
  * `modern_saas`: Indigo/violet gradients, dark glassmorphism.
  * `apple_minimal`: Pure `#000000` black, SF Pro typography, refined borders.
  * `cyberpunk_neon`: Electric cyan & hot pink, glowing shadows, monospace typography.
  * `neo_brutalist`: 4px black borders, hard offset shadows, high-contrast pastel palettes.
  * `clean_editorial`: Warm cream tones, serif typography, editorial layouts.
* 🪟 **Infinite Canvas & Parallel Exploration:** Generate 4 visual variants simultaneously for side-by-side aesthetic comparison.
* ⚡ **Zero Dependencies / Zero Setup:** Generates clean, standalone HTML files with Tailwind CSS via CDN, Lucide Icons, and Chart.js that work in any browser, IDE previewer, or webview.

---

## 📦 Quick Start

### 1. Installation

```bash
cd superdesign-agent
pip install -e .
```

### 2. Generate a Website

```bash
superdesign site \
  --title "KryptonFlow" \
  --tagline "Real-Time Solana Stream Engine" \
  --prompt "High-frequency on-chain transaction parser and automated pool sniffer" \
  --theme modern_saas
```

### 3. Generate a 16:9 Pitch Deck

```bash
superdesign slide \
  --title "AI Agent Architect Keynote" \
  --presenter "Chief AI Architect" \
  --slides-count 5 \
  --theme apple_minimal
```

### 4. Generate a Product Dashboard

```bash
superdesign product \
  --name "SolanaSentinel Ops" \
  --theme modern_saas
```

### 5. Launch Live Preview Canvas

```bash
superdesign serve --port 8080
```

---

## 🧪 Running Tests

```bash
python3 -m unittest discover tests
```

---

## 📄 License

MIT License. Free for indie hackers, commercial projects, and autonomous agent systems.
