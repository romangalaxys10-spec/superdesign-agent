"""
Anti-Slop Product UI & Telemetry HUD Generator.
Teenage Engineering inspired hardware layout, dot matrices, and dense telemetry.
"""

from typing import Dict, List, Any
from .taste_matrix import TasteMatrix, TasteArchetype


class ProductUIGenerator:
    """Generates industrial tactile dashboards with dense operational telemetry."""

    @staticmethod
    def generate_dashboard(
        app_name: str,
        kpis: List[Dict[str, str]],
        theme_style: str = "industrial_hud",
    ) -> str:
        theme = TasteMatrix.get_theme(theme_style)
        
        default_kpis = kpis or [
            {"label": "REVENUE / SEC", "value": "$4.82", "change": "+18.4%", "trend": "up"},
            {"label": "ACTIVE AGENTS", "value": "1,024", "change": "+100%", "trend": "up"},
            {"label": "CLOCK JITTER", "value": "0.02ms", "change": "-42.0%", "trend": "down"},
            {"label": "SYSTEM VERIFY", "value": "100.0%", "change": "STABLE", "trend": "up"},
        ]

        kpis_html = ""
        for idx, k in enumerate(default_kpis):
            kpis_html += f"""
            <div class="{theme.card_style} space-y-3">
                <div class="flex items-center justify-between text-[11px] font-mono {theme.text_secondary}">
                    <span>[{idx+1:02d}] {k['label']}</span>
                    <span class="text-[#FFB000] font-bold">{k['change']}</span>
                </div>
                <div class="text-4xl font-black font-mono {theme.text_primary} tracking-tight">{k['value']}</div>
            </div>"""

        js_block = """
    <script>
        lucide.createIcons();

        var ctx = document.getElementById('throughputChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', 'LIVE'],
                datasets: [{
                    label: 'OPS / SEC',
                    data: [42000, 58000, 71000, 94000, 120000, 115000, 148000, 162000],
                    borderColor: '#FFB000',
                    borderWidth: 2,
                    backgroundColor: 'rgba(255, 176, 0, 0.05)',
                    fill: true,
                    tension: 0.1,
                    pointRadius: 3,
                    pointBackgroundColor: '#FFB000'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#7e8494', font: { family: 'monospace', size: 10 } } },
                    y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#7e8494', font: { family: 'monospace', size: 10 } } }
                }
            }
        });
    </script>"""

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{app_name} — Industrial Telemetry HUD</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="{theme.font_import_url}" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="{theme.bg_style} {theme.font_family_body} min-h-screen p-8 flex flex-col justify-between">

    <!-- Top Hardware Header -->
    <header class="border-b {theme.border_rule} pb-6 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div class="flex items-center gap-4">
            <div class="w-3 h-3 bg-[#FFB000] rounded-full animate-pulse shadow-[0_0_8px_#FFB000]"></div>
            <h1 class="text-2xl font-black font-mono tracking-tight {theme.text_primary} uppercase">{app_name}</h1>
            <span class="{theme.badge_style}">HARDWARE TELEMETRY 1.0</span>
        </div>
        <div class="flex items-center gap-3 font-mono text-xs">
            <span class="text-neutral-500">CLOCK: 100.00 MHz</span>
            <span class="text-neutral-500">|</span>
            <button class="{theme.button_secondary}">DUMP CSV</button>
            <button class="{theme.button_primary}">OVERCLOCK</button>
        </div>
    </header>

    <!-- Main Grid -->
    <main class="space-y-8 flex-1">
        <!-- KPIs -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {kpis_html}
        </div>

        <!-- Telemetry Chart -->
        <div class="{theme.card_style} p-8 space-y-4">
            <div class="flex items-center justify-between border-b {theme.border_rule} pb-4 font-mono text-xs">
                <span class="text-neutral-400 font-bold uppercase">// DETERMINISTIC THROUGHPUT OSCILLOSCOPE</span>
                <span class="text-[#FFB000]">[SAMPLE: REALTIME]</span>
            </div>
            <div class="h-80">
                <canvas id="throughputChart"></canvas>
            </div>
        </div>
    </main>

    <!-- Bottom Telemetry Footer -->
    <footer class="mt-8 pt-6 border-t {theme.border_rule} flex items-center justify-between font-mono text-xs {theme.text_secondary}">
        <div>UNIT: TEENAGE_ENGINEERING_HUD_01</div>
        <div>ZERO AI SLOP COMPLIANT</div>
    </footer>

    {js_block}
</body>
</html>"""
