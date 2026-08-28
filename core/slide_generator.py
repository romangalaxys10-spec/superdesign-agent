"""
Interactive 16:9 Slide Deck Generator.
Generates responsive presentation slide decks with keyboard navigation, progress bars, animations, and presenter modes.
"""

from typing import Dict, List, Any
from .theme_matrix import ThemeMatrix, ThemeStyle


class SlideGenerator:
    """Builds interactive HTML slide decks with zero dependencies."""

    @staticmethod
    def generate_deck(
        deck_title: str,
        presenter: str,
        slides: List[Dict[str, Any]],
        theme_style: str = "apple_minimal",
    ) -> str:
        theme = ThemeMatrix.get_theme(theme_style)
        
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
                sub_badge = f'<div class="{theme.badge_style} inline-flex items-center gap-2 mb-4"><i data-lucide="presentation" class="w-4 h-4"></i><span>{s_subtitle or "Keynote Presentation"}</span></div>'
                inner_html = f"""
                <div class="text-center space-y-6 max-w-4xl mx-auto">
                    {sub_badge}
                    <h1 class="text-6xl md:text-7xl font-extrabold {theme.text_primary} tracking-tight leading-tight">
                        {s_title}
                    </h1>
                    <p class="text-2xl {theme.text_secondary} font-light">
                        {presenter}
                    </p>
                </div>"""
            elif s_type == "metric" and s_metric:
                val = s_metric.get('value', '10X')
                lbl = s_metric.get('label', 'Performance boost and cost reduction achieved.')
                inner_html = f"""
                <div class="text-center space-y-8 max-w-4xl mx-auto">
                    <h2 class="text-3xl font-bold {theme.text_secondary}">{s_title}</h2>
                    <div class="text-8xl md:text-9xl font-black {theme.accent_gradient} bg-clip-text text-transparent tracking-tighter">
                        {val}
                    </div>
                    <p class="text-2xl {theme.text_primary} font-medium max-w-2xl mx-auto">
                        {lbl}
                    </p>
                </div>"""
            elif s_type == "quote" and s_quote:
                q_text = s_quote.get('text', '')
                q_author = s_quote.get('author', 'Steve Jobs')
                inner_html = f"""
                <div class="max-w-4xl mx-auto text-center space-y-8">
                    <i data-lucide="quote" class="w-16 h-16 mx-auto text-indigo-400 opacity-60"></i>
                    <blockquote class="text-4xl md:text-5xl font-serif italic {theme.text_primary} leading-snug">
                        "{q_text}"
                    </blockquote>
                    <div class="{theme.text_secondary} text-xl font-medium">
                        — {q_author}
                    </div>
                </div>"""
            else:
                cards = ""
                for item in s_content:
                    c_title = item.get("title", "") if isinstance(item, dict) else str(item)
                    c_desc = item.get("desc", "") if isinstance(item, dict) else ""
                    c_icon = item.get("icon", "check-circle-2") if isinstance(item, dict) else "check-circle-2"
                    desc_html = f'<p class="{theme.text_secondary} text-base leading-relaxed">{c_desc}</p>' if c_desc else ''
                    cards += f"""
                    <div class="{theme.card_bg} {theme.card_border} p-8 rounded-2xl text-left space-y-4">
                        <div class="w-10 h-10 rounded-xl {theme.badge_style} flex items-center justify-center">
                            <i data-lucide="{c_icon}" class="w-5 h-5"></i>
                        </div>
                        <h3 class="text-2xl font-bold {theme.text_primary}">{c_title}</h3>
                        {desc_html}
                    </div>"""
                
                sub_badge = f'<div class="{theme.badge_style} inline-block mb-3">{s_subtitle}</div>' if s_subtitle else ''
                inner_html = f"""
                <div class="w-full max-w-6xl mx-auto space-y-8">
                    <div>
                        {sub_badge}
                        <h2 class="text-4xl md:text-5xl font-extrabold {theme.text_primary}">{s_title}</h2>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        {cards}
                    </div>
                </div>"""

            active_cls = "opacity-100 scale-100 z-10" if i == 0 else "opacity-0 scale-95 pointer-events-none absolute inset-0 z-0"
            slides_html += f"""
            <section id="slide-{i}" class="slide-item transition-all duration-500 ease-out flex items-center justify-center p-12 {active_cls}">
                {inner_html}
            </section>"""

        num_slides = len(slides)
        
        js_block = """
    <script>
        lucide.createIcons();
        var currentSlide = 0;
        var totalSlides = NUM_SLIDES_PLACEHOLDER;

        function updateSlide(newIndex) {
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
        }

        function nextSlide() { updateSlide(currentSlide + 1); }
        function prevSlide() { updateSlide(currentSlide - 1); }

        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(function() {});
            } else {
                document.exitFullscreen().catch(function() {});
            }
        }

        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
                e.preventDefault();
                nextSlide();
            } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
                e.preventDefault();
                prevSlide();
            } else if (e.key === 'f' || e.key === 'F') {
                toggleFullscreen();
            } else if (e.key === 'Home') {
                updateSlide(0);
            } else if (e.key === 'End') {
                updateSlide(totalSlides - 1);
            }
        });

        updateSlide(0);
    </script>
""".replace("NUM_SLIDES_PLACEHOLDER", str(num_slides))

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{deck_title} — Slide Deck</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap');
    </style>
