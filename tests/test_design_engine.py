"""Unit tests for SuperDesign Engine & Theme Matrix"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.theme_matrix import ThemeMatrix, ThemeStyle
from core.design_engine import SuperDesignEngine
from core.site_generator import SiteGenerator
from core.slide_generator import SlideGenerator
from core.product_ui_generator import ProductUIGenerator


class TestSuperDesign(unittest.TestCase):
    def test_theme_matrix(self):
        theme_saas = ThemeMatrix.get_theme("modern_saas")
        self.assertEqual(theme_saas.key, "modern_saas")
        self.assertIn("bg-[#0a0d14]", theme_saas.body_bg)

        theme_apple = ThemeMatrix.get_theme("apple_minimal")
        self.assertEqual(theme_apple.key, "apple_minimal")
        self.assertIn("bg-[#000000]", theme_apple.body_bg)

    def test_site_generator(self):
        html = SiteGenerator.generate_site(
            title="TestPlatform",
            tagline="High Performance AI",
            description="Testing autonomous site synthesis",
            features=[{"title": "Fast Execution", "desc": "Sub-millisecond speed", "icon": "zap"}],
            theme_style="modern_saas"
        )
        self.assertIn("TestPlatform", html)
        self.assertIn("Sub-millisecond speed", html)
        self.assertIn("lucide.createIcons", html)

    def test_slide_generator(self):
        html = SlideGenerator.generate_deck(
            deck_title="AI Vision 2026",
            presenter="Lead Architect",
            slides=[
                {"type": "title", "title": "AI Vision 2026", "subtitle": "Keynote"},
                {"type": "metric", "title": "Growth", "metric": {"value": "10X", "label": "Velocity"}}
            ],
            theme_style="apple_minimal"
        )
        self.assertIn("AI Vision 2026", html)
        self.assertIn("10X", html)
        self.assertIn("updateSlide", html)

    def test_product_dashboard(self):
        html = ProductUIGenerator.generate_dashboard(
            app_name="TelemetryHub",
            kpis=[{"label": "Throughput", "value": "1.2M", "change": "+14%", "trend": "up"}],
            theme_style="modern_saas"
        )
        self.assertIn("TelemetryHub", html)
        self.assertIn("throughputChart", html)

    def test_infinite_canvas_variants(self):
        engine = SuperDesignEngine(output_dir="./output")
        canvas_path = engine.generate_infinite_canvas_variants("Autonomous Agent OS", "NexusEngine")
        self.assertTrue(os.path.exists(canvas_path))


if __name__ == "__main__":
    unittest.main()
