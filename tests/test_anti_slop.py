"""Unit tests for Anti-Slop Linter, Taste Matrix & Generators"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.anti_slop_linter import AntiSlopAuditor
from core.taste_matrix import TasteMatrix, TasteArchetype
from core.site_generator import SiteGenerator
from core.slide_generator import SlideGenerator
from core.product_ui_generator import ProductUIGenerator


class TestAntiSlop(unittest.TestCase):
    def test_linter_detects_slop(self):
        sloppy_html = """
        <div class="from-indigo-500 to-pink-500">
            <h1>Supercharge your workflow and empower teams seamlessly!</h1>
        </div>
        """
        report = AntiSlopAuditor.audit_html(sloppy_html)
        self.assertFalse(report.is_slop_free)
        self.assertGreater(report.slop_score, 0.4)
        rule_ids = [v.rule_id for v in report.violations]
        self.assertIn("SLOP_PURPLE_GRADIENT_BLOB", rule_ids)
        self.assertIn("SLOP_BUZZWORD_CLICHE", rule_ids)

    def test_linter_approves_swiss_site(self):
        clean_site = SiteGenerator.generate_site(
            title="SwissCore",
            tagline="BAUHAUS PROTOCOL",
            description="Deterministic cognitive systems engineering with mathematical precision.",
            features=[{"title": "Grid Precision", "desc": "Asymmetric bounding rules."}],
            theme_style="swiss_international"
        )
        report = AntiSlopAuditor.audit_html(clean_site)
        self.assertTrue(report.is_slop_free)
        self.assertIn("A+", report.taste_grade)

    def test_taste_matrix_archetypes(self):
        swiss = TasteMatrix.get_theme("swiss_international")
        self.assertEqual(swiss.accent_color, "#FF3B00")
        self.assertIn("Syne", swiss.font_family_display)

        hud = TasteMatrix.get_theme("industrial_hud")
        self.assertEqual(hud.accent_color, "#FFB000")
        self.assertIn("Chivo_Mono", hud.font_family_display)

    def test_slide_generator(self):
        deck = SlideGenerator.generate_deck(
            deck_title="Anti-Slop Vision",
            presenter="Architect",
            slides=[{"type": "title", "title": "Anti-Slop Vision", "subtitle": "KEYNOTE"}],
            theme_style="swiss_international"
        )
        self.assertIn("ANTI-SLOP", deck.upper())
        self.assertIn("KEYNOTE SPECIFICATION", deck)

    def test_product_dashboard(self):
        hud = ProductUIGenerator.generate_dashboard(
            app_name="SynthOps",
            kpis=[{"label": "CLOCK JITTER", "value": "0.01ms", "change": "STABLE"}],
            theme_style="industrial_hud"
        )
        self.assertIn("HARDWARE TELEMETRY", hud)
        self.assertIn("CLOCK JITTER", hud)


if __name__ == "__main__":
    unittest.main()
