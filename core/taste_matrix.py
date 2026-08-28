"""
Anti-Slop Taste Matrix & Design Systems.
4 Radical Archetypes:
1. Swiss International (Bauhaus Grid, High-Contrast Asymmetry, Bold Vermillion)
2. Industrial Teenage HUD (Tactile hardware, dot matrix, phosphor amber, physical switches)
3. Haute Editorial (Vogue/Kinfolk luxury typography, museum canvas, drop caps, delicate hairlines)
4. Neo-Cybernetic Brutalism (Wipeout wireframes, acid lime, glitch magenta, dense telemetry)
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any


class TasteArchetype(str, Enum):
    SWISS_INTERNATIONAL = "swiss_international"
    INDUSTRIAL_HUD = "industrial_hud"
    HAUTE_EDITORIAL = "haute_editorial"
    NEO_CYBERNETIC = "neo_cybernetic"


@dataclass
class AntiSlopTheme:
    name: str
    key: str
    font_import_url: str
    font_family_display: str
    font_family_body: str
    bg_style: str
    text_primary: str
    text_secondary: str
    accent_color: str
    card_style: str
    button_primary: str
    button_secondary: str
    badge_style: str
    border_rule: str
    texture_overlay: str


class TasteMatrix:
    """Curated anti-slop aesthetic configurations with zero generic defaults."""

    THEMES: Dict[str, AntiSlopTheme] = {
        TasteArchetype.SWISS_INTERNATIONAL: AntiSlopTheme(
            name="Swiss International / Bauhaus Grid",
            key=TasteArchetype.SWISS_INTERNATIONAL.value,
            font_import_url="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Syne:wght@700;800;900&display=swap",
            font_family_display="font-['Syne',sans-serif]",
            font_family_body="font-['Space_Grotesk',sans-serif]",
            bg_style="bg-[#0c0d0e] text-[#f4f4f4]",
            text_primary="text-white",
            text_secondary="text-neutral-400",
            accent_color="#FF3B00",
            card_style="bg-transparent border-t-2 border-white/20 hover:border-[#FF3B00] transition-colors p-8 rounded-none",
            button_primary="bg-[#FF3B00] hover:bg-[#ff5522] text-white font-bold px-8 py-4 rounded-none uppercase tracking-widest text-xs transition-all duration-150 active:translate-y-0.5",
            button_secondary="bg-transparent hover:bg-white/10 text-white border-2 border-white px-8 py-4 rounded-none font-bold uppercase tracking-widest text-xs transition-all",
            badge_style="bg-white text-black font-black px-3 py-1 text-[11px] uppercase tracking-widest",
            border_rule="border-white/15",
            texture_overlay="grid-bg",
        ),
        TasteArchetype.INDUSTRIAL_HUD: AntiSlopTheme(
            name="Industrial Teenage HUD / Hardware Synth",
            key=TasteArchetype.INDUSTRIAL_HUD.value,
            font_import_url="https://fonts.googleapis.com/css2?family=Chivo+Mono:wght@400;600;700;900&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap",
            font_family_display="font-['Chivo_Mono',monospace]",
            font_family_body="font-['Plus_Jakarta_Sans',sans-serif]",
            bg_style="bg-[#121316] text-[#e1e4ea]",
            text_primary="text-[#e1e4ea]",
            text_secondary="text-[#7e8494]",
            accent_color="#FFB000",
            card_style="bg-[#1a1c22] border border-[#2b2f3a] p-6 rounded-lg shadow-inner shadow-black/40",
            button_primary="bg-[#FFB000] hover:bg-[#ffa000] text-black font-['Chivo_Mono',monospace] font-bold px-6 py-3 rounded-md uppercase tracking-wider text-xs shadow-[inset_0_1px_0_rgba(255,255,255,0.4),0_2px_4px_rgba(0,0,0,0.5)] active:translate-y-0.5",
            button_secondary="bg-[#242731] hover:bg-[#2d313e] text-[#e1e4ea] border border-[#373c4b] px-6 py-3 rounded-md font-['Chivo_Mono',monospace] text-xs uppercase tracking-wider",
            badge_style="bg-[#2a1d00] text-[#FFB000] border border-[#FFB000]/40 font-mono px-2.5 py-0.5 rounded text-[10px] tracking-wider uppercase",
            border_rule="border-[#2b2f3a]",
            texture_overlay="dot-matrix",
        ),
        TasteArchetype.HAUTE_EDITORIAL: AntiSlopTheme(
            name="Haute Editorial / Luxury Bookcraft",
            key=TasteArchetype.HAUTE_EDITORIAL.value,
            font_import_url="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Playfair+Display:ital,wght@0,600;0,800;1,400;1,600&display=swap",
            font_family_display="font-['Playfair_Display',serif]",
            font_family_body="font-['Instrument_Sans',sans-serif]",
            bg_style="bg-[#F7F5F0] text-[#141311]",
            text_primary="text-[#141311]",
            text_secondary="text-[#696560]",
            accent_color="#141311",
            card_style="bg-white/80 border-t border-b border-[#141311]/15 p-8 rounded-none shadow-sm",
            button_primary="bg-[#141311] hover:bg-[#2d2b27] text-[#F7F5F0] font-serif px-8 py-4 rounded-none text-sm tracking-wide transition-all duration-200",
            button_secondary="bg-transparent hover:bg-[#141311]/5 text-[#141311] border border-[#141311] px-8 py-4 rounded-none font-serif text-sm tracking-wide",
            badge_style="bg-transparent text-[#141311] border-b border-[#141311] pb-0.5 text-xs font-serif italic tracking-widest",
            border_rule="border-[#141311]/15",
            texture_overlay="paper-grain",
        ),
        TasteArchetype.NEO_CYBERNETIC: AntiSlopTheme(
            name="Neo-Cybernetic Wipeout",
            key=TasteArchetype.NEO_CYBERNETIC.value,
            font_import_url="https://fonts.googleapis.com/css2?family=Clash+Display:wght@600;700&family=JetBrains+Mono:wght@400;700;800&display=swap",
            font_family_display="font-['Clash_Display',sans-serif]",
            font_family_body="font-['JetBrains_Mono',monospace]",
            bg_style="bg-[#050608] text-[#e0f8ff]",
            text_primary="text-white",
            text_secondary="text-[#64748b]",
            accent_color="#CCFF00",
            card_style="bg-[#0a0c10] border-l-2 border-[#CCFF00] p-6 rounded-none relative overflow-hidden",
            button_primary="bg-[#CCFF00] hover:bg-[#b8e600] text-black font-mono font-black px-7 py-3.5 rounded-none uppercase text-xs tracking-widest shadow-[3px_3px_0px_0px_#00E5FF] hover:translate-x-[-1px] hover:translate-y-[-1px]",
            button_secondary="bg-transparent hover:bg-white/5 text-[#CCFF00] border border-[#CCFF00] px-7 py-3.5 rounded-none font-mono text-xs uppercase tracking-widest",
            badge_style="bg-[#CCFF00]/10 text-[#CCFF00] border border-[#CCFF00]/40 font-mono px-2 py-0.5 text-[10px] tracking-widest uppercase",
            border_rule="border-slate-800",
            texture_overlay="isometric-grid",
        ),
    }

    @classmethod
    def get_theme(cls, key: str) -> AntiSlopTheme:
        for k, theme in cls.THEMES.items():
            if k == key or theme.key == key or key.lower() in k.value:
                return theme
        return cls.THEMES[TasteArchetype.SWISS_INTERNATIONAL]
