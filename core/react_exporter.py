"""
React / Next.js Component Exporter.
Converts generated HTML/Tailwind elements into clean, modular React TSX components with Lucide React icons.
"""

import re


class ReactExporter:
    """Exports raw HTML into production-ready React TSX components."""

    @classmethod
    def html_to_react_tsx(cls, component_name: str, html_snippet: str) -> str:
        # Convert class to className
        jsx = re.sub(r'class="([^"]*)"', r'className=""', html_snippet)
        
        # Convert inline styles if any (style="...")
        jsx = re.sub(r'style="([^"]*)"', r'/* style="" */', jsx)
        
        # Convert Lucide data-lucide icons to React Lucide components
        jsx = re.sub(r'<i\s+data-lucide="([^"]+)"\s+className="([^"]+)"></i>', r'<LucideIcon name="" className="" />', jsx)
        
        return f"""import React from 'react';
import * as Icons from 'lucide-react';

interface {component_name}Props {{
  className?: string;
}}

const LucideIcon = ({{ name, className }}: {{ name: string; className?: string }}) => {{
  const formattedName = name.split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('');
  const IconComponent = (Icons as any)[formattedName] || Icons.Sparkles;
  return <IconComponent className={{className}} />;
}};

export const {component_name}: React.FC<{component_name}Props> = ({{ className = "" }}) => {{
  return (
    <div className={{`w-full ${{className}}`}}>
      {jsx}
    </div>
  );
}};

export default {component_name};
"""
