# -*- coding: utf-8 -*-
"""生成《原画门诊》图证四张（间距 / 弧线 / 跟随重叠 / 蓄力）+ 拼版。
配色沿用仓库多巴胺色系：暖白纸底 + 墨黑 + 陶土红/赭黄/薄荷/紫。中文字体 Hiragino Sans GB / STHeiti。"""
import math, os
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
PAPER = (255, 253, 247)
INK = (34, 27, 46)
INK2 = (92, 82, 102)
INK3 = (141, 132, 150)
CLAY = (228, 87, 46)
YELLOW = (255, 198, 26)
MINT = (18, 199, 154)
VIOLET = (123, 77, 255)
PINK = (255, 46, 99)
LIME = (155, 197, 61)

FR = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FB = "/System/Library/Fonts/STHeiti Medium.ttc"


def f(size, bold=False):
    return ImageFont.truetype(FB if bold else FR, size)


def head(d, title, sub):
    d.text((60, 42), title, font=f(52, True), fill=INK)
    d.text((62, 118), sub, font=f(27), fill=INK2)
    d.line([(60, 176), (1540, 176)], fill=INK, width=3)


def newfig():
    im = Image.new("RGB", (W, H), PAPER)
    return im, ImageDraw.Draw(im)


# ---------------------------------------------------------------- 图 1 间距
def fig_spacing():
    im, d = newfig()
    head(d, "图 1 · 时间相同，间距不同", "同样是 12 帧走完这段位移：帧数没变，点的疏密变了，重量就变了")
    x0, x1 = 360, 1520
    rows = [
        ("匀速", "点距相等", "塑料感 / 像机器", INK2, lambda t: t),
        ("缓入缓出", "两端密、中段疏", "有重量、有呼吸（最常用）", MINT, lambda t: 3 * t * t - 2 * t * t * t),
        ("缓入后急停", "起步密、越走越疏", "爆发 / 打斗的爽", CLAY, lambda t: t ** 2.2),
    ]
    y = 290
    for name, sub, diag, col, fn in rows:
        d.text((60, y - 46), name, font=f(38, True), fill=INK)
        d.text((60, y + 4), sub, font=f(24), fill=INK2)
        d.line([(x0, y), (x1, y)], fill=(214, 208, 198), width=3)
        for i in range(12):
            t = i / 11.0
            x = x0 + fn(t) * (x1 - x0)
            r = 13 if i in (0, 11) else 10
            d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=INK, width=2)
        d.text((x0, y + 34), "第 1 帧", font=f(22), fill=INK3)
        d.text((x1 - 90, y + 34), "第 12 帧", font=f(22), fill=INK3)
        d.text((x0 + 40, y - 60), diag, font=f(28, True), fill=col)
        y += 190
    d.text((60, 830), "每个圆点 = 一帧；点与点的距离 = 间距。原画调动作，先调这个距离，不是先改造型。",
           font=f(26), fill=INK2)
    return im


# ---------------------------------------------------------------- 图 2 弧线
def fig_arc():
    im, d = newfig()
    head(d, "图 2 · 弧线：关节是轴", "同一个起点、同一个终点 —— 走直线像连杆，走弧线才像有关节")
    # 左：直线
    lx0, lx1 = 170, 740
    ly = 570
    d.text((lx0, 240), "错 · 直线", font=f(38, True), fill=INK2)
    d.text((lx0, 296), "省事的画法：两点之间连直线", font=f(24), fill=INK2)
    d.line([(lx0, ly), (lx1, ly)], fill=INK2, width=4)
    for i in range(9):
        x = lx0 + (lx1 - lx0) * i / 8.0
        d.ellipse([x - 11, ly - 11, x + 11, ly + 11], fill=INK2, outline=INK, width=2)
    d.text((lx0, ly + 70), "诊断：手像被一根杆子推着走 —— 关节不存在", font=f(24), fill=CLAY)
    # 右：弧线
    rx0, rx1 = 890, 1460
    ry = ly
    cx = (rx0 + rx1) / 2.0
    bow = 170
    d.text((rx0, 240), "对 · 弧线", font=f(38, True), fill=MINT)
    d.text((rx0, 296), "肩→肘→腕 各走各的弧，合成一条抛物线", font=f(24), fill=INK2)
    pts = []
    for i in range(37):
        t = i / 36.0
        x = rx0 + (rx1 - rx0) * t
        yy = ry - bow * math.sin(math.pi * t)
        pts.append((x, yy))
    # 虚线引导
    for i in range(0, 36, 2):
        d.line([pts[i], pts[i + 1]], fill=(206, 236, 224), width=4)
    for i in range(0, 37, 4):
        x, yy = pts[i]
        d.ellipse([x - 11, yy - 11, x + 11, yy + 11], fill=MINT, outline=INK, width=2)
    d.text((rx0, ry + 70), "诊断：轨迹连点成弧 —— 关节的转速不一样，力才传得出去", font=f(24), fill=MINT)
    # 提示
    d.text((60, 730), "课堂工具「轨迹连点法」：把作业逐帧点出手／脚中心，连成线 ——", font=f(30, True), fill=INK)
    d.text((60, 778), "凡是连出直线的地方，就是该改的地方。", font=f(30, True), fill=CLAY)
    d.text((60, 842), "例外：机械运动、木偶／机甲要的\"断裂感\"，直线才是对的 —— 先想清楚自己在做哪一种。",
           font=f(25), fill=INK2)
    return im


