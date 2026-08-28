"""
Master Anti-Slop Design Engine.
Guarantees zero-slop synthesis with built-in AntiSlopAuditor linting and 4-archetype parallel exploration.
"""

from typing import Dict, List, Any, Optional
import os
from .taste_matrix import TasteMatrix, TasteArchetype
from .site_generator import SiteGenerator
from .slide_generator import SlideGenerator
from .product_ui_generator import ProductUIGenerator
from .anti_slop_linter import AntiSlopAuditor, AuditReport


class SuperDesignEngine:
    """Anti-AI-Slop Autonomous Design Engine."""

    def __init__(self, output_dir: str = "./output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def create_site(
        self,
        title: str,
        tagline: str,
        description: str,
        features: List[Dict[str, str]],
        theme_style: str = "swiss_international",
        filename: Optional[str] = None,
    ) -> str:
        html = SiteGenerator.generate_site(
            title=title,
            tagline=tagline,
            description=description,
            features=features,
            theme_style=theme_style,
        )
        purified_html = AntiSlopAuditor.auto_purify_html(html)
        fname = filename or f"site_{theme_style}.html"
        out_path = os.path.join(self.output_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(purified_html)
        return out_path

    @staticmethod
    def create_slide_deck(
        deck_title: str,
        presenter: str,
        slides: List[Dict[str, Any]],
        theme_style: str = "swiss_international",
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
        purified_html = AntiSlopAuditor.auto_purify_html(html)
        fname = filename or f"deck_{theme_style}.html"
        out_path = os.path.join(output_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(purified_html)
        return out_path

    def create_product_dashboard(
        self,
        app_name: str,
        kpis: Optional[List[Dict[str, str]]] = None,
        theme_style: str = "industrial_hud",
        filename: Optional[str] = None,
    ) -> str:
        html = ProductUIGenerator.generate_dashboard(
            app_name=app_name,
            kpis=kpis or [],
            theme_style=theme_style,
        )
        purified_html = AntiSlopAuditor.auto_purify_html(html)
        fname = filename or f"dashboard_{theme_style}.html"
        out_path = os.path.join(self.output_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(purified_html)
        return out_path

    def generate_infinite_canvas_variants(
        self,
        prompt: str,
        product_name: str = "NexusEngine",
    ) -> str:
        """Generates 4 radical anti-slop archetypes on a comparison canvas."""
        canvas_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anti-Slop Canvas — 4 Radical Aesthetic Dimensions</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Chivo+Mono:wght@700&family=Playfair+Display:ital,wght@1,700&family=Space+Grotesk:wght@700&family=Syne:wght@800&family=Clash+Display:wght@700&display=swap" rel="stylesheet">
</head>
<body class="bg-[#08090a] text-white min-h-screen p-8 font-mono">
    <header class="max-w-7xl mx-auto mb-10 pb-6 border-b border-neutral-800 flex items-center justify-between">
        <div>
            <div class="text-xs uppercase tracking-widest text-[#FF3B00] font-bold mb-1">[ANTI-SLOP CANVAS // 2026]</div>
            <h1 class="text-3xl font-black tracking-tight text-white uppercase">Aesthetic Archetypes: "{prompt}"</h1>
        </div>
    </header>

    <main class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Archetype 1: Swiss International -->
        <div class="bg-[#0c0d0e] border-2 border-white/20 p-8 space-y-6">
            <div class="flex items-center justify-between border-b border-white/10 pb-3">
                <span class="text-xs font-bold text-[#FF3B00] uppercase tracking-widest">01 // SWISS INTERNATIONAL</span>
                <span class="text-[10px] text-neutral-500">SYNE + SPACE GROTESK</span>
            </div>
            <div class="text-4xl font-black font-['Syne',sans-serif] uppercase tracking-tight">{product_name}</div>
            <p class="text-sm font-['Space_Grotesk',sans-serif] text-neutral-400">{prompt}</p>
            <button class="bg-[#FF3B00] text-white font-bold px-6 py-3 uppercase text-xs tracking-widest">Initiate Protocol</button>
        </div>

        <!-- Archetype 2: Industrial Teenage HUD -->
        <div class="bg-[#121316] border border-[#2b2f3a] p-8 space-y-6 shadow-inner">
            <div class="flex items-center justify-between border-b border-[#2b2f3a] pb-3">
                <span class="text-xs font-bold text-[#FFB000] uppercase tracking-widest">02 // INDUSTRIAL TEENAGE HUD</span>
                <span class="text-[10px] text-neutral-500">CHIVO MONO</span>
            </div>
            <div class="text-3xl font-black font-['Chivo_Mono',monospace] text-[#e1e4ea] uppercase">{product_name}</div>
            <p class="text-xs font-mono text-[#7e8494]">{prompt}</p>
            <button class="bg-[#FFB000] text-black font-mono font-bold px-6 py-3 uppercase text-xs rounded">EXECUTE CLOCK</button>
        </div>

        <!-- Archetype 3: Haute Editorial -->
        <div class="bg-[#F7F5F0] border border-black/10 p-8 space-y-6 text-[#141311]">
            <div class="flex items-center justify-between border-b border-black/10 pb-3">
                <span class="text-xs font-serif italic tracking-widest text-[#141311]">03 // HAUTE EDITORIAL</span>
                <span class="text-[10px] text-neutral-500">PLAYFAIR + INSTRUMENT</span>
            </div>
            <div class="text-4xl font-serif italic tracking-tight">{product_name}</div>
            <p class="text-sm font-serif text-[#696560] leading-relaxed">{prompt}</p>
            <button class="bg-[#141311] text-[#F7F5F0] font-serif px-6 py-3 text-xs tracking-wide">Enter Archive</button>
        </div>

        <!-- Archetype 4: Neo-Cybernetic -->
        <div class="bg-[#050608] border-l-4 border-[#CCFF00] p-8 space-y-6">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <span class="text-xs font-bold text-[#CCFF00] uppercase tracking-widest">04 // NEO-CYBERNETIC</span>
                <span class="text-[10px] text-neutral-500">CLASH DISPLAY</span>
            </div>
            <div class="text-3xl font-black text-white font-['Clash_Display',sans-serif] uppercase">{product_name}</div>
            <p class="text-xs font-mono text-neutral-400">{prompt}</p>
            <button class="bg-[#CCFF00] text-black font-mono font-black px-6 py-3 uppercase text-xs">OVERRIDE</button>
        </div>
    </main>
</body>
</html>"""
        canvas_path = os.path.join(self.output_dir, "anti_slop_canvas.html")
        with open(canvas_path, "w", encoding="utf-8") as f:
            f.write(canvas_html)
        return canvas_path
