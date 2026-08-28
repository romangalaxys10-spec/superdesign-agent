"""
Product UI & Dashboard Generator.
Generates responsive SaaS dashboards, Chart.js analytics charts, KPI cards, tables, and settings interfaces.
"""

from typing import Dict, List, Any
from .theme_matrix import ThemeMatrix, ThemeStyle


class ProductUIGenerator:
    """Generates production-grade product dashboards and web application components."""

    @staticmethod
    def generate_dashboard(
        app_name: str,
        kpis: List[Dict[str, str]],
        theme_style: str = "modern_saas",
    ) -> str:
        theme = ThemeMatrix.get_theme(theme_style)
        
        default_kpis = kpis or [
            {"label": "Monthly Recurring Revenue", "value": "$142,850", "change": "+18.4%", "trend": "up"},
            {"label": "Active Autonomous Agents", "value": "24,890", "change": "+32.1%", "trend": "up"},
            {"label": "Avg Execution Latency", "value": "4.2 ms", "change": "-12.0%", "trend": "down"},
            {"label": "System Health Score", "value": "99.98%", "change": "+0.2%", "trend": "up"},
        ]

        kpis_html = ""
        for k in default_kpis:
            color_cls = "text-emerald-400 bg-emerald-500/10" if k.get("trend") == "up" else "text-indigo-400 bg-indigo-500/10"
            icon = "trending-up" if k.get("trend") == "up" else "trending-down"
            kpis_html += f"""
            <div class="{theme.card_bg} {theme.card_border} p-6 rounded-2xl space-y-3">
                <div class="flex items-center justify-between text-xs {theme.text_secondary}">
                    <span>{k['label']}</span>
                    <span class="flex items-center gap-1 px-2 py-0.5 rounded-md {color_cls} font-semibold">
                        <i data-lucide="{icon}" class="w-3.5 h-3.5"></i>
                        {k['change']}
                    </span>
                </div>
                <div class="text-3xl font-extrabold {theme.text_primary} tracking-tight">{k['value']}</div>
            </div>"""

        js_block = """
    <script>
        lucide.createIcons();

        // Chart 1: Throughput Area Chart
        var ctx1 = document.getElementById('throughputChart').getContext('2d');
        new Chart(ctx1, {
            type: 'line',
            data: {
                labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00', 'Now'],
                datasets: [{
                    label: 'OPS / sec',
                    data: [12000, 19000, 34000, 52000, 48000, 68000, 84000],
                    borderColor: '#6366f1',
                    backgroundColor: 'rgba(99, 102, 241, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                    y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } }
                }
            }
        });

        // Chart 2: Workload Doughnut
        var ctx2 = document.getElementById('workloadChart').getContext('2d');
        new Chart(ctx2, {
            type: 'doughnut',
            data: {
                labels: ['Web Design', 'Slide Decks', 'Code Audits', 'Telemetry'],
                datasets: [{
                    data: [40, 25, 20, 15],
                    backgroundColor: ['#6366f1', '#ec4899', '#06b6d4', '#10b981'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 11 } } }
                }
            }
        });
    </script>
"""

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{app_name} — Analytics & Ops Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');
    </style>
