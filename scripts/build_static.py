#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_static.py —— 把仓库里的 Markdown 预渲染成**自带样式、零依赖**的静态站点，输出到 site/。

为什么需要它：
  GitHub Pages 用 Jekyll 把 .md 变成 .html，所以站内链接（xxx.html）**只在 Pages 上有效**。
  而国内可直连的 CDN（cdn.jsdelivr.net）只按仓库原样发文件 → .html 不存在、链接全 404。
  本脚本在仓库里另建一份 site/ 镜像（结构相同、页面自带 CSS），于是**任何静态托管/网盘/CDN 都能整站打开**。

用法：  python3 scripts/build_static.py
产物：  site/**/*.html   +  site/index.html（首页副本）+ site/css、site/js
"""
import html
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
SKIP_DIRS = {".git", "scripts", "site", "node_modules"}

CSS = """
:root{--paper:#FFFDF7;--ink:#221B2E;--ink2:#5C5266;--clay:#E4572E}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
 font-family:'Hiragino Sans GB','Noto Sans SC','Microsoft YaHei',-apple-system,sans-serif;
 line-height:1.8;-webkit-font-smoothing:antialiased}
.bar{position:sticky;top:0;z-index:9;background:var(--paper);border-bottom:3px solid var(--ink);
 padding:10px 18px;display:flex;gap:12px;flex-wrap:wrap;font-weight:800;font-size:15px}
.bar a{color:var(--ink);text-decoration:none;border:2px solid var(--ink);border-radius:999px;
 padding:3px 12px;background:#FFF6E4}
.bar a:hover{background:#FFEFD6}
.bar .sp{flex:1}
.wrap{max-width:1000px;margin:0 auto;padding:26px 20px 90px}
h1{font-size:33px;line-height:1.35;margin:.2em 0 .6em;padding-bottom:.25em;border-bottom:4px solid var(--ink)}
h2{font-size:25px;margin:1.6em 0 .5em;padding-left:.5em;border-left:8px solid var(--clay)}
h3{font-size:20px;margin:1.3em 0 .4em}
h4{font-size:17px;margin:1.1em 0 .3em;color:var(--ink2)}
p{margin:.6em 0}
a{color:var(--clay)}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:15px;background:#fff}
th,td{border:2px solid var(--ink);padding:7px 10px;text-align:left;vertical-align:top}
th{background:#FFF6E4;font-weight:800}
tr:nth-child(even) td{background:#FFFAF0}
code{background:#F4EFE6;border:1px solid #DED6C8;border-radius:5px;padding:1px 5px;font-size:.92em}
pre{background:#FFF6E4;border:3px solid var(--ink);border-radius:14px;padding:14px 16px;overflow:auto}
pre code{background:none;border:none;padding:0}
blockquote{margin:1em 0;padding:.5em 1em;border-left:8px solid var(--clay);background:#FFF6E4;border-radius:0 12px 12px 0}
blockquote p{margin:.3em 0}
ul,ol{padding-left:1.5em;margin:.6em 0}
li{margin:.25em 0}
hr{border:none;border-top:3px dashed #D6D0C6;margin:2em 0}
img{max-width:100%;border:3px solid var(--ink);border-radius:12px;background:#fff}
.foot{margin-top:3em;padding-top:1em;border-top:3px solid var(--ink);font-size:14px;color:var(--ink2)}
"""


def esc(t):
    return html.escape(t, quote=False)


def _target(url):
    """把 md 里的相对目标改写成 site/ 镜像里可用的目标。"""
    if url.startswith(("http://", "https://", "#", "mailto:")):
        return url
    if url.endswith(".md"):
        return url[:-3] + ".html"
    if url.endswith(".html") or url.endswith(("/",)):
        return url
    return "../" + url          # 图片等资产：从 site/<子目录>/ 退回仓库根


def inline(t):
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes)-1}\x00"

    t = re.sub(r"`([^`]+)`", stash, t)
    t = esc(t)
    t = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", lambda m: f'<img alt="{m.group(1)}" src="{_target(m.group(2))}">', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{_target(m.group(2))}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)

    def unstash(m):
        return "<code>" + esc(codes[int(m.group(1))]) + "</code>"

    return re.sub(r"\x00(\d+)\x00", unstash, t)


def md_to_html(md):
    lines = md.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>" + esc("\n".join(buf)) + "</code></pre>")
            continue
        if ln.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<table><thead><tr>"] + [f"<th>{inline(h)}</th>" for h in head] + ["</tr></thead><tbody>"]
            for r in rows:
                r += [""] * (len(head) - len(r))
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r[:len(head)]) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            lv = len(m.group(1))
            out.append(f"<h{lv}>{inline(m.group(2).strip())}</h{lv}>")
            i += 1
            continue
        if re.match(r"^\s*(-{3,}|\*{3,})\s*$", ln):
            out.append("<hr>")
            i += 1
            continue
        if ln.strip().startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>" + "".join(f"<p>{inline(b)}</p>" for b in buf if b) + "</blockquote>")
            continue
        if re.match(r"^\s*([-*]|\d+\.)\s+", ln):
            ordered = bool(re.match(r"^\s*\d+\.\s+", ln))
            tag = "ol" if ordered else "ul"
            buf = []
            while i < len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                item = re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i]).strip()
                item = re.sub(r"^\[ \]\s*", "☐ ", item)
                item = re.sub(r"^\[[xX]\]\s*", "☑ ", item)
                buf.append(f"<li>{inline(item)}</li>")
                i += 1
            out.append(f"<{tag}>" + "".join(buf) + f"</{tag}>")
            continue
        if not ln.strip():
            i += 1
            continue
        buf = [ln.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^\s*(#{1,6}\s|>|\||```|[-*]\s|\d+\.\s|-{3,})", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")
    return "\n".join(out)


TITLE_RE = re.compile(r"^#\s+(.*)$", re.M)


def page(md_path):
    rel = os.path.relpath(md_path, ROOT)
    md = open(md_path, encoding="utf-8").read()
    m = TITLE_RE.search(md)
    title = m.group(1).strip() if m else rel
    depth = rel.count(os.sep)
    up = "../" * depth if depth else ""
    tpl = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} · 动漫原画设计</title>
<style>{CSS}</style></head><body>
<div class="bar"><a href="{up}index.html">← 首页</a><a href="{up}README.html">README</a>
<span class="sp"></span><span>动漫原画设计 · 静态镜像</span></div>
<div class="wrap">
{md_to_html(md)}
<div class="foot">本页由 <code>scripts/build_static.py</code> 从 Markdown 静态生成 · 原仓库 Ivy-Piggy/anime-key-animation</div>
</div></body></html>
"""
    dst = os.path.join(OUT, rel[:-3] + ".html")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(tpl)
    return dst


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP_DIRS and not d.startswith(".")]
        for f in fn:
            if f.endswith(".md"):
                page(os.path.join(dp, f))
                n += 1
    # 首页与资源
    shutil.copy2(os.path.join(ROOT, "index.html"), os.path.join(OUT, "index.html"))
    for d in ("css", "js"):
        s = os.path.join(ROOT, d)
        if os.path.isdir(s):
            shutil.copytree(s, os.path.join(OUT, d), dirs_exist_ok=True)
    print(f"生成 {n} 个页面 -> {OUT}")


if __name__ == "__main__":
    main()
