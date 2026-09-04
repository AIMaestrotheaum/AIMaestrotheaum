#!/usr/bin/env python3
import argparse,json,math
from pathlib import Path
def render(data,title,dark):
    bg="#0d1117" if dark else "#fff"; fg="#e6edf3" if dark else "#24292f"; grid="#30363d" if dark else "#d0d7de"
    n=len(data); cx=300; cy=260; R=180
    pts=[]
    for i,(k,v) in enumerate(data.items()):
        a=-math.pi/2+i*2*math.pi/n; r=R*float(v)/100
        pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="540"><rect width="100%" height="100%" fill="{bg}"/>',
         f'<text x="300" y="34" text-anchor="middle" fill="{fg}" font-family="Segoe UI,Arial" font-size="20" font-weight="700">{title}</text>']
    for level in (20,40,60,80,100):
        p=[]
        for i in range(n):
            a=-math.pi/2+i*2*math.pi/n; r=R*level/100
            p.append(f"{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f}")
        svg.append(f'<polygon points="{" ".join(p)}" fill="none" stroke="{grid}"/>')
    svg.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="#39d353" fill-opacity=".25" stroke="#39d353" stroke-width="3"/>')
    for i,k in enumerate(data):
        a=-math.pi/2+i*2*math.pi/n; x=cx+(R+42)*math.cos(a); y=cy+(R+42)*math.sin(a)
        anchor="middle" if abs(math.cos(a))<.3 else ("start" if math.cos(a)>0 else "end")
        svg.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{fg}" font-family="Segoe UI,Arial" font-size="13">{k}</text>')
    svg.append("</svg>"); return "\n".join(svg)
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--skills",default="assets/skills.json"); p.add_argument("--out",default="assets")
    a=p.parse_args(); data=json.loads(Path(a.skills).read_text())
    for t in ("dark","light"):
        Path(a.out,f"radar-{t}.svg").write_text(render(data,"Technical Skills",t=="dark"),encoding="utf-8")
