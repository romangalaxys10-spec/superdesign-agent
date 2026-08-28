"""
Theme Matrix & Design System Generator.
Contains color palettes, typography, glassmorphism, shadows, and styling rules.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any


class ThemeStyle(str, Enum):
    MODERN_SAAS = "modern_saas"
    APPLE_MINIMAL = "apple_minimal"
    CYBERPUNK_NEON = "cyberpunk_neon"
    NEO_BRUTALIST = "neo_brutalist"
    CLEAN_EDITORIAL = "clean_editorial"


@dataclass
class DesignTheme:
    name: str
    key: str
    body_bg: str
    text_primary: str
    text_secondary: str
    card_bg: str
    card_border: str
    accent_gradient: str
    button_primary: str
    button_secondary: str
    font_family: str
    shadow_style: str
    badge_style: str
    glow_effect: str


class ThemeMatrix:
    """Pre-engineered design tokens and aesthetic engines."""

    THEMES: Dict[str, DesignTheme] = {
        ThemeStyle.MODERN_SAAS: DesignTheme(
            name="Modern SaaS Dark",
            key=ThemeStyle.MODERN_SAAS.value,
            body_bg="bg-[#0a0d14] text-slate-100",
            text_primary="text-white",
            text_secondary="text-slate-400",
            card_bg="bg-slate-900/60 backdrop-blur-xl",
            card_border="border border-slate-800/80 hover:border-indigo-500/50 transition-all duration-300",
            accent_gradient="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500",
            button_primary="bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-500/25 px-6 py-3 rounded-xl font-medium transition-all duration-200 hover:scale-[1.02] active:scale-[0.98]",
            button_secondary="bg-slate-800/80 hover:bg-slate-700/80 text-slate-200 border border-slate-700 px-6 py-3 rounded-xl font-medium transition-all duration-200",
            font_family="font-sans antialiased",
            shadow_style="shadow-2xl shadow-indigo-950/40",
            badge_style="bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider",
            glow_effect="before:absolute before:-inset-1 before:bg-gradient-to-r before:from-indigo-500 before:to-purple-600 before:rounded-2xl before:blur-xl before:opacity-20 hover:before:opacity-40 before:transition-opacity",
        ),
        ThemeStyle.APPLE_MINIMAL: DesignTheme(
            name="Apple Minimalist",
            key=ThemeStyle.APPLE_MINIMAL.value,
            body_bg="bg-[#000000] text-[#f5f5f7]",
            text_primary="text-[#f5f5f7]",
            text_secondary="text-[#86868b]",
            card_bg="bg-[#161617]/70 backdrop-blur-2xl",
            card_border="border border-[#2d2d2f] hover:border-[#424245] transition-all duration-300",
            accent_gradient="bg-gradient-to-r from-[#2997ff] via-[#9955ff] to-[#ff2d55]",
            button_primary="bg-[#0071e3] hover:bg-[#0077ed] text-white px-6 py-3 rounded-full font-medium transition-all duration-200 hover:scale-[1.02] active:scale-[0.98]",
            button_secondary="bg-[#1d1d1f] hover:bg-[#2d2d2f] text-[#f5f5f7] border border-[#424245] px-6 py-3 rounded-full font-medium transition-all duration-200",
            font_family="font-sans tracking-tight antialiased",
            shadow_style="shadow-2xl shadow-black/80",
            badge_style="bg-[#1d1d1f] text-[#2997ff] border border-[#2d2d2f] px-3 py-1 rounded-full text-xs font-medium",
            glow_effect="",
        ),
        ThemeStyle.CYBERPUNK_NEON: DesignTheme(
            name="Cyberpunk Neon",
            key=ThemeStyle.CYBERPUNK_NEON.value,
            body_bg="bg-[#050508] text-cyan-100",
            text_primary="text-cyan-400",
            text_secondary="text-cyan-200/60",
            card_bg="bg-[#0d0f18]/90 backdrop-blur-md",
            card_border="border border-cyan-500/40 hover:border-pink-500 shadow-[0_0_15px_rgba(6,182,212,0.15)] hover:shadow-[0_0_25px_rgba(236,72,153,0.3)] transition-all duration-300",
            accent_gradient="bg-gradient-to-r from-cyan-400 via-fuchsia-500 to-yellow-400",
            button_primary="bg-cyan-500 hover:bg-cyan-400 text-black font-bold px-6 py-3 rounded-none border border-cyan-300 shadow-[0_0_20px_rgba(6,182,212,0.5)] transition-all duration-200 uppercase tracking-widest",
            button_secondary="bg-transparent hover:bg-pink-500/20 text-pink-400 border border-pink-500 px-6 py-3 rounded-none font-bold transition-all duration-200 uppercase tracking-widest",
            font_family="font-mono antialiased",
            shadow_style="shadow-[0_0_30px_rgba(0,240,255,0.2)]",
            badge_style="bg-cyan-950 text-cyan-400 border border-cyan-500/50 px-3 py-1 text-xs font-mono uppercase tracking-widest",
            glow_effect="shadow-[0_0_30px_rgba(236,72,153,0.4)]",
        ),
        ThemeStyle.NEO_BRUTALIST: DesignTheme(
            name="Neo Brutalist",
            key=ThemeStyle.NEO_BRUTALIST.value,
            body_bg="bg-[#fdf6e2] text-black",
            text_primary="text-black",
            text_secondary="text-neutral-700",
            card_bg="bg-white",
            card_border="border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:shadow-[10px_10px_0px_0px_rgba(0,0,0,1)] transition-all duration-200",
            accent_gradient="bg-gradient-to-r from-yellow-300 via-pink-300 to-cyan-300",
            button_primary="bg-[#FFE600] hover:bg-[#FFD600] text-black border-3 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[-2px] hover:translate-y-[-2px] active:translate-x-[2px] active:translate-y-[2px] px-6 py-3 font-black text-base transition-all duration-100 uppercase tracking-wider",
            button_secondary="bg-white hover:bg-neutral-100 text-black border-3 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] px-6 py-3 font-bold text-base transition-all duration-100",
            font_family="font-sans font-bold antialiased",
            shadow_style="shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]",
            badge_style="bg-[#FF90E8] text-black border-2 border-black px-3 py-1 font-black text-xs uppercase shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]",
            glow_effect="",
        ),
        ThemeStyle.CLEAN_EDITORIAL: DesignTheme(
            name="Clean Editorial",
            key=ThemeStyle.CLEAN_EDITORIAL.value,
            body_bg="bg-[#f9f8f6] text-[#1c1b1a]",
            text_primary="text-[#1c1b1a]",
            text_secondary="text-[#686663]",
            card_bg="bg-white",
            card_border="border border-[#e4e2dd] hover:border-[#1c1b1a] transition-all duration-300",
            accent_gradient="bg-gradient-to-r from-[#1c1b1a] via-[#5c5852] to-[#8a857d]",
            button_primary="bg-[#1c1b1a] hover:bg-[#33302c] text-[#f9f8f6] px-6 py-3 rounded-none font-serif font-medium text-base transition-all duration-200",
            button_secondary="bg-transparent hover:bg-[#eae8e3] text-[#1c1b1a] border border-[#1c1b1a] px-6 py-3 rounded-none font-serif font-medium text-base transition-all duration-200",
            font_family="font-serif antialiased",
            shadow_style="shadow-sm",
            badge_style="bg-[#eeece7] text-[#1c1b1a] border border-[#d5d2cb] px-3 py-1 text-xs font-sans uppercase tracking-widest",
            glow_effect="",
        ),
    }

    @classmethod
    def get_theme(cls, theme_style: str) -> DesignTheme:
        for key, theme in cls.THEMES.items():
            if key == theme_style or theme.key == theme_style or theme_style.lower() in key.value:
                return theme
        return cls.THEMES[ThemeStyle.MODERN_SAAS]
