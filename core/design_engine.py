"""
Master SuperDesign Engine.
Orchestrates parallel multi-variant exploration, sites, slides, and component generation with zero external credits.
"""

from typing import Dict, List, Any, Optional
import os
from .theme_matrix import ThemeMatrix, ThemeStyle
from .site_generator import SiteGenerator
from .slide_generator import SlideGenerator
from .product_ui_generator import ProductUIGenerator


class SuperDesignEngine:
    """Universal Design Synthesis & Variant Generator Engine."""

    def __init__(self, output_dir: str = "./output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def create_site(
        self,
        title: str,
        tagline: str,
        description: str,
        features: List[Dict[str, str]],
        theme_style: str = "modern_saas",
        filename: Optional[str] = None,
    ) -> str:
        html = SiteGenerator.generate_site(
            title=title,
            tagline=tagline,
            description=description,
            features=features,
            theme_style=theme_style,
        )
        fname = filename or f"site_{theme_style}.html"
        out_path = os.path.join(self.output_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        return out_path

    def create_slide_deck(
        deck_title: str,
        presenter: str,
        slides: List[Dict[str, Any]],
        theme_style: str = "apple_minimal",
        output_dir: str = "./output",
        filename: Optional[str] = None,
    ) -> str:
        os.makedirs(output_dir, exist_ok=True)
        html = SlideGenerator.generate_deck(
            deck_title=deck_title,
            presenter=presenter,
            slides=slides,
            theme_style=theme_style,
        )
        fname = filename or f"deck_{theme_style}.html"
        out_path = os.path.join(output_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        return out_path

    def create_product_dashboard(
        self,
        app_name: str,
        kpis: Optional[List[Dict[str, str]]] = None,
        theme_style: str = "modern_saas",
        filename: Optional[str] = None,
    ) -> str:
        html = ProductUIGenerator.generate_dashboard(
            app_name=app_name,
            kpis=kpis or [],
            theme_style=theme_style,
        )
        fname = filename or f"dashboard_{theme_style}.html"
        out_path = os.path.join(self.output_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        return out_path

    def generate_infinite_canvas_variants(
        self,
        prompt: str,
        product_name: str = "SuperAgent",
    ) -> str:
        """
        Generates 4 distinct style variations (Modern SaaS, Apple Minimal, Cyberpunk, Neo-Brutalist)
        and packages them into a multi-viewport comparison canvas.
        """
        features = [
            {"title": "Instant Autonomous Execution", "desc": "Decompose high-level goals into verified actions.", "icon": "zap"},
            {"title": "Zero-Credit Local Generation", "desc": "100% free, deterministic design tokens without third-party paywalls.", "icon": "shield-check"},
            {"title": "Cross-Platform Export", "desc": "Export directly to clean React, Vue, HTML, and Tailwind code.", "icon": "code-2"},
        ]

        canvas_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SuperDesign Canvas — 4-Variant Parallel Exploration</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-[#0b0f19] text-slate-100 min-h-screen p-8">
    <header class="max-w-7xl mx-auto mb-8 flex items-center justify-between border-b border-slate-800 pb-6">
        <div>
            <div class="flex items-center gap-3 mb-2">
                <span class="px-3 py-1 bg-indigo-500/20 text-indigo-400 border border-indigo-500/30 rounded-full text-xs font-mono uppercase">SuperDesign Canvas</span>
                <span class="text-xs text-slate-400">Zero-Credit Architecture</span>
            </div>
            <h1 class="text-3xl font-extrabold text-white">Parallel Variant Exploration: "{prompt}"</h1>
        </div>
        <div class="flex gap-3">
            <button onclick="window.location.reload()" class="bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2 rounded-xl text-sm font-semibold flex items-center gap-2 cursor-pointer">
                <i data-lucide="refresh-cw" class="w-4 h-4"></i> Regenerate
            </button>
        </div>
    </header>

    <main class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Variant 1: Modern SaaS -->
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4 shadow-xl">
            <div class="flex items-center justify-between">
                <span class="font-bold text-indigo-400 flex items-center gap-2">
                    <i data-lucide="sparkles" class="w-4 h-4"></i> Variant A: Modern SaaS Dark
                </span>
                <span class="text-xs text-slate-500">Tailwind + Glassmorphism</span>
            </div>
            <div class="bg-[#0a0d14] p-6 rounded-xl border border-slate-800 space-y-4">
                <div class="text-xl font-bold text-white">{product_name}</div>
                <p class="text-sm text-slate-400">{prompt}</p>
                <button class="bg-indigo-600 text-white px-4 py-2 rounded-lg text-xs font-semibold shadow-lg shadow-indigo-500/30">Get Started Free</button>
            </div>
        </div>

        <!-- Variant 2: Apple Minimal -->
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4 shadow-xl">
            <div class="flex items-center justify-between">
                <span class="font-bold text-white flex items-center gap-2">
                    <i data-lucide="apple" class="w-4 h-4"></i> Variant B: Apple Minimalist
                </span>
                <span class="text-xs text-slate-500">Pure Black + SF Typography</span>
            </div>
            <div class="bg-black p-6 rounded-xl border border-[#2d2d2f] space-y-4">
                <div class="text-xl font-bold text-[#f5f5f7] tracking-tight">{product_name}</div>
                <p class="text-sm text-[#86868b]">{prompt}</p>
                <button class="bg-[#0071e3] text-white px-4 py-2 rounded-full text-xs font-medium">Explore Now</button>
            </div>
        </div>

        <!-- Variant 3: Cyberpunk Neon -->
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4 shadow-xl">
            <div class="flex items-center justify-between">
                <span class="font-bold text-cyan-400 flex items-center gap-2">
                    <i data-lucide="terminal" class="w-4 h-4"></i> Variant C: Cyberpunk Neon
                </span>
                <span class="text-xs text-slate-500">Monospace + Neon Glow</span>
            </div>
            <div class="bg-[#050508] p-6 rounded-xl border border-cyan-500/50 space-y-4 shadow-[0_0_15px_rgba(6,182,212,0.2)]">
                <div class="text-xl font-mono font-bold text-cyan-400 uppercase">{product_name}</div>
                <p class="text-sm font-mono text-cyan-200/70">{prompt}</p>
                <button class="bg-cyan-500 text-black px-4 py-2 text-xs font-mono font-bold uppercase tracking-widest">Execute</button>
            </div>
        </div>

        <!-- Variant 4: Neo Brutalist -->
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4 shadow-xl">
            <div class="flex items-center justify-between">
                <span class="font-bold text-yellow-400 flex items-center gap-2">
                    <i data-lucide="box" class="w-4 h-4"></i> Variant D: Neo-Brutalist
                </span>
                <span class="text-xs text-slate-500">Hard Shadows + Bold Borders</span>
            </div>
            <div class="bg-[#fdf6e2] p-6 rounded-xl border-4 border-black space-y-4 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)]">
                <div class="text-xl font-black text-black uppercase">{product_name}</div>
                <p class="text-sm font-bold text-neutral-800">{prompt}</p>
                <button class="bg-[#FFE600] text-black border-2 border-black px-4 py-2 text-xs font-black uppercase shadow-[3px_3px_0px_0px_rgba(0,0,0,1)]">Launch Now</button>
            </div>
        </div>
    </main>

    <script>lucide.createIcons();</script>
</body>
</html>
"""
        canvas_path = os.path.join(self.output_dir, "canvas_variants.html")
        with open(canvas_path, "w", encoding="utf-8") as f:
            f.write(canvas_html)
        return canvas_path
