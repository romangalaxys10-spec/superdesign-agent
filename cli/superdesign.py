"""
SuperDesign Agent CLI.
Build sites, slides, products, and parallel canvas variants without external credits.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from core.design_engine import SuperDesignEngine
from core.theme_matrix import ThemeMatrix
from preview_server.server import start_preview_server


def cmd_site(args):
    engine = SuperDesignEngine(output_dir=args.out_dir)
    print(f"🚀 Generating responsive website: '{args.title}' with theme '{args.theme}'...")
    features = [
        {"title": "Real-time AI Synthesis", "desc": "Generates production-grade UI code on demand.", "icon": "sparkles"},
        {"title": "Zero Third-Party Credits", "desc": "Local deterministic design engine with zero API bill shock.", "icon": "shield-check"},
        {"title": "Seamless Code Export", "desc": "100% standard Tailwind CSS and modern HTML/React.", "icon": "code"},
    ]
    out_file = engine.create_site(
        title=args.title,
        tagline=args.tagline or "Supercharge Your AI Product Workflow",
        description=args.prompt or "Transform plain English concepts into responsive websites and interactive slides instantly.",
        features=features,
        theme_style=args.theme,
        filename=args.file,
    )
    print(f"✅ Website generated successfully at: {out_file}")


def cmd_slide(args):
    engine = SuperDesignEngine(output_dir=args.out_dir)
    print(f"📊 Generating {args.slides_count}-slide presentation deck: '{args.title}'...")
    
    slides_data = [
        {"type": "title", "title": args.title, "subtitle": "AI-Powered Architecture & Vision"},
        {
            "type": "content",
            "title": "The Problem with Modern Design Tools",
            "subtitle": "High Friction & Hidden Paywalls",
            "content": [
                {"title": "Credit Traps", "desc": "$30/mo for 50 design generations is unsustainable.", "icon": "alert-triangle"},
                {"title": "Figma-to-Code Gap", "desc": "Designers deliver canvas shapes, developers rebuild from scratch.", "icon": "scissors"},
                {"title": "Slow Iteration", "desc": "Days spent tweaking margins and padding.", "icon": "clock"},
            ]
        },
        {
            "type": "metric",
            "title": "Unrivaled Engineering Velocity",
            "metric": {"value": "10X", "label": "Faster turnaround from prompt to live production UI"}
        },
        {
            "type": "content",
            "title": "The Three Architectural Pillars",
            "subtitle": "Radical Simplicity",
            "content": [
                {"title": "1. Zero-Credit Engine", "desc": "Runs 100% locally with zero external API dependencies.", "icon": "cpu"},
                {"title": "2. Production Tailwind", "desc": "Outputs clean, maintainable, responsive code.", "icon": "code-2"},
                {"title": "3. Multi-Theme Matrix", "desc": "Apple Minimal, Modern SaaS, Cyberpunk, and Neo-Brutalist.", "icon": "palette"},
            ]
        },
        {
            "type": "quote",
            "quote": {
                "text": "Design is not just what it looks like and feels like. Design is how it works.",
                "author": "Steve Jobs"
            }
        }
    ]
    
    out_file = SuperDesignEngine.create_slide_deck(
        deck_title=args.title,
        presenter=args.presenter,
        slides=slides_data[:args.slides_count],
        theme_style=args.theme,
        output_dir=args.out_dir,
        filename=args.file,
    )
    print(f"✅ Slide deck generated successfully at: {out_file}")


def cmd_product(args):
    engine = SuperDesignEngine(output_dir=args.out_dir)
    print(f"💻 Generating Product Dashboard: '{args.name}'...")
    out_file = engine.create_product_dashboard(
        app_name=args.name,
        theme_style=args.theme,
        filename=args.file,
    )
    print(f"✅ Dashboard generated successfully at: {out_file}")


def cmd_explore(args):
    engine = SuperDesignEngine(output_dir=args.out_dir)
    print(f"🎨 Generating 4-variant parallel style exploration for: '{args.prompt}'...")
    out_file = engine.generate_infinite_canvas_variants(
        prompt=args.prompt,
        product_name=args.name,
    )
    print(f"✅ Parallel canvas generated successfully at: {out_file}")


def cmd_serve(args):
    start_preview_server(port=args.port, directory=args.dir, open_browser=not args.no_browser)


def main():
    parser = argparse.ArgumentParser(description="SuperDesign Agent - Generate Sites, Slides & Product UI without paid credits.")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Site
    p_site = subparsers.add_parser("site", help="Generate a responsive website / landing page")
    p_site.add_argument("--title", default="NexusAI", help="Site title")
    p_site.add_argument("--tagline", default="Autonomous Cognitive Platform", help="Tagline badge")
    p_site.add_argument("--prompt", default="", help="Description or prompt")
    p_site.add_argument("--theme", default="modern_saas", choices=["modern_saas", "apple_minimal", "cyberpunk_neon", "neo_brutalist", "clean_editorial"])
    p_site.add_argument("--out-dir", default="./output", help="Output directory")
    p_site.add_argument("--file", default=None, help="Custom filename")

    # Slide
    p_slide = subparsers.add_parser("slide", help="Generate an interactive 16:9 presentation slide deck")
    p_slide.add_argument("--title", default="Product Vision 2026", help="Deck title")
    p_slide.add_argument("--presenter", default="Chief Architect", help="Presenter name")
    p_slide.add_argument("--slides-count", type=int, default=5, help="Number of slides")
    p_slide.add_argument("--theme", default="apple_minimal", choices=["modern_saas", "apple_minimal", "cyberpunk_neon", "neo_brutalist", "clean_editorial"])
    p_slide.add_argument("--out-dir", default="./output", help="Output directory")
    p_slide.add_argument("--file", default=None, help="Custom filename")

    # Product
    p_prod = subparsers.add_parser("product", help="Generate a product dashboard / analytics UI")
    p_prod.add_argument("--name", default="SuperDesign Ops", help="Product name")
    p_prod.add_argument("--theme", default="modern_saas", help="Theme style")
    p_prod.add_argument("--out-dir", default="./output", help="Output directory")
    p_prod.add_argument("--file", default=None, help="Custom filename")

    # Explore
    p_exp = subparsers.add_parser("explore", help="Generate 4-style parallel exploration canvas")
    p_exp.add_argument("--prompt", required=True, help="Prompt description")
    p_exp.add_argument("--name", default="SuperAgent", help="Product name")
    p_exp.add_argument("--out-dir", default="./output", help="Output directory")

    # Serve
    p_serve = subparsers.add_parser("serve", help="Start local live preview canvas server")
    p_serve.add_argument("--port", type=int, default=8080, help="Port")
    p_serve.add_argument("--dir", default="./output", help="Directory to serve")
    p_serve.add_argument("--no-browser", action="store_true", help="Do not auto-open browser")

    args = parser.parse_args()
    if args.command == "site":
        cmd_site(args)
    elif args.command == "slide":
        cmd_slide(args)
    elif args.command == "product":
        cmd_product(args)
    elif args.command == "explore":
        cmd_explore(args)
    elif args.command == "serve":
        cmd_serve(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
