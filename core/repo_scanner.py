"""
Repository UI Context Analyzer (Parity with superdesign init).
Scans codebases for existing design tokens, components, routes, and styles, saving context to .superdesign/init/.
"""

import os
import re
import json
from typing import Dict, List, Any


class RepoScanner:
    """Scans and extracts design DNA from local codebases."""

    @classmethod
    def scan_repository(cls, root_dir: str = ".", output_dir: str = ".superdesign/init") -> Dict[str, str]:
        os.makedirs(output_dir, exist_ok=True)
        
        components = []
        routes = []
        colors_found = set()
        fonts_found = set()
        
        ignore_dirs = {".git", "node_modules", ".next", "dist", "build", ".venv", "__pycache__", ".pytest_cache"}

        for root, dirs, files in os.walk(root_dir):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                rel_path = os.path.relpath(os.path.join(root, file), root_dir)
                
                # Check for components
                if ext in {".tsx", ".jsx", ".vue", ".svelte"}:
                    components.append(rel_path)
                
                # Check for routes (Next.js / App router)
                if "page." in file or "route." in file or "index.html" in file:
                    routes.append(rel_path)
                
                # Extract colors and fonts from css/tailwind
                if ext in {".css", ".scss", ".ts", ".js", ".json", ".html"}:
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                            # Find hex colors
                            hexes = re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", content)
                            for h in hexes:
                                colors_found.add(h.upper())
                            # Find font families
                            fonts = re.findall(r"font-family:\s*([^;]+);", content)
                            for fn in fonts:
                                fonts_found.add(fn.strip())
                    except Exception:
                        pass

        # 1. Generate theme.md
        theme_md = f"""# Design System & Theme Context
*Extracted automatically by SuperDesign Agent*

## Colors Detected ({len(colors_found)})
{chr(10).join(f"- `{c}`" for c in sorted(list(colors_found))[:20]) if colors_found else "- Standard High-Contrast Monochrome (#000000, #FFFFFF, #FF3B00)"}

## Typography Detected
{chr(10).join(f"- `{fn}`" for fn in sorted(list(fonts_found))[:10]) if fonts_found else "- Anti-Slop Recommended: Syne + Space Grotesk / Chivo Mono"}

## Design System Guidelines
- Architecture: Zero-Slop Swiss Asymmetric Grids & Tactile Depth.
- Framework: Tailwind CSS + React / Modern HTML.
"""
        theme_file = os.path.join(output_dir, "theme.md")
        with open(theme_file, "w", encoding="utf-8") as f:
            f.write(theme_md)

        # 2. Generate components.md
        comp_md = f"""# Component Catalog ({len(components)})
*Existing UI Components in Workspace*

{chr(10).join(f"- `{c}`" for c in sorted(components)[:50]) if components else "- No legacy components found. Ready to scaffold from scratch."}
"""
        comp_file = os.path.join(output_dir, "components.md")
        with open(comp_file, "w", encoding="utf-8") as f:
            f.write(comp_md)

        # 3. Generate routes.md
        routes_md = f"""# Application Routes ({len(routes)})
*Detected Pages & Views*

{chr(10).join(f"- `{r}`" for r in sorted(routes)[:30]) if routes else "- Root View: `index.html` / `app/page.tsx`"}
"""
        routes_file = os.path.join(output_dir, "routes.md")
        with open(routes_file, "w", encoding="utf-8") as f:
            f.write(routes_md)

        return {
            "theme": theme_file,
            "components": comp_file,
            "routes": routes_file,
        }
