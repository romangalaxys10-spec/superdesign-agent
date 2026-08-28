"""
Anti-AI-Slop Linter & Taste Engine.
Audits HTML, CSS, and UI components for generic AI tropes, computes a Slop Score, and auto-purifies designs.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple
import re


@dataclass
class SlopViolation:
    rule_id: str
    severity: str  # CRITICAL, WARNING, INFO
    pattern_name: str
    description: str
    remedy: str


@dataclass
class AuditReport:
    slop_score: float  # 0.0 (Pure Bespoke Taste) to 1.0 (Pure AI Slop)
    is_slop_free: bool
    violations: List[SlopViolation]
    taste_grade: str  # A+ (Masterpiece), B (Passable), F (Generic Slop)
    recommendations: List[str]


class AntiSlopAuditor:
    """Rigorous taste auditor for modern web design."""

    SLOP_PATTERNS = [
        (
            "SLOP_PURPLE_GRADIENT_BLOB",
            "CRITICAL",
            r"(from-indigo-500.*to-pink-500|from-purple-500.*to-indigo-500|from-violet-500.*to-fuchsia-500)",
            "Generic 2023 Dribbble purple-to-pink gradient blob detected. This is the #1 marker of AI-generated slop.",
            "Replace with intentional single-hue contrast, high-contrast Vermillion (#FF3B00), Phosphor Amber (#FFB000), or pure monochrome line art."
        ),
        (
            "SLOP_DEFAULT_INTER_FONT",
            "WARNING",
            r"font-sans(?!\s+(tracking-tighter|antialiased\s+font-serif))",
            "Unspecified generic system/Inter sans-serif typography detected without bespoke editorial hierarchy.",
            "Pair high-character display fonts (Syne, Clash Display, Playfair Display) with technical body fonts (Space Grotesk, JetBrains Mono)."
        ),
        (
            "SLOP_BUZZWORD_CLICHE",
            "CRITICAL",
            r"(?i)\b(supercharge|revolutionize|unleash|empower|streamline|game-changing|next-gen|seamlessly|frictionless|synergistic)\b",
            "Trite, hollow marketing buzzwords detected.",
            "Replace with concrete, high-information technical statements and quantifiable metrics."
        ),
        (
            "SLOP_BLAND_3_CARD_GRID",
            "WARNING",
            r"grid-cols-1\s+md:grid-cols-3\s+gap-8.*rounded-2xl.*rounded-2xl.*rounded-2xl",
            "Predictable, cookie-cutter 3-card grid layout with identical rounded corners.",
            "Use asymmetric Swiss grids, oversized hero callouts, hairline border rules, or horizontal timeline flows."
        ),
        (
            "SLOP_STERILE_DARK_MODE",
            "INFO",
            r"bg-slate-900.*bg-slate-800",
            "Generic sterile slate dark mode with zero tactile grain or depth.",
            "Inject SVG noise textures, industrial dot-matrix grids, or pitch void (#060709) with high-contrast hairline borders."
        ),
    ]

    @classmethod
    def audit_html(cls, html_content: str) -> AuditReport:
        violations = []
        slop_penalty = 0.0

        for rule_id, severity, regex, desc, remedy in cls.SLOP_PATTERNS:
            if re.search(regex, html_content):
                violations.append(SlopViolation(
                    rule_id=rule_id,
                    severity=severity,
                    pattern_name=rule_id.replace("SLOP_", "").title().replace("_", " "),
                    description=desc,
                    remedy=remedy,
                ))
                if severity == "CRITICAL":
                    slop_penalty += 0.35
                elif severity == "WARNING":
                    slop_penalty += 0.20
                else:
                    slop_penalty += 0.10

        slop_score = min(1.0, round(slop_penalty, 2))
        is_clean = slop_score <= 0.15
        
        if slop_score <= 0.10:
            grade = "A+ (Bespoke Human Taste)"
        elif slop_score <= 0.35:
            grade = "B (Minor Slop Elements)"
        elif slop_score <= 0.60:
            grade = "C (Noticeable AI Clichés)"
        else:
            grade = "F (Pure Generic AI Slop)"

        recs = [v.remedy for v in violations]
        return AuditReport(
            slop_score=slop_score,
            is_slop_free=is_clean,
            violations=violations,
            taste_grade=grade,
            recommendations=recs,
        )

    @classmethod
    def auto_purify_html(cls, html_content: str) -> str:
        """Purges common slop patterns and injects tactile noise and bespoke typography."""
        replacements = {
            r"(?i)\bsupercharge your workflow\b": "Accelerate engineering throughput",
            r"(?i)\bunleash the power of ai\b": "Deterministic cognitive execution",
            r"(?i)\bseamlessly integrate\b": "Direct API and RPC integration",
            r"(?i)\bnext-gen\b": "High-throughput",
            r"(?i)\bgame-changing\b": "Verified",
        }
        purified = html_content
        for pattern, repl in replacements.items():
            purified = re.sub(pattern, repl, purified)

        if "noiseFilter" not in purified:
            svg_noise = '<svg class="pointer-events-none fixed inset-0 z-50 h-full w-full opacity-[0.035]" xmlns="http://www.w3.org/2000/svg"><filter id="noiseFilter"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#noiseFilter)"/></svg>'
            purified = purified.replace("</body>", svg_noise + chr(10) + "</body>")

        return purified
