"""
SuperDesign Agent - Anti-AI-Slop Architecture
"""
from .taste_matrix import TasteMatrix, TasteArchetype, AntiSlopTheme
from .anti_slop_linter import AntiSlopAuditor, SlopViolation, AuditReport
from .site_generator import SiteGenerator
from .slide_generator import SlideGenerator
from .product_ui_generator import ProductUIGenerator
from .design_engine import SuperDesignEngine

__all__ = [
    "TasteMatrix",
    "TasteArchetype",
    "AntiSlopTheme",
    "AntiSlopAuditor",
    "SlopViolation",
    "AuditReport",
    "SiteGenerator",
    "SlideGenerator",
    "ProductUIGenerator",
    "SuperDesignEngine",
]
