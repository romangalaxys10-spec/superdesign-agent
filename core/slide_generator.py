"""
Anti-Slop Keynote Slide Deck Generator.
Produces stark, high-contrast, typographically exquisite 16:9 presentation decks.
"""

from typing import Dict, List, Any
from .taste_matrix import TasteMatrix, TasteArchetype


class SlideGenerator:
    """Builds presentation slide decks with International Typographic Style."""

    @staticmethod
    def generate_deck(
        deck_title: str,
        presenter: str,
        slides: List[Dict[str, Any]],
        theme_style: str = "swiss_international",
    ) -> str:
        theme = TasteMatrix.get_theme(theme_style)
        
        slides_html = ""
        for i, slide in enumerate(slides):
            s_type = slide.get("type", "content")
            s_title = slide.get("title", f"Slide {i+1}")
            s_subtitle = slide.get("subtitle", "")
            s_content = slide.get("content", [])
            s_metric = slide.get("metric", None)
            s_quote = slide.get("quote", None)
            
            inner_html = ""
            if s_type == "title":
                inner_html = f"""
                <div class="text-left max-w-5xl mx-auto space-y-8">
                    <div class="flex items-center gap-3">
                        <span class="{theme.badge_style}">KEYNOTE SPECIFICATION</span>
                        <span class="text-xs font-mono text-neutral-500">// {s_subtitle or 'CONFIDENTIAL'}</span>
                    </div>
                    <h1 class="text-6xl sm:text-8xl font-black {theme.font_family_display} {theme.text_primary} tracking-tight leading-[0.9] uppercase">
                        {s_title}
                    </h1>
                    <div class="pt-8 border-t-2 border-[{theme.accent_color}] flex items-center justify-between">
                        <span class="text-xl {theme.text_secondary} font-mono">{presenter}</span>
                        <span class="text-xs uppercase font-mono tracking-widest text-neutral-500">2026 EDITION</span>
                    </div>
                </div>"""
            elif s_type == "metric" and s_metric:
                val = s_metric.get('value', '10X')
                lbl = s_metric.get('label', 'Engineering velocity multiplier.')
                inner_html = f"""
                <div class="max-w-5xl mx-auto text-left space-y-8">
                    <span class="text-xs font-mono text-neutral-500 uppercase tracking-widest">// QUANTIFIABLE IMPACT</span>
                    <h2 class="text-3xl font-bold {theme.font_family_display} {theme.text_primary}">{s_title}</h2>
                    <div class="text-9xl sm:text-[13rem] font-black {theme.font_family_display} text-[{theme.accent_color}] tracking-tighter leading-none">
                        {val}
                    </div>
                    <p class="text-2xl {theme.text_secondary} max-w-2xl font-mono">
                        {lbl}
                    </p>
                </div>"""
            elif s_type == "quote" and s_quote:
                q_text = s_quote.get('text', '')
                q_author = s_quote.get('author', 'Steve Jobs')
                inner_html = f"""
                <div class="max-w-4xl mx-auto text-left space-y-8 border-l-4 border-[{theme.accent_color}] pl-10">
                    <blockquote class="text-4xl sm:text-6xl font-serif italic {theme.text_primary} leading-tight">
                        "{q_text}"
                    </blockquote>
                    <div class="{theme.text_secondary} font-mono text-sm uppercase tracking-widest">
                        — {q_author}
                    </div>
                </div>"""
            else:
                cards = ""
                for idx, item in enumerate(s_content):
                    c_title = item.get("title", "") if isinstance(item, dict) else str(item)
                    c_desc = item.get("desc", "") if isinstance(item, dict) else ""
                    c_tag = f"0{idx+1}"
                    cards += f"""
                    <div class="{theme.card_style} relative">
                        <div class="text-xs font-mono text-neutral-500 mb-4">// {c_tag}</div>
                        <h3 class="text-2xl font-bold {theme.font_family_display} {theme.text_primary} mb-3">{c_title}</h3>
                        <p class="{theme.font_family_body} {theme.text_secondary} text-sm leading-relaxed">{c_desc}</p>
                    </div>"""
                
                inner_html = f"""
                <div class="w-full max-w-6xl mx-auto space-y-8">
                    <div class="border-b {theme.border_rule} pb-6 flex items-end justify-between">
                        <div>
                            <span class="text-xs font-mono text-neutral-500 uppercase tracking-widest">// {s_subtitle or 'SECTION'}</span>
                            <h2 class="text-5xl font-black {theme.font_family_display} {theme.text_primary} uppercase tracking-tight mt-1">{s_title}</h2>
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                        {cards}
                    </div>
                </div>"""

            active_cls = "opacity-100 scale-100 z-10" if i == 0 else "opacity-0 scale-95 pointer-events-none absolute inset-0 z-0"
            slides_html += f"""
            <section id="slide-{i}" class="slide-item transition-all duration-400 ease-out flex items-center justify-center p-12 {active_cls}">
                {inner_html}
            </section>"""

        num_slides = len(slides)
        js_block = f"""
    <script>
        lucide.createIcons();
        var currentSlide = 0;
        var totalSlides = {num_slides};

        function updateSlide(newIndex) {{
            if (newIndex < 0 || newIndex >= totalSlides) return;
            
            var prevEl = document.getElementById('slide-' + currentSlide);
            prevEl.classList.remove('opacity-100', 'scale-100', 'z-10');
            prevEl.classList.add('opacity-0', 'scale-95', 'pointer-events-none', 'absolute', 'inset-0', 'z-0');

            currentSlide = newIndex;
            var nextEl = document.getElementById('slide-' + currentSlide);
            nextEl.classList.remove('opacity-0', 'scale-95', 'pointer-events-none', 'absolute', 'inset-0', 'z-0');
            nextEl.classList.add('opacity-100', 'scale-100', 'z-10');

            document.getElementById('slide-indicator').innerText = (currentSlide + 1) + ' / ' + totalSlides;
            var progress = ((currentSlide + 1) / totalSlides) * 100;
            document.getElementById('progress-bar').style.width = progress + '%';
        }}

        function nextSlide() {{ updateSlide(currentSlide + 1); }}
        function prevSlide() {{ updateSlide(currentSlide - 1); }}

        function toggleFullscreen() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen().catch(function() {{}});
            }} else {{
                document.exitFullscreen().catch(function() {{}});
            }}
        }}

        document.addEventListener('keydown', function(e) {{
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
                e.preventDefault();
                nextSlide();
            }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
                e.preventDefault();
                prevSlide();
            }} else if (e.key === 'f' || e.key === 'F') {{
                toggleFullscreen();
            }} else if (e.key === 'Home') {{
                updateSlide(0);
            }} else if (e.key === 'End') {{
                updateSlide(totalSlides - 1);
            }}
        }});

        updateSlide(0);
    </script>"""

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{deck_title} — Keynote Deck</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="{theme.font_import_url}" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="{theme.bg_style} {theme.font_family_body} min-h-screen overflow-hidden flex flex-col justify-between select-none">

    <!-- Progress Line -->
    <div class="fixed top-0 inset-x-0 h-1 bg-neutral-800 z-50">
        <div id="progress-bar" class="h-full bg-[{theme.accent_color}] transition-all duration-200 w-0"></div>
    </div>

    <!-- Header -->
    <header class="p-8 flex items-center justify-between text-xs font-mono uppercase tracking-widest text-neutral-500 z-40 border-b {theme.border_rule}">
        <div class="flex items-center gap-3">
            <span class="font-bold text-white">{deck_title}</span>
        </div>
        <div class="flex items-center gap-4">
            <span>[NAV: ← → / SPACE]</span>
            <button onclick="toggleFullscreen()" class="hover:text-white cursor-pointer">[FULLSCREEN: F]</button>
        </div>
    </header>

    <!-- Main Stage -->
    <main class="flex-1 relative flex items-center justify-center max-w-7xl w-full mx-auto px-8">
        {slides_html}
    </main>

    <!-- Footer -->
    <footer class="p-8 flex items-center justify-between text-xs font-mono uppercase tracking-widest text-neutral-500 z-40 border-t {theme.border_rule}">
        <div>{presenter}</div>
        <div class="flex items-center gap-4">
            <button onclick="prevSlide()" class="p-2 border border-neutral-700 hover:text-white cursor-pointer">PREV</button>
            <span id="slide-indicator" class="font-bold text-white">1 / {num_slides}</span>
            <button onclick="nextSlide()" class="p-2 border border-neutral-700 hover:text-white cursor-pointer">NEXT</button>
        </div>
    </footer>

    {js_block}
</body>
</html>"""
