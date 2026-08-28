"""
Site & Landing Page Generator.
Generates full-fidelity, responsive, production-ready landing pages with Tailwind CSS, Lucide icons, and interactive widgets.
"""

from typing import Dict, List, Optional, Any
from .theme_matrix import ThemeMatrix, ThemeStyle, DesignTheme


class SiteGenerator:
    """Generates complete responsive web experiences."""

    @staticmethod
    def generate_site(
        title: str,
        tagline: str,
        description: str,
        features: List[Dict[str, str]],
        theme_style: str = "modern_saas",
        cta_text: str = "Get Started Free",
        metrics: Optional[List[Dict[str, str]]] = None,
        pricing_plans: Optional[List[Dict[str, Any]]] = None,
        testimonials: Optional[List[Dict[str, str]]] = None,
        faqs: Optional[List[Dict[str, str]]] = None,
    ) -> str:
        theme = ThemeMatrix.get_theme(theme_style)
        
        default_metrics = metrics or [
            {"value": "99.99%", "label": "Uptime Guarantee"},
            {"value": "<10ms", "label": "Sub-millisecond Latency"},
            {"value": "10M+", "label": "Events Processed / Sec"},
            {"value": "4.9/5", "label": "Developer Satisfaction"},
        ]

        default_pricing = pricing_plans or [
            {
                "name": "Starter",
                "price": "$0",
                "period": "/mo",
                "desc": "Perfect for indie hackers and side projects.",
                "features": ["10,000 requests/mo", "Community support", "1 workspace", "Basic analytics"],
                "popular": False,
                "cta": "Start for Free"
            },
            {
                "name": "Pro Architect",
                "price": "$49",
                "period": "/mo",
                "desc": "For high-velocity engineering teams.",
                "features": ["Unlimited requests", "24/7 Dedicated SLA", "Infinite workspaces", "Deep AI telemetry", "Custom webhooks"],
                "popular": True,
                "cta": "Start 14-Day Free Trial"
            },
            {
                "name": "Enterprise",
                "price": "Custom",
                "period": "",
                "desc": "Dedicated infrastructure & bespoke compliance.",
                "features": ["Self-hosted VPC option", "SOC2 Type II compliance", "Custom model fine-tuning", "Dedicated solutions architect"],
                "popular": False,
                "cta": "Contact Sales"
            }
        ]

        default_faqs = faqs or [
            {
                "q": "How does SuperDesign Agent generate code without external credits?",
                "a": "It utilizes deterministic design systems, token matrix heuristics, and local generative layouts without any API rate limits or recurring monthly credits."
            },
            {
                "q": "Can I export to React / Next.js?",
                "a": "Yes! All components are built with standard Tailwind utility classes and modular HTML structure that translates directly to React/Vue/Svelte."
            },
            {
                "q": "Are the layouts responsive on mobile devices?",
                "a": "100%. Every block includes mobile breakpoints (sm, md, lg, xl) with responsive typography, collapsible navigation, and touch-friendly controls."
            }
        ]

        # Features HTML
        features_html = ""
        for i, feat in enumerate(features):
            icon = feat.get("icon", "sparkles")
            f_title = feat.get("title", f"Feature {i+1}")
            f_desc = feat.get("desc", "High-performance modular architecture engineered for maximum developer velocity.")
            features_html += f"""
            <div class="{theme.card_bg} {theme.card_border} p-8 rounded-2xl relative overflow-hidden group">
                <div class="w-12 h-12 rounded-xl {theme.badge_style} flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                    <i data-lucide="{icon}" class="w-6 h-6"></i>
                </div>
                <h3 class="text-xl font-bold {theme.text_primary} mb-3">{f_title}</h3>
                <p class="{theme.text_secondary} leading-relaxed text-sm">{f_desc}</p>
            </div>"""

        # Metrics HTML
        metrics_html = ""
        for m in default_metrics:
            metrics_html += f"""
            <div class="text-center p-6">
                <div class="text-4xl lg:text-5xl font-extrabold {theme.text_primary} mb-2 tracking-tight">{m['value']}</div>
                <div class="{theme.text_secondary} text-sm font-medium">{m['label']}</div>
            </div>"""

        # Pricing HTML
        pricing_html = ""
        for p in default_pricing:
            pop_badge = f'<span class="{theme.badge_style} absolute -top-3 left-1/2 -translate-x-1/2">Most Popular</span>' if p["popular"] else ""
            border_cls = "ring-2 ring-indigo-500 shadow-2xl" if p["popular"] and "saas" in theme.key else theme.card_border
            btn_cls = theme.button_primary if p["popular"] else theme.button_secondary
            
            p_features = "".join([f'<li class="flex items-center gap-3 text-sm {theme.text_secondary}"><i data-lucide="check" class="w-4 h-4 text-emerald-400 shrink-0"></i>{item}</li>' for item in p["features"]])

            pricing_html += f"""
            <div class="{theme.card_bg} {border_cls} p-8 rounded-3xl relative flex flex-col justify-between">
                {pop_badge}
                <div>
                    <h4 class="text-xl font-bold {theme.text_primary} mb-2">{p['name']}</h4>
                    <p class="{theme.text_secondary} text-xs mb-6">{p['desc']}</p>
                    <div class="flex items-baseline gap-1 mb-6">
                        <span class="text-4xl font-extrabold {theme.text_primary}">{p['price']}</span>
                        <span class="{theme.text_secondary} text-sm">{p['period']}</span>
                    </div>
                    <ul class="space-y-3 mb-8">
                        {p_features}
                    </ul>
                </div>
                <button class="{btn_cls} w-full text-center block cursor-pointer">{p['cta']}</button>
            </div>"""

        # FAQs HTML
        faqs_html = ""
        for i, faq in enumerate(default_faqs):
            faqs_html += f"""
            <div class="{theme.card_bg} {theme.card_border} rounded-2xl p-6 transition-all">
                <button onclick="toggleFaq({i})" class="w-full flex items-center justify-between text-left font-bold {theme.text_primary} text-lg cursor-pointer">
                    <span>{faq['q']}</span>
                    <i id="faq-icon-{i}" data-lucide="chevron-down" class="w-5 h-5 transition-transform duration-300"></i>
                </button>
                <div id="faq-answer-{i}" class="hidden mt-4 {theme.text_secondary} text-sm leading-relaxed border-t border-slate-800/50 pt-4">
                    {faq['a']}
                </div>
            </div>"""

        js_script = """
    <script>
        lucide.createIcons();

        function toggleFaq(index) {
            var ans = document.getElementById('faq-answer-' + index);
            var icon = document.getElementById('faq-icon-' + index);
            if (ans.classList.contains('hidden')) {
                ans.classList.remove('hidden');
                icon.style.transform = 'rotate(180deg)';
            } else {
                ans.classList.add('hidden');
                icon.style.transform = 'rotate(0deg)';
            }
        }
    </script>"""

        # Build full HTML
        return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — {tagline}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,700;1,6..72,400&display=swap');
    </style>