</head>
<body class="{theme.body_bg} {theme.font_family} min-h-screen flex">

    <!-- Sidebar -->
    <aside class="w-64 border-r border-slate-800/80 p-6 flex flex-col justify-between hidden md:flex">
        <div class="space-y-8">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl {theme.accent_gradient} flex items-center justify-center text-white font-black shadow-md">
                    <i data-lucide="layers" class="w-5 h-5"></i>
                </div>
                <span class="text-lg font-bold tracking-tight {theme.text_primary}">{app_name}</span>
            </div>
            <nav class="space-y-2 text-sm font-medium">
                <a href="#" class="flex items-center gap-3 px-4 py-2.5 rounded-xl bg-indigo-600/10 text-indigo-400 font-semibold border border-indigo-500/20">
                    <i data-lucide="layout-dashboard" class="w-4 h-4"></i>
                    <span>Dashboard</span>
                </a>
                <a href="#" class="flex items-center gap-3 px-4 py-2.5 rounded-xl {theme.text_secondary} hover:{theme.text_primary} hover:bg-slate-800/40 transition-colors">
                    <i data-lucide="bot" class="w-4 h-4"></i>
                    <span>Agents</span>
                </a>
                <a href="#" class="flex items-center gap-3 px-4 py-2.5 rounded-xl {theme.text_secondary} hover:{theme.text_primary} hover:bg-slate-800/40 transition-colors">
                    <i data-lucide="activity" class="w-4 h-4"></i>
                    <span>Telemetry</span>
                </a>
                <a href="#" class="flex items-center gap-3 px-4 py-2.5 rounded-xl {theme.text_secondary} hover:{theme.text_primary} hover:bg-slate-800/40 transition-colors">
                    <i data-lucide="settings" class="w-4 h-4"></i>
                    <span>Settings</span>
                </a>
            </nav>
        </div>
        <div class="p-4 rounded-xl {theme.card_bg} {theme.card_border} text-xs space-y-2">
            <div class="font-bold {theme.text_primary}">SuperDesign Engine</div>
            <div class="{theme.text_secondary}">100% Credit-Free Local Runtime</div>
        </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 p-8 overflow-y-auto max-w-7xl mx-auto space-y-8">
        <!-- Header -->
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div>
                <h1 class="text-3xl font-extrabold {theme.text_primary} tracking-tight">Mission Control</h1>
                <p class="{theme.text_secondary} text-sm">Real-time telemetry and agentic cognitive telemetry.</p>
            </div>
            <div class="flex items-center gap-3">
                <button class="{theme.button_secondary} text-xs py-2.5 px-4 flex items-center gap-2 cursor-pointer">
                    <i data-lucide="download" class="w-4 h-4"></i> Export CSV
                </button>
                <button class="{theme.button_primary} text-xs py-2.5 px-4 flex items-center gap-2 cursor-pointer">
                    <i data-lucide="plus" class="w-4 h-4"></i> Spawn Agent
                </button>
            </div>
        </div>

        <!-- KPIs Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {kpis_html}
        </div>

        <!-- Charts Section -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div class="lg:col-span-2 {theme.card_bg} {theme.card_border} p-6 rounded-2xl space-y-4">
                <div class="flex items-center justify-between">
                    <h3 class="font-bold {theme.text_primary}">Execution Throughput & Requests</h3>
                    <span class="{theme.badge_style}">Live Feed</span>
                </div>
                <div class="h-72">
                    <canvas id="throughputChart"></canvas>
                </div>
            </div>
            <div class="{theme.card_bg} {theme.card_border} p-6 rounded-2xl space-y-4">
                <h3 class="font-bold {theme.text_primary}">Agent Workload Mix</h3>
                <div class="h-72 flex items-center justify-center">
                    <canvas id="workloadChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Live Events Table -->
        <div class="{theme.card_bg} {theme.card_border} rounded-2xl p-6 space-y-4">
            <h3 class="font-bold {theme.text_primary}">Recent Cognitive Executions</h3>
            <div class="overflow-x-auto">
                <table class="w-full text-left text-sm {theme.text_secondary}">
                    <thead class="border-b border-slate-800/80 text-xs uppercase tracking-wider {theme.text_primary}">
                        <tr>
                            <th class="py-3 px-4">Agent Node</th>
                            <th class="py-3 px-4">Goal / Instruction</th>
                            <th class="py-3 px-4">Status</th>
                            <th class="py-3 px-4">Duration</th>
                            <th class="py-3 px-4 text-right">Action</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/50">
                        <tr class="hover:bg-slate-800/30">
                            <td class="py-3.5 px-4 font-semibold {theme.text_primary}">SolanaStreamer</td>
                            <td class="py-3.5 px-4">Meteora DLMM pool sniffer</td>
                            <td class="py-3.5 px-4"><span class="px-2 py-1 rounded-md text-xs font-semibold bg-emerald-500/10 text-emerald-400">COMPLETED</span></td>
                            <td class="py-3.5 px-4">12.4 ms</td>
                            <td class="py-3.5 px-4 text-right"><button class="text-indigo-400 hover:text-indigo-300 text-xs font-medium">Inspect</button></td>
                        </tr>
                        <tr class="hover:bg-slate-800/30">
                            <td class="py-3.5 px-4 font-semibold {theme.text_primary}">CodeAuditor</td>
                            <td class="py-3.5 px-4">Zero-trust IAM policy scan</td>
                            <td class="py-3.5 px-4"><span class="px-2 py-1 rounded-md text-xs font-semibold bg-emerald-500/10 text-emerald-400">COMPLETED</span></td>
                            <td class="py-3.5 px-4">45.1 ms</td>
                            <td class="py-3.5 px-4 text-right"><button class="text-indigo-400 hover:text-indigo-300 text-xs font-medium">Inspect</button></td>
                        </tr>
                        <tr class="hover:bg-slate-800/30">
                            <td class="py-3.5 px-4 font-semibold {theme.text_primary}">SuperDesigner</td>
                            <td class="py-3.5 px-4">Generate 16:9 keynote deck</td>
                            <td class="py-3.5 px-4"><span class="px-2 py-1 rounded-md text-xs font-semibold bg-indigo-500/10 text-indigo-400">ACTIVE</span></td>
                            <td class="py-3.5 px-4">6.2 ms</td>
                            <td class="py-3.5 px-4 text-right"><button class="text-indigo-400 hover:text-indigo-300 text-xs font-medium">Inspect</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    {js_block}
</body>
</html>"""