# ---------------------------------------------------------------- 图 3 跟随重叠
def fig_follow():
    im, d = newfig()
    head(d, "图 3 · 惯性：主体先停，附件后停", "同一段\"停住\"的戏 —— 一起停像整块纸板，依次停才有肉")
    x0, x1 = 420, 1500
    def fx(fr):
        return x0 + (x1 - x0) * fr / 36.0

    def tl(y, bars, tag, tagcol):
        d.text((60, y - 26), tag, font=f(32, True), fill=tagcol)
        d.line([(x0, y + 96), (x1, y + 96)], fill=(214, 208, 198), width=2)
        for fr in range(0, 37, 6):
            d.line([(fx(fr), y + 96), (fx(fr), y + 104)], fill=INK3, width=2)
            d.text((fx(fr) - 20, y + 112), str(fr), font=f(20), fill=INK3)
        d.text((x1 + 6, y + 108), "帧", font=f(20), fill=INK3)
        for i, (nm, a, b, col) in enumerate(bars):
            yy = y + i * 32
            d.rounded_rectangle([fx(a), yy, fx(b), yy + 24], radius=12, fill=col, outline=INK, width=2)
            d.text((x0 - 130, yy - 2), nm, font=f(24), fill=INK)
            if nm != "躯干":
                d.line([(fx(a), yy - 14), (fx(a), yy - 2)], fill=CLAY, width=3)
        return

    tl(230, [("躯干", 0, 24, MINT), ("袖", 0, 24, CLAY), ("发", 0, 24, VIOLET)],
       "错 · 同时停", CLAY)
    d.text((1320, 236), "三个部件同帧停 → 纸板", font=f(24), fill=CLAY)
    tl(560, [("躯干", 0, 24, MINT), ("袖", 2, 27, CLAY), ("发", 4, 31, VIOLET)],
       "对 · 依次停", MINT)
    d.text((980, 726), "错开 2–4 帧，余波 1–3 次递减", font=f(24), fill=MINT)
    d.line([(fx(2), 560 + 3 * 32 - 20), (fx(4), 560 + 3 * 32 - 20)], fill=CLAY, width=3)
    d.text((60, 830), "戏曲水袖要更\"长气\"：滞后 4–12 帧、余波 2–3 次（见 03-motion/06）。",
           font=f(26), fill=INK2)
    return im


# ---------------------------------------------------------------- 图 4 蓄力
def fig_anticipation():
    im, d = newfig()
    head(d, "图 4 · 蓄力：反向预备", "位置—时间曲线里那段小小的\"先往下\"，就是力的起跑线")
    ox, oy = 300, 700          # 原点
    pw, ph = 1080, 400         # 绘图区
    d.line([(ox, oy), (ox + pw, oy)], fill=INK, width=3)
    d.line([(ox, oy), (ox, oy - ph)], fill=INK, width=3)
    d.text((ox + pw - 90, oy + 16), "帧 →", font=f(24), fill=INK2)
    d.text((150, 430), "位移 ↑", font=f(24), fill=INK2)
    for fr in range(0, 13, 2):
        x = ox + pw * fr / 12.0
        d.line([(x, oy), (x, oy + 8)], fill=INK3, width=2)
        d.text((x - 14, oy + 14), str(fr), font=f(20), fill=INK3)
    d.line([(ox, oy - 130), (ox + pw, oy - 130)], fill=(224, 218, 208), width=2)
    d.text((ox + 8, oy - 168), "目标位置", font=f(22), fill=INK3)

    def curve(dip, dipfr, label, col, dy=0):
        pts = []
        for i in range(0, 97):
            fr = i / 8.0
            if fr <= dipfr:
                y = dip * math.sin(math.pi * fr / dipfr) if dipfr else 0
            else:
                t = (fr - dipfr) / (12.0 - dipfr)
                y = -130 * (3 * t * t - 2 * t * t * t) + (0 if dipfr else 0)
            x = ox + pw * fr / 12.0
            pts.append((x, oy + y + dy))
        for i in range(len(pts) - 1):
            d.line([pts[i], pts[i + 1]], fill=col, width=5)
        return pts

    curve(0, 0.001, "", INK2, dy=6)
    curve(34, 1.5, "", YELLOW, dy=0)
    curve(58, 3.5, "", CLAY, dy=0)
    # 图例
    lg = [(INK2, "无预备：说动就动 —— \"被拽走的\""),
          (YELLOW, "预备 2 帧：反向小压（幅度 10–20%）"),
          (CLAY, "预备 6 帧 + タメ：反向更明显、停顿更久")]
    yy = 250
    for col, txt in lg:
        d.line([(70, yy + 14), (130, yy + 14)], fill=col, width=6)
        d.text((146, yy), txt, font=f(27), fill=INK)
        yy += 52
    d.text((62, 806), "反向那段 = 蓄力：方向相反、幅度更小、时间更短；太长会变\"慢\"，2–6 帧是经验区间。",
           font=f(26), fill=INK2)
    return im


out = os.path.dirname(os.path.abspath(__file__))   # 输出到本目录
os.makedirs(out, exist_ok=True)
figs = [("07-clinic-1-spacing", fig_spacing), ("07-clinic-2-arc", fig_arc),
        ("07-clinic-3-follow", fig_follow), ("07-clinic-4-anticipation", fig_anticipation)]
imgs = []
for name, fn in figs:
    im = fn()
    im.save(f"{out}/{name}.png")
    imgs.append(im)
    print("saved", f"{out}/{name}.png")

# 拼版 2x2
GAP = 24
sheet = Image.new("RGB", (W * 2 + GAP * 3, H * 2 + GAP * 3), PAPER)
pos = [(GAP, GAP), (W + GAP * 2, GAP), (GAP, H + GAP * 2), (W + GAP * 2, H + GAP * 2)]
for im, p in zip(imgs, pos):
    sheet.paste(im, p)
sheet.save(f"{out}/07-clinic-图证总览.png")
print("saved sheet", sheet.size)