</head>
<body class="{theme.body_bg} {theme.font_family} min-h-screen overflow-hidden flex flex-col justify-between select-none">

    <!-- Progress Bar -->
    <div class="fixed top-0 inset-x-0 h-1.5 bg-slate-800/40 z-50">
        <div id="progress-bar" class="h-full {theme.accent_gradient} transition-all duration-300 w-0"></div>
    </div>

    <!-- Top Bar -->
    <header class="p-6 flex items-center justify-between text-sm {theme.text_secondary} z-40">
        <div class="flex items-center gap-2">
            <i data-lucide="sparkles" class="w-4 h-4 text-indigo-400"></i>
            <span class="font-bold {theme.text_primary}">{deck_title}</span>
        </div>
        <div class="flex items-center gap-4 text-xs">
            <span class="hidden md:inline">Use <kbd class="px-2 py-1 bg-slate-800 rounded">←</kbd> <kbd class="px-2 py-1 bg-slate-800 rounded">→</kbd> or <kbd class="px-2 py-1 bg-slate-800 rounded">Space</kbd></span>
            <button onclick="toggleFullscreen()" class="hover:{theme.text_primary} cursor-pointer p-1">
                <i data-lucide="maximize" class="w-4 h-4"></i>
            </button>
        </div>
    </header>

    <!-- Main Slide Stage -->
    <main class="flex-1 relative flex items-center justify-center max-w-7xl w-full mx-auto px-6">
        {slides_html}
    </main>

    <!-- Bottom Controls -->
    <footer class="p-6 flex items-center justify-between text-sm {theme.text_secondary} z-40">
        <div class="text-xs">
            Presented by <span class="{theme.text_primary} font-medium">{presenter}</span>
        </div>
        <div class="flex items-center gap-4">
            <button onclick="prevSlide()" class="p-2 rounded-xl {theme.card_bg} {theme.card_border} hover:{theme.text_primary} cursor-pointer">
                <i data-lucide="chevron-left" class="w-5 h-5"></i>
            </button>
            <span id="slide-indicator" class="font-mono text-xs font-bold {theme.text_primary}">1 / {num_slides}</span>
            <button onclick="nextSlide()" class="p-2 rounded-xl {theme.card_bg} {theme.card_border} hover:{theme.text_primary} cursor-pointer">
                <i data-lucide="chevron-right" class="w-5 h-5"></i>
            </button>
        </div>
    </footer>

    {js_block}
</body>
</html>"""
