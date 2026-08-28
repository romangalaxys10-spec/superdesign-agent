import React from 'react';
import * as Icons from 'lucide-react';

interface SwissHeroComponentProps {
  className?: string;
}

const LucideIcon = ({ name, className }: { name: string; className?: string }) => {
  const formattedName = name.split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('');
  const IconComponent = (Icons as any)[formattedName] || Icons.Sparkles;
  return <IconComponent className={className} />;
};

export const SwissHeroComponent: React.FC<SwissHeroComponentProps> = ({ className = "" }) => {
  return (
    <div className={`w-full ${className}`}>
      <!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KryptonFlow — SWISS ARCHITECTURE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Syne:wght@700;800;900&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .grid-matrix {
            background-size: 32px 32px;
            background-image: linear-gradient(to right, rgba(255, 255, 255, 0.04) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
        }
        .dot-matrix {
            background-size: 24px 24px;
            background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
        }
    </style>
</head>
<body class="bg-[#0c0d0e] text-[#f4f4f4] font-['Space_Grotesk',sans-serif] min-h-screen selection:bg-[#FF3B00] selection:text-white relative">
    
    <svg class="pointer-events-none fixed inset-0 z-50 h-full w-full opacity-[0.03]" xmlns="http://www.w3.org/2000/svg">
        <filter id="noiseFilter"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/></filter>
        <rect width="100%" height="100%" filter="url(#noiseFilter)"/>
    </svg>

    <!-- Top Architecture Bar -->
    <header class="border-b border-white/15 px-8 py-5 flex items-center justify-between sticky top-0 z-40 bg-inherit/90 backdrop-blur-md">
        <div class="flex items-center gap-4">
            <span class="text-xl font-black tracking-tighter font-['Syne',sans-serif] text-white uppercase">KryptonFlow</span>
            <span class="bg-white text-black font-black px-3 py-1 text-[11px] uppercase tracking-widest">SWISS ARCHITECTURE</span>
        </div>
        <div class="hidden md:flex items-center gap-8 text-xs uppercase tracking-widest font-bold text-neutral-400">
            <a href="#manifesto" class="hover:text-white transition-colors">Manifesto</a>
            <a href="#architecture" class="hover:text-white transition-colors">Architecture</a>
            <a href="#specs" class="hover:text-white transition-colors">Telemetry</a>
        </div>
        <div>
            <a href="#specs" class="bg-[#FF3B00] hover:bg-[#ff5522] text-white font-bold px-8 py-4 rounded-none uppercase tracking-widest text-xs transition-all duration-150 active:translate-y-0.5">Initiate Protocol</a>
        </div>
    </header>

    <!-- Hero: Asymmetric Editorial Scale -->
    <section class="pt-24 pb-20 px-8 max-w-7xl mx-auto border-b border-white/15">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-end">
            <div class="lg:col-span-8 space-y-6">
                <div class="font-['Space_Grotesk',sans-serif] text-xs uppercase tracking-[0.25em] text-neutral-500 flex items-center gap-2">
                    <span class="inline-block w-2 h-2 bg-[#FF3B00]"></span>
                    <span>ANTI-SLOP ARCHITECTURAL SPECIFICATION 2026</span>
                </div>
                <h1 class="text-5xl sm:text-7xl lg:text-8xl font-black font-['Syne',sans-serif] text-white tracking-tight leading-[0.95] uppercase">
                    Form Follows <br>
                    <span class="text-[#FF3B00]">Precision.</span>
                </h1>
                <p class="text-lg md:text-xl text-neutral-400 max-w-2xl leading-relaxed pt-4">
                    Deterministic cognitive agent workstation. Engineered with uncompromising human taste.
                </p>
            </div>
            <div class="lg:col-span-4 border-t-2 border-[#FF3B00] pt-6 space-y-4">
                <div class="text-xs font-mono uppercase text-neutral-500">SYSTEM MANIFESTO // 01</div>
                <p class="text-sm italic text-white font-serif leading-relaxed">
                    "We reject the sea of identical purple-gradient SaaS clones. Real engineering demands uncompromising typography, tactile depth, asymmetric balance, and structural honesty."
                </p>
                <div class="pt-4 flex gap-4">
                    <a href="#architecture" class="bg-[#FF3B00] hover:bg-[#ff5522] text-white font-bold px-8 py-4 rounded-none uppercase tracking-widest text-xs transition-all duration-150 active:translate-y-0.5 w-full text-center">Deploy Engine</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Metrics Strip -->
    <section class="border-b border-white/15 max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-4">
            
            <div class="p-8 border-b md:border-b-0 md:border-r last:border-r-0 border-white/15">
                <div class="text-5xl lg:text-6xl font-black font-['Syne',sans-serif] text-white mb-2 tracking-tighter">0.04ms</div>
                <div class="font-['Space_Grotesk',sans-serif] text-neutral-400 text-xs uppercase tracking-widest">Mean Deterministic Latency</div>
            </div>
            <div class="p-8 border-b md:border-b-0 md:border-r last:border-r-0 border-white/15">
                <div class="text-5xl lg:text-6xl font-black font-['Syne',sans-serif] text-white mb-2 tracking-tighter">100%</div>
                <div class="font-['Space_Grotesk',sans-serif] text-neutral-400 text-xs uppercase tracking-widest">Self-Contained Local Execution</div>
            </div>
            <div class="p-8 border-b md:border-b-0 md:border-r last:border-r-0 border-white/15">
                <div class="text-5xl lg:text-6xl font-black font-['Syne',sans-serif] text-white mb-2 tracking-tighter">0.00$</div>
                <div class="font-['Space_Grotesk',sans-serif] text-neutral-400 text-xs uppercase tracking-widest">Third-Party API Credit Cost</div>
            </div>
            <div class="p-8 border-b md:border-b-0 md:border-r last:border-r-0 border-white/15">
                <div class="text-5xl lg:text-6xl font-black font-['Syne',sans-serif] text-white mb-2 tracking-tighter">4.98★</div>
                <div class="font-['Space_Grotesk',sans-serif] text-neutral-400 text-xs uppercase tracking-widest">Architectural Taste Index</div>
            </div>
        </div>
    </section>

    <!-- Architectural Modules -->
    <section id="architecture" class="py-24 px-8 max-w-7xl mx-auto border-b border-white/15">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-white/15 gap-6">
            <div>
                <span class="text-xs font-mono text-neutral-500 uppercase tracking-widest">// ARCHITECTURAL TOPOLOGY</span>
                <h2 class="text-4xl md:text-5xl font-black font-['Syne',sans-serif] text-white tracking-tight uppercase mt-2">Engineered Modules</h2>
            </div>
            <p class="text-neutral-400 max-w-md text-xs uppercase tracking-wider leading-relaxed">
                Zero cookie-cutter components. Each module is crafted with strict typography, discrete bounding boxes, and verified telemetry.
            </p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            
            <div class="bg-transparent border-t-2 border-white/20 hover:border-[#FF3B00] transition-colors p-8 rounded-none relative group">
                <div class="flex items-center justify-between mb-6 pb-2 border-b border-white/15">
                    <span class="font-['Space_Grotesk',sans-serif] text-xs uppercase tracking-widest text-neutral-500">ARCH_01</span>
                    <span class="text-xs font-mono text-neutral-400">[ACTIVE]</span>
                </div>
                <h3 class="text-2xl font-bold font-['Syne',sans-serif] text-white mb-3 tracking-tight">Swiss Grid Asymmetry</h3>
                <p class="font-['Space_Grotesk',sans-serif] text-neutral-400 text-sm leading-relaxed">International Typographic Style with strict bounding rules.</p>
            </div>
            <div class="bg-transparent border-t-2 border-white/20 hover:border-[#FF3B00] transition-colors p-8 rounded-none relative group">
                <div class="flex items-center justify-between mb-6 pb-2 border-b border-white/15">
                    <span class="font-['Space_Grotesk',sans-serif] text-xs uppercase tracking-widest text-neutral-500">COST_02</span>
                    <span class="text-xs font-mono text-neutral-400">[ACTIVE]</span>
                </div>
                <h3 class="text-2xl font-bold font-['Syne',sans-serif] text-white mb-3 tracking-tight">Zero Paid Credit Tax</h3>
                <p class="font-['Space_Grotesk',sans-serif] text-neutral-400 text-sm leading-relaxed">100% self-contained deterministic local generation forever.</p>
            </div>
            <div class="bg-transparent border-t-2 border-white/20 hover:border-[#FF3B00] transition-colors p-8 rounded-none relative group">
                <div class="flex items-center justify-between mb-6 pb-2 border-b border-white/15">
                    <span class="font-['Space_Grotesk',sans-serif] text-xs uppercase tracking-widest text-neutral-500">PHYS_03</span>
                    <span class="text-xs font-mono text-neutral-400">[ACTIVE]</span>
                </div>
                <h3 class="text-2xl font-bold font-['Syne',sans-serif] text-white mb-3 tracking-tight">Tactile Noise & Depth</h3>
                <p class="font-['Space_Grotesk',sans-serif] text-neutral-400 text-sm leading-relaxed">Physical texture overlays, dot matrices, and hairline borders.</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 px-8 max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-6 text-xs uppercase tracking-widest text-neutral-400">
        <div>
            <span class="font-bold text-white">KryptonFlow</span> — Built with Anti-Slop Standards.
        </div>
        <div class="flex gap-8 font-mono">
            <span>[NO PURPLE BLOBS]</span>
            <span>[NO GENERIC INTER]</span>
            <span>[NO PAYWALLS]</span>
        </div>
    </footer>

    <script>lucide.createIcons();</script>
</body>
</html>
    </div>
  );
};

export default SwissHeroComponent;
