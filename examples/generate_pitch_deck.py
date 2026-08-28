"""Example: Generate a 16:9 Keynote Pitch Deck"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.design_engine import SuperDesignEngine

slides = [
    {"type": "title", "title": "SuperDesign Agent", "subtitle": "Democratizing Autonomous UI & Presentation Engineering"},
    {
        "type": "content",
        "title": "The Broken Status Quo",
        "subtitle": "Why Traditional AI Design Tools Fail",
        "content": [
            {"title": "Predatory Credit Systems", "desc": "Developers run out of monthly credits in 15 minutes.", "icon": "ban"},
            {"title": "Disconnected Output", "desc": "Static images that take hours to convert to real code.", "icon": "image-off"},
            {"title": "Style Inconsistency", "desc": "Every prompt generates a completely random disjointed aesthetic.", "icon": "shuffle"},
        ]
    },
    {
        "type": "metric",
        "title": "The SuperDesign Advantage",
        "metric": {"value": "0$", "label": "Zero paid credits. 100% deterministic local generation forever."}
    },
    {
        "type": "content",
        "title": "Four Distinct Aesthetic Dimensions",
        "subtitle": "Unified Design System Matrix",
        "content": [
            {"title": "Apple Minimal", "desc": "Pure black, SF typography, understated luxury.", "icon": "sparkles"},
            {"title": "Modern SaaS", "desc": "Indigo glow, glassmorphism, crisp telemetry.", "icon": "monitor"},
            {"title": "Neo-Brutalist", "desc": "Bold 4px borders, hard shadows, vibrant accents.", "icon": "box"},
        ]
    },
    {
        "type": "quote",
        "quote": {
            "text": "Simplicity is the ultimate sophistication.",
            "author": "Leonardo da Vinci / Steve Jobs"
        }
    }
]

out = SuperDesignEngine.create_slide_deck(
    deck_title="SuperDesign Vision",
    presenter="Chief AI Architect",
    slides=slides,
    theme_style="apple_minimal",
    output_dir="./output",
    filename="superdesign_pitch_deck.html"
)
print(f"Generated Pitch Deck: {out}")
