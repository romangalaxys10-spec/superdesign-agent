"""
Anti-Slop Site & Landing Page Generator.
Builds bespoke, asymmetric, typographically bold web layouts free of generic AI tropes.
"""

from typing import Dict, List, Optional, Any
from .taste_matrix import TasteMatrix, TasteArchetype, AntiSlopTheme


class SiteGenerator:
    """Generates human-taste architectural web experiences."""

    @staticmethod
    def generate_site(
        title: str,
        tagline: str,
        description: str,
        features: List[Dict[str, str]],
        theme_style: str = "swiss_international",
        cta_text: str = "Initiate Protocol",
        metrics: Optional[List[Dict[str, str]]] = None,
        pricing_plans: Optional[List[Dict[str, Any]]] = None,
        manifesto: Optional[str] = None,
    ) -> str:
        theme = TasteMatrix.get_theme(theme_style)
        
        default_metrics = metrics or [
            {"value": "0.04ms", "label": "Mean Deterministic Latency"},
            {"value": "100%", "label": "Self-Contained Local Execution"},
            {"value": "0.00$", "label": "Third-Party API Credit Cost"},
            {"value": "4.98★", "label": "Architectural Taste Index"},
        ]

        # Manifesto copy (Anti-slop narrative)
        manifesto_text = manifesto or (
            "We reject the sea of identical purple-gradient SaaS clones. "
            "Real engineering demands uncompromising typography, tactile depth, "
            "asymmetric balance, and structural honesty."
        )

        # Features HTML (Asymmetric Swiss or Industrial format)
        features_html = ""
        for i, feat in enumerate(features):
            f_title = feat.get("title", f"Protocol {i+1}")
            f_desc = feat.get("desc", "High-density deterministic component design with zero AI bloat.")
            f_tag = feat.get("tag", f"MOD_{i+1:02d}")
            
            features_html += f"""
            <div class="{theme.card_style} relative group">
                <div class="flex items-center justify-between mb-6 pb-2 border-b {theme.border_rule}">
                    <span class="{theme.font_family_body} text-xs uppercase tracking-widest text-neutral-500">{f_tag}</span>
                    <span class="text-xs font-mono {theme.text_secondary}">[ACTIVE]</span>
                </div>
                <h3 class="text-2xl font-bold {theme.font_family_display} {theme.text_primary} mb-3 tracking-tight">{f_title}</h3>
                <p class="{theme.font_family_body} {theme.text_secondary} text-sm leading-relaxed">{f_desc}</p>
            </div>"""

        # Metrics HTML (High-contrast numbers)
        metrics_html = ""
        for m in default_metrics:
            metrics_html += f"""
            <div class="p-8 border-b md:border-b-0 md:border-r last:border-r-0 {theme.border_rule}">
                <div class="text-5xl lg:text-6xl font-black {theme.font_family_display} {theme.text_primary} mb-2 tracking-tighter">{m['value']}</div>
                <div class="{theme.font_family_body} {theme.text_secondary} text-xs uppercase tracking-widest">{m['label']}</div>
            </div>"""

        # Noise & Texture Overlay CSS
        noise_svg = """
    <svg class="pointer-events-none fixed inset-0 z-50 h-full w-full opacity-[0.03]" xmlns="http://www.w3.org/2000/svg">
        <filter id="noiseFilter"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/></filter>
        <rect width="100%" height="100%" filter="url(#noiseFilter)"/>
    </svg>"""

        return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — {tagline}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="{theme.font_import_url}" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .grid-matrix {{
            background-size: 32px 32px;
            background-image: linear-gradient(to right, rgba(255, 255, 255, 0.04) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
        }}
        .dot-matrix {{
            background-size: 24px 24px;
            background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
        }}
    </style>
</head>
<body class="{theme.bg_style} {theme.font_family_body} min-h-screen selection:bg-[{theme.accent_color}] selection:text-white relative">
    {noise_svg}

    <!-- Top Architecture Bar -->
    <header class="border-b {theme.border_rule} px-8 py-5 flex items-center justify-between sticky top-0 z-40 bg-inherit/90 backdrop-blur-md">
        <div class="flex items-center gap-4">
            <span class="text-xl font-black tracking-tighter {theme.font_family_display} {theme.text_primary} uppercase">{title}</span>
            <span class="{theme.badge_style}">{tagline}</span>
        </div>
        <div class="hidden md:flex items-center gap-8 text-xs uppercase tracking-widest font-bold {theme.text_secondary}">
            <a href="#manifesto" class="hover:{theme.text_primary} transition-colors">Manifesto</a>
            <a href="#architecture" class="hover:{theme.text_primary} transition-colors">Architecture</a>
            <a href="#specs" class="hover:{theme.text_primary} transition-colors">Telemetry</a>
        </div>
        <div>
            <a href="#specs" class="{theme.button_primary}">{cta_text}</a>
        </div>
    </header>

    <!-- Hero: Asymmetric Editorial Scale -->
    <section class="pt-24 pb-20 px-8 max-w-7xl mx-auto border-b {theme.border_rule}">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-end">
            <div class="lg:col-span-8 space-y-6">
                <div class="{theme.font_family_body} text-xs uppercase tracking-[0.25em] text-neutral-500 flex items-center gap-2">
                    <span class="inline-block w-2 h-2 bg-[{theme.accent_color}]"></span>
                    <span>ANTI-SLOP ARCHITECTURAL SPECIFICATION 2026</span>
                </div>
                <h1 class="text-5xl sm:text-7xl lg:text-8xl font-black {theme.font_family_display} {theme.text_primary} tracking-tight leading-[0.95] uppercase">
                    Form Follows <br>
                    <span class="text-[{theme.accent_color}]">Precision.</span>
                </h1>
                <p class="text-lg md:text-xl {theme.text_secondary} max-w-2xl leading-relaxed pt-4">
                    {description}
                </p>
            </div>
            <div class="lg:col-span-4 border-t-2 border-[{theme.accent_color}] pt-6 space-y-4">
                <div class="text-xs font-mono uppercase text-neutral-500">SYSTEM MANIFESTO // 01</div>
                <p class="text-sm italic {theme.text_primary} font-serif leading-relaxed">
                    "{manifesto_text}"
                </p>
                <div class="pt-4 flex gap-4">
                    <a href="#architecture" class="{theme.button_primary} w-full text-center">Deploy Engine</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Metrics Strip -->
    <section class="border-b {theme.border_rule} max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-4">
            {metrics_html}
        </div>
    </section>

    <!-- Architectural Modules -->
    <section id="architecture" class="py-24 px-8 max-w-7xl mx-auto border-b {theme.border_rule}">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b {theme.border_rule} gap-6">
            <div>
                <span class="text-xs font-mono text-neutral-500 uppercase tracking-widest">// ARCHITECTURAL TOPOLOGY</span>
                <h2 class="text-4xl md:text-5xl font-black {theme.font_family_display} {theme.text_primary} tracking-tight uppercase mt-2">Engineered Modules</h2>
            </div>
            <p class="{theme.text_secondary} max-w-md text-xs uppercase tracking-wider leading-relaxed">
                Zero cookie-cutter components. Each module is crafted with strict typography, discrete bounding boxes, and verified telemetry.
            </p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            {features_html}
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 px-8 max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-6 text-xs uppercase tracking-widest {theme.text_secondary}">
        <div>
            <span class="font-bold {theme.text_primary}">{title}</span> — Built with Anti-Slop Standards.
        </div>
        <div class="flex gap-8 font-mono">
            <span>[NO PURPLE BLOBS]</span>
            <span>[NO GENERIC INTER]</span>
            <span>[NO PAYWALLS]</span>
        </div>
    </footer>

    <script>lucide.createIcons();</script>
</body>
</html>"""
