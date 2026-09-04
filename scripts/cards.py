#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from xml.sax.saxutils import escape

def card(project, dark=True):
    bg="#0d1117" if dark else "#ffffff"
    fg="#e6edf3" if dark else "#24292f"
    muted="#8b949e" if dark else "#57606a"
    border="#30363d" if dark else "#d0d7de"
    title=escape(project["name"])
    desc=escape(project["description"][:105])
    tags=escape("  ".join("["+x+"]" for x in project.get("stack",[])))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="190">
<rect x="1" y="1" width="758" height="188" rx="14" fill="{bg}" stroke="{border}"/>
<text x="28" y="48" fill="{fg}" font-family="Segoe UI,Arial" font-size="24" font-weight="700">{title}</text>
<text x="28" y="88" fill="{muted}" font-family="Segoe UI,Arial" font-size="16">{desc}</text>
<text x="28" y="124" fill="{muted}" font-family="Consolas,monospace" font-size="14">{tags}</text>
<text x="28" y="160" fill="#39d353" font-family="Consolas,monospace" font-size="13">AIMaestrotheaum · project</text>
</svg>'''

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--user",required=True); p.add_argument("--out",default="assets")
    a=p.parse_args(); out=Path(a.out)
    projects=json.loads((out/"projects.json").read_text())
    for i,project in enumerate(projects,1):
        for theme in ("dark","light"):
            (out/f"card-project-{i}-{theme}.svg").write_text(card(project,theme=="dark"),encoding="utf-8")