</head>
<body class="{theme.body_bg} {theme.font_family} min-h-screen selection:bg-indigo-500 selection:text-white">

    <!-- Navigation -->
    <header class="fixed top-0 inset-x-0 z-50 px-6 py-4">
        <nav class="max-w-7xl mx-auto {theme.card_bg} {theme.card_border} rounded-2xl px-6 py-3 flex items-center justify-between shadow-lg">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl {theme.accent_gradient} flex items-center justify-center text-white font-black shadow-md">
                    <i data-lucide="sparkles" class="w-5 h-5"></i>
                </div>
                <span class="text-lg font-bold tracking-tight {theme.text_primary}">{title}</span>
            </div>
            <div class="hidden md:flex items-center gap-8 text-sm font-medium {theme.text_secondary}">
                <a href="#features" class="hover:{theme.text_primary} transition-colors">Features</a>
                <a href="#metrics" class="hover:{theme.text_primary} transition-colors">Performance</a>
                <a href="#pricing" class="hover:{theme.text_primary} transition-colors">Pricing</a>
                <a href="#faq" class="hover:{theme.text_primary} transition-colors">FAQ</a>
            </div>
            <div class="flex items-center gap-4">
                <a href="#pricing" class="{theme.button_primary} text-xs py-2 px-4 shadow-sm">{cta_text}</a>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="relative pt-36 pb-20 px-6 overflow-hidden">
        <div class="max-w-5xl mx-auto text-center relative z-10">
            <div class="inline-flex items-center gap-2 {theme.badge_style} mb-8">
                <i data-lucide="zap" class="w-3.5 h-3.5"></i>
                <span>{tagline}</span>
            </div>
            <h1 class="text-5xl md:text-7xl font-extrabold {theme.text_primary} tracking-tight leading-[1.1] mb-8">
                Design & Ship at the <br>
                <span class="{theme.accent_gradient} bg-clip-text text-transparent">Speed of Thought</span>
            </h1>
            <p class="text-lg md:text-xl {theme.text_secondary} max-w-3xl mx-auto leading-relaxed mb-10">
                {description}
            </p>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                <a href="#pricing" class="{theme.button_primary} text-base px-8 py-4 flex items-center gap-2">
                    <span>{cta_text}</span>
                    <i data-lucide="arrow-right" class="w-5 h-5"></i>
                </a>
                <a href="#features" class="{theme.button_secondary} text-base px-8 py-4">
                    Explore Architecture
                </a>
            </div>
        </div>
    </section>

    <!-- Metrics Section -->
    <section id="metrics" class="py-12 border-y border-slate-800/40 bg-slate-950/20">
        <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-6">
            {metrics_html}
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-24 px-6 max-w-7xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-16">
            <h2 class="text-3xl md:text-5xl font-extrabold {theme.text_primary} mb-4">Engineered for Radical Velocity</h2>
            <p class="{theme.text_secondary} text-base">Uncompromising performance, modular component design, and zero credit limits.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            {features_html}
        </div>
    </section>

    <!-- Pricing Section -->
    <section id="pricing" class="py-24 px-6 max-w-7xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-16">
            <h2 class="text-3xl md:text-5xl font-extrabold {theme.text_primary} mb-4">Simple, Transparent Pricing</h2>
            <p class="{theme.text_secondary} text-base">No hidden credits. No per-prompt metered fees. Own your tools forever.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch">
            {pricing_html}
        </div>
    </section>

    <!-- FAQ Section -->
    <section id="faq" class="py-20 px-6 max-w-4xl mx-auto">
        <div class="text-center mb-12">
            <h2 class="text-3xl font-extrabold {theme.text_primary} mb-3">Frequently Asked Questions</h2>
            <p class="{theme.text_secondary} text-sm">Everything you need to know about SuperDesign Agent.</p>
        </div>
        <div class="space-y-4">
            {faqs_html}
        </div>
    </section>

    <!-- Footer -->
    <footer class="border-t border-slate-800/60 py-12 px-6">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6 text-sm {theme.text_secondary}">
            <div class="flex items-center gap-2">
                <i data-lucide="sparkles" class="w-5 h-5 text-indigo-400"></i>
                <span class="font-bold {theme.text_primary}">{title}</span>
                <span>© 2026. All rights reserved.</span>
            </div>
            <div class="flex gap-6">
                <a href="#" class="hover:{theme.text_primary}">Privacy</a>
                <a href="#" class="hover:{theme.text_primary}">Terms</a>
                <a href="https://github.com/romangalaxys10-spec" class="hover:{theme.text_primary}">GitHub</a>
            </div>
        </div>
    </footer>

    {js_script}
</body>
</html>"""
