"""
Anti-Slop SuperDesign CLI.
Full Parity with superdesign.dev skills without paid credits:
- `init`: Scans repository and builds UI context (.superdesign/init/)
- `export-react`: Converts HTML into modular React TSX components
- `audit`: Rigorous Anti-AI-Slop design quality linter
- `purify`: Auto-removes slop patterns from code
- `site`, `slide`, `product`, `explore`, `serve`
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from core.design_engine import SuperDesignEngine
from core.taste_matrix import TasteMatrix
from core.anti_slop_linter import AntiSlopAuditor
from core.repo_scanner import RepoScanner
from core.react_exporter import ReactExporter
from preview_server.server import start_preview_server


def cmd_init(args):
    print("Scanning repository for UI context and design DNA...")
    results = RepoScanner.scan_repository(root_dir=args.dir, output_dir=args.out_dir)
    print("Repository context initialized in: " + args.out_dir)
    print("  - Theme DNA: " + results["theme"])
    print("  - Components: " + results["components"])
    print("  - Routes: " + results["routes"])


def cmd_export_react(args):
    print("Converting HTML to React TSX component: " + args.name)
    if not os.path.exists(args.file):
        print("File not found: " + args.file)
        return
    with open(args.file, "r", encoding="utf-8") as f:
        html = f.read()
    
    tsx = ReactExporter.html_to_react_tsx(args.name, html)
    out_file = args.out or ("./output/" + args.name + ".tsx")
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(tsx)
    print("Exported React TSX component to: " + out_file)


def cmd_audit(args):
    print("Running Anti-AI-Slop Audit on: " + args.file)
    if not os.path.exists(args.file):
        print("File not found: " + args.file)
        return
    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()
    
    report = AntiSlopAuditor.audit_html(content)
    print("=" * 50)
    print("ANTI-SLOP TASTE GRADE: " + report.taste_grade)
    print("SLOP SCORE: " + str(report.slop_score) + " (0.0 = Pure Human Taste, 1.0 = Pure Slop)")
    print("=" * 50)
    if report.violations:
        print("Detected " + str(len(report.violations)) + " Slop Anti-Patterns:")
        for v in report.violations:
            print("- [" + v.severity + "] " + v.pattern_name + ": " + v.description)
            print("  Remedy: " + v.remedy)
    else:
        print("100% SLOP FREE! Uncompromising typography, contrast, and layout verified.")


def cmd_purify(args):
    print("Auto-purifying slop from: " + args.file)
    if not os.path.exists(args.file):
        print("File not found: " + args.file)
        return
    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()
    
    purified = AntiSlopAuditor.auto_purify_html(content)
    out_file = args.out or args.file
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(purified)
    print("Purified design saved to: " + out_file)


def cmd_site(args):
    engine = SuperDesignEngine(output_dir=args.out_dir)
    print("Generating Anti-Slop Architectural Site: " + args.title + " with archetype " + args.theme)
    features = [
        {"title": "Swiss Grid Asymmetry", "desc": "International Typographic Style with strict bounding rules.", "tag": "ARCH_01"},
        {"title": "Zero Paid Credit Tax", "desc": "100% self-contained deterministic local generation forever.", "tag": "COST_02"},
        {"title": "Tactile Noise & Depth", "desc": "Physical texture overlays, dot matrices, and hairline borders.", "tag": "PHYS_03"},
    ]
    out_file = engine.create_site(
        title=args.title,
        tagline=args.tagline or "ANTI-SLOP ARCHITECTURE",
        description=args.prompt or "Deterministic cognitive agent workstation. Engineered with uncompromising human taste.",
        features=features,
        theme_style=args.theme,
        filename=args.file,
    )
    print("Website generated successfully at: " + out_file)


def cmd_slide(args):
    engine = SuperDesignEngine(output_dir=args.out_dir)
    print("Generating Anti-Slop Keynote Deck: " + args.title)
    
    slides_data = [
        {"type": "title", "title": args.title, "subtitle": "ANTI-AI-SLOP MANIFESTO"},
        {
            "type": "content",
            "title": "The Epidemic of AI Slop",
            "subtitle": "GENERIC AI TROPES",
            "content": [
                {"title": "Purple Gradient Blobs", "desc": "The lazy default of every 2023 Dribbble clone."},
                {"title": "Default Inter Everywhere", "desc": "Zero personality, zero editorial weight, statistical average."},
                {"title": "Hollow Buzzword Pitch", "desc": "Endless supercharge and empower filler text."},
            ]
        },
        {
            "type": "metric",
            "title": "The Anti-Slop Benchmark",
            "metric": {"value": "0%", "label": "Zero generic AI slop. 100% bespoke typographic soul."}
        },
        {
            "type": "content",
            "title": "The Four Architectural Pillars",
            "subtitle": "HUMAN TASTE MATRIX",
            "content": [
                {"title": "1. Swiss International", "desc": "Syne + Space Grotesk, asymmetric Bauhaus grids."},
                {"title": "2. Industrial Teenage HUD", "desc": "Chivo Mono, phosphor amber, tactile dot matrices."},
                {"title": "3. Haute Editorial", "desc": "Playfair Display, museum canvas, drop caps."},
            ]
        },
        {
            "type": "quote",
            "quote": {
                "text": "Simplicity is about subtracting the obvious and adding the meaningful.",
                "author": "John Maeda / Steve Jobs"
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
    print("Keynote Deck generated successfully at: " + out_file)


def cmd_product(args):
    engine = SuperDesignEngine(output_dir=args.out_dir)
    print("Generating Industrial Telemetry HUD: " + args.name)
    out_file = engine.create_product_dashboard(
        app_name=args.name,
        theme_style=args.theme,
        filename=args.file,
    )
    print("Telemetry HUD generated successfully at: " + out_file)


def cmd_explore(args):
    engine = SuperDesignEngine(output_dir=args.out_dir)
    print("Generating 4-Archetype Anti-Slop Comparison Canvas for: " + args.prompt)
    out_file = engine.generate_infinite_canvas_variants(
        prompt=args.prompt,
        product_name=args.name,
    )
    print("Comparison canvas generated successfully at: " + out_file)


def cmd_serve(args):
    start_preview_server(port=args.port, directory=args.dir, open_browser=not args.no_browser)


def main():
    parser = argparse.ArgumentParser(description="SuperDesign Anti-AI-Slop CLI - Generate Bespoke Sites, Slides & Telemetry HUDs.")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Init (Parity with superdesign init)
    p_init = subparsers.add_parser("init", help="Analyze codebase & create .superdesign/init context files")
    p_init.add_argument("--dir", default=".", help="Root directory to scan")
    p_init.add_argument("--out-dir", default=".superdesign/init", help="Target context directory")

    # Export React
    p_react = subparsers.add_parser("export-react", help="Export HTML design to React TSX component")
    p_react.add_argument("--file", required=True, help="Input HTML file")
    p_react.add_argument("--name", default="BespokeComponent", help="React component name")
    p_react.add_argument("--out", default=None, help="Target output TSX file path")

    # Audit
    p_audit = subparsers.add_parser("audit", help="Audit HTML file for AI Slop anti-patterns")
    p_audit.add_argument("--file", required=True, help="Path to HTML file to audit")

    # Purify
    p_purify = subparsers.add_parser("purify", help="Auto-purify AI slop from HTML file")
    p_purify.add_argument("--file", required=True, help="Path to HTML file")
    p_purify.add_argument("--out", default=None, help="Target output file")

    # Site
    p_site = subparsers.add_parser("site", help="Generate an Anti-Slop architectural website")
    p_site.add_argument("--title", default="NexusArch", help="Site title")
    p_site.add_argument("--tagline", default="SWISS ARCHITECTURE", help="Tagline badge")
    p_site.add_argument("--prompt", default="", help="Description or prompt")
    p_site.add_argument("--theme", default="swiss_international", choices=["swiss_international", "industrial_hud", "haute_editorial", "neo_cybernetic"])
    p_site.add_argument("--out-dir", default="./output", help="Output directory")
    p_site.add_argument("--file", default=None, help="Custom filename")

    # Slide
    p_slide = subparsers.add_parser("slide", help="Generate an Anti-Slop 16:9 presentation deck")
    p_slide.add_argument("--title", default="Anti-Slop Manifesto", help="Deck title")
    p_slide.add_argument("--presenter", default="Chief Architect", help="Presenter name")
    p_slide.add_argument("--slides-count", type=int, default=5, help="Number of slides")
    p_slide.add_argument("--theme", default="swiss_international", choices=["swiss_international", "industrial_hud", "haute_editorial", "neo_cybernetic"])
    p_slide.add_argument("--out-dir", default="./output", help="Output directory")
    p_slide.add_argument("--file", default=None, help="Custom filename")

    # Product
    p_prod = subparsers.add_parser("product", help="Generate an Industrial Telemetry HUD")
    p_prod.add_argument("--name", default="TelemetryOps", help="Product name")
    p_prod.add_argument("--theme", default="industrial_hud", help="Theme style")
    p_prod.add_argument("--out-dir", default="./output", help="Output directory")
    p_prod.add_argument("--file", default=None, help="Custom filename")

    # Explore
    p_exp = subparsers.add_parser("explore", help="Generate 4-archetype Anti-Slop comparison canvas")
    p_exp.add_argument("--prompt", required=True, help="Prompt description")
    p_exp.add_argument("--name", default="NexusEngine", help="Product name")
    p_exp.add_argument("--out-dir", default="./output", help="Output directory")

    # Serve
    p_serve = subparsers.add_parser("serve", help="Start local live preview canvas server")
    p_serve.add_argument("--port", type=int, default=8080, help="Port")
    p_serve.add_argument("--dir", default="./output", help="Directory to serve")
    p_serve.add_argument("--no-browser", action="store_true", help="Do not auto-open browser")

    args = parser.parse_args()
    if args.command == "init":
        cmd_init(args)
    elif args.command == "export-react":
        cmd_export_react(args)
    elif args.command == "audit":
        cmd_audit(args)
    elif args.command == "purify":
        cmd_purify(args)
    elif args.command == "site":
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
