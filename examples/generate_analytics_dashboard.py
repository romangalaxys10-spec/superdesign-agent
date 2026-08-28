"""Example: Generate an Interactive Analytics Dashboard"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.design_engine import SuperDesignEngine

engine = SuperDesignEngine(output_dir="./output")
out = engine.create_product_dashboard(
    app_name="SolanaSentinel Ops",
    theme_style="modern_saas",
    filename="sentinel_dashboard.html"
)
print(f"Generated Dashboard: {out}")
