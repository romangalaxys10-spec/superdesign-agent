"""Example: Generate a complete SaaS Landing Page"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.design_engine import SuperDesignEngine

engine = SuperDesignEngine(output_dir="./output")
out = engine.create_site(
    title="KryptonFlow",
    tagline="Next-Generation Solana Stream Indexer",
    description="Stream, decode, and trigger autonomous actions from Yellowstone gRPC and on-chain DEX pools in sub-milliseconds.",
    features=[
        {"title": "Sub-millisecond Geyser gRPC", "desc": "Direct slot-level transaction streaming with zero lag.", "icon": "zap"},
        {"title": "Meteora & Raydium Decoders", "desc": "Automatic instruction discriminator and pool migration parsing.", "icon": "layers"},
        {"title": "Self-Healing Fallback Trees", "desc": "Zero dropouts with dual-endpoint redundant failover.", "icon": "shield"},
    ],
    theme_style="cyberpunk_neon",
    filename="kryptonflow_landing.html"
)
print(f"Generated Landing Page: {out}")
