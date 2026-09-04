#!/usr/bin/env python3
import argparse
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

def make_portrait(src, out, cols=100, equalize=False, detail=0.5, color=False):
    img = Image.open(src).convert("RGB")
    rows = max(1, int(cols * img.height / img.width))
    img = ImageOps.fit(img, (cols, rows), method=Image.Resampling.LANCZOS)
    gray = ImageOps.grayscale(img)
    if equalize:
        gray = ImageOps.equalize(gray)
    gray = ImageEnhance.Sharpness(gray).enhance(1 + detail)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols*10} {rows*10}">',
           f'<rect width="{cols*10}" height="{rows*10}" fill="#0d1117"/>']
    for y in range(rows):
        for x in range(cols):
            v = gray.getpixel((x,y))
            radius = 1.5 + (255-v)/255*3.5
            opacity = .12 + (255-v)/255*.88
            r,g,b = img.getpixel((x,y))
            fill = f"rgb({r},{g},{b})" if color else f"rgb(20,{int(120+(255-v)*.45)},{int(105+(255-v)*.58)})"
            svg.append(f'<circle cx="{x*10+5}" cy="{y*10+5}" r="{radius:.2f}" fill="{fill}" opacity="{opacity:.3f}"/>')
    svg.append("</svg>")
    out = Path(out)
    if out.suffix.lower() != ".svg":
        out = out.with_suffix(".svg")
    out.write_text("\n".join(svg), encoding="utf-8")

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("image"); p.add_argument("-o","--output",required=True)
    p.add_argument("--cols",type=int,default=100); p.add_argument("--equalize",action="store_true")
    p.add_argument("--detail",type=float,default=.5); p.add_argument("--color",action="store_true")
    p.add_argument("--reveal",action="store_true"); p.add_argument("--animate",action="store_true")
    a=p.parse_args()
    make_portrait(a.image,a.output,a.cols,a.equalize,a.detail,a.color)
