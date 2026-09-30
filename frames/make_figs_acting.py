# -*- coding: utf-8 -*-
"""生成《02 表演原画》图证四张（面部 AU 地图 / 三层表情强度谱 / 六条时钟 / 三秒结构）+ 拼版。
配色与画法沿用 frames/make_figs.py（暖白纸底 + 墨黑 + 多巴胺色系）。中文字体 Hiragino Sans GB / STHeiti Medium。
运行：python3 frames/make_figs_acting.py
"""
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
ORANGE = (255, 122, 26)
LINE = (214, 207, 221)

L_PINK = (255, 241, 244)
L_MINT = (239, 251, 246)
L_VIOLET = (243, 238, 255)
L_ORANGE = (255, 246, 232)
FACE = (255, 247, 236)
HAIR = (239, 231, 251)

FR = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FB = "/System/Library/Fonts/STHeiti Medium.ttc"

OUT = os.path.dirname(os.path.abspath(__file__))


def f(size, bold=False):
    return ImageFont.truetype(FB if bold else FR, size)


def head(d, title, sub):
    d.text((60, 42), title, font=f(52, True), fill=INK)
    d.text((62, 118), sub, font=f(27), fill=INK2)
    d.line([(60, 176), (1540, 176)], fill=INK, width=3)


def newfig():
    im = Image.new("RGB", (W, H), PAPER)
    return im, ImageDraw.Draw(im)


def T(d, x, y, s, size=26, bold=False, fill=INK, anchor="la"):
    d.text((x, y), s, font=f(size, bold), fill=fill, anchor=anchor)


def lead(d, p1, p2, col, w=3, dash=None):
    d.line([p1, p2], fill=col, width=w)


def dot(d, xy, r, fill, outline=INK, w=3):
    x, y = xy
    d.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=outline, width=w)


def badge(d, x, y, num, col, r=28):
    d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=INK, width=3)
    T(d, x, y, num, 28, True, (255, 255, 255), "mm")


# ================================================================ 图 5 面部 AU 地图
def fig_au_map():
    im, d = newfig()
    head(d, "图 5 · 面部 AU 地图：真笑看眼，假笑看嘴",
         "FACS 把面部动作拆成 AU（动作单元）。动画上 12 个够覆盖 90% 的表演，下面是近景最常用的 7 个。")
    cx, cy, rx, ry = 470, 480, 190, 250
    d.ellipse([255, 205, 685, 725], fill=HAIR, outline=INK, width=4)
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=FACE, outline=INK, width=4)
    d.polygon([(292, 380), (300, 262), (360, 232), (470, 224), (580, 232), (640, 262), (648, 380),
               (600, 312), (470, 296), (340, 312)], fill=HAIR, outline=INK)
    d.line([(358, 428), (440, 410)], fill=INK, width=9)
    d.line([(500, 410), (582, 428)], fill=INK, width=9)
    for ex in (397, 543):
        d.ellipse([ex - 45, 455, ex + 45, 503], fill=(255, 255, 255), outline=INK, width=4)
        d.arc([ex - 45, 455, ex + 45, 503], 180, 360, fill=INK, width=7)
        d.arc([ex - 45, 455, ex + 45, 503], 12, 168, fill=INK, width=4)
        d.ellipse([ex - 15, 464, ex + 15, 494], fill=INK)
        d.ellipse([ex - 5, 470, ex + 5, 480], fill=(255, 255, 255))
    d.line([(352, 479), (334, 470)], fill=INK, width=4)
    d.line([(352, 489), (332, 491)], fill=INK, width=4)
    d.line([(588, 479), (606, 470)], fill=INK, width=4)
    d.line([(588, 489), (608, 491)], fill=INK, width=4)
    d.line([(470, 470), (470, 588)], fill=INK, width=5)
    d.arc([438, 566, 502, 606], 0, 180, fill=INK, width=5)
    d.ellipse([446, 588, 458, 600], fill=INK)
    d.ellipse([482, 588, 494, 600], fill=INK)
    d.arc([400, 618, 540, 690], 0, 180, fill=INK, width=6)
    d.arc([410, 632, 530, 696], 0, 180, fill=INK, width=4)
    d.arc([420, 718, 520, 758], 0, 180, fill=INK, width=4)
    d.line([(420, 742), (402, 858)], fill=INK, width=6)
    d.line([(520, 742), (538, 858)], fill=INK, width=6)

    au = [
        ("4", 470, 404, VIOLET, "皱眉", "眉头下压、眉心竖纹（愤怒 / 专注 / 痛苦）"),
        ("1", 444, 418, VIOLET, "内眉上扬", "眉头内侧提高（悲伤 / 担忧 / 恳求）"),
        ("6", 356, 500, PINK, "眼轮匝肌收紧", "下眼睑上顶、眼角收 —— 真笑的核心"),
        ("9", 470, 524, MINT, "鼻皱", "鼻梁起皱（厌恶）"),
        ("12", 406, 648, ORANGE, "嘴角上扬", "颧大肌拉起嘴角（笑）"),
        ("15", 534, 648, ORANGE, "嘴角下压", "降口角肌（悲伤 / 隐忍）"),
        ("17", 470, 742, YELLOW, "下巴上抬", "颏肌发力、下巴起皱（强忍 / 紧张）"),
    ]
    by = 296
    for num, dx, dy, col, name, desc in au:
        d.line([(226, by), (dx, dy)], fill=col, width=3)
        dot(d, (dx, dy), 10, col, col, 0)
        badge(d, 196, by, num, col)
        dot(d, (812, by - 8), 11, col, col, 0)
        T(d, 842, by - 8, num, 25, True, col, "lm")
        T(d, 878, by - 8, name + " — " + desc, 25, False, INK, "lm")
        by += 72
    T(d, 800, 250, "AU 编号 → 图上位置（左右对称）", 30, True, INK, "lm")
    d.rounded_rectangle([800, 806, 1520, 866], radius=14, fill=L_PINK, outline=PINK, width=4)
    T(d, 1160, 836, "只动嘴的笑 = 假笑；真笑 = AU6 + AU12，眼比嘴早 2–4 帧", 22, True, PINK, "mm")
    T(d, 60, 840, "近景里：眼先动、嘴后到 —— 这段错拍就是「真」。", 26, True, INK2, "la")
    return im


# ================================================================ 图 6 三层表情强度谱
def fig_layers():
    im, d = newfig()
    d.text((60, 42), "图 6 · 三层表情：强度谱与时间尺度", font=f(52, True), fill=INK)
    d.text((62, 116), "micro 只有 1–5 帧（40–200 ms）—— 一拍二会直接把它吃掉。", font=f(25), fill=INK2)
    d.text((62, 150), "近景黄金配比 ≈ subtle 七成 + macro 三成 + micro 闪 3–5 次。", font=f(25), fill=INK2)
    d.line([(60, 176), (1540, 176)], fill=INK, width=3)
    X0, X1 = 430, 1520
    span = X1 - X0

    def poly(vals, base, amp, col, w=7):
        pts = [(X0 + span * i / (len(vals) - 1), base - amp * v) for i, v in enumerate(vals)]
        d.line(pts, fill=col, width=w, joint="curve")
        return pts

    # macro
    base = 320
    vals = [math.sin(math.pi * (i / 60.0)) ** 1.6 for i in range(61)]
    d.line([(X0, base), (X1, base)], fill=LINE, width=2)
    poly(vals, base, 150, CLAY)
    T(d, 402, base - 6, "宏观 macro", 34, True, CLAY, "rm")
    T(d, 402, base + 30, "0.5–4 s", 25, False, INK3, "rm")
    T(d, X0 + 6, base + 46, "完整、可辨认、可控 —— 主表演由它发力", 25, False, INK2, "la")
    # subtle
    base = 540
    vals = [0.30 + 0.70 * abs(math.sin(2 * math.pi * 2.2 * (i / 60.0))) for i in range(61)]
    d.line([(X0, base), (X1, base)], fill=LINE, width=2)
    poly(vals, base, 110, VIOLET)
    T(d, 402, base - 6, "细微 subtle", 34, True, VIOLET, "rm")
    T(d, 402, base + 30, "0.5–1 s", 25, False, INK3, "rm")
    T(d, X0 + 6, base + 46, "半幅度、长 hold —— 杜丽娘的主战场", 25, False, INK2, "la")
    # micro
    base = 760
    spikes = [0.18, 0.42, 0.65, 0.86]
    vals = []
    for i in range(61):
        t = i / 60.0
        v = 0.0
        for s in spikes:
            v = max(v, math.exp(-((t - s) / 0.009) ** 2))
        vals.append(v)
    d.line([(X0, base), (X1, base)], fill=LINE, width=2)
    pts = poly(vals, base, 165, PINK)
    T(d, 402, base - 6, "微表情 micro", 34, True, PINK, "rm")
    T(d, 402, base + 30, "40–200 ms", 25, False, INK3, "rm")
    sx = pts[int(0.65 * 60)][0]
    d.line([(sx, base - 175), (sx, base - 60)], fill=PINK, width=2)
    T(d, sx + 12, base - 200, "1 帧 = 1/24 秒：靠「闪一下」起效", 25, True, PINK, "la")
    T(d, X0 + 6, base + 46, "一闪而过、无意识泄露 —— 近景「真感」的来源", 25, False, INK2, "la")
    # 配比条
    T(d, 402, 826, "近景配比", 30, True, INK, "rm")
    bw = X1 - X0
    d.rounded_rectangle([X0, 800, X0 + bw * 0.7, 852], radius=12, fill=L_VIOLET, outline=VIOLET, width=4)
    d.rounded_rectangle([X0 + bw * 0.7, 800, X1, 852], radius=12, fill=L_ORANGE, outline=CLAY, width=4)
    T(d, X0 + bw * 0.35, 826, "subtle 七成", 25, True, VIOLET, "mm")
    T(d, X0 + bw * 0.85, 826, "macro 三成", 25, True, CLAY, "mm")
    T(d, X0 + 6, 864, "位置比强度重要：把 micro 放在大表情峰值前后的 2–4 帧，或两句台词之间的空隙里。", 25, False, INK2, "la")
    return im


# ================================================================ 图 7 六条时钟
def fig_clocks():
    im, d = newfig()
    head(d, "图 7 · 六条时钟：一个近景里至少六件东西在各自走",
         "口诀：眼先到、头随后、手最后、呼吸一直在、嘴永远单干。")
    X0 = 430
    U = (1520 - X0) / 72.0

    def fx(fr):
        return X0 + fr * U

    d.line([(X0, 250), (X1 := fx(72), 250)], fill=LINE, width=2)
    for fr in range(0, 73, 12):
        d.line([(fx(fr), 242), (fx(fr), 258)], fill=LINE, width=2)
        T(d, fx(fr), 262, str(fr), 22, False, INK3, "ma")
    T(d, fx(72) + 10, 262, "帧", 22, False, INK3, "la")

    rows = [
        ("① 视线（眼球）", "眼睛像玻璃球，人像蜡像", PINK, [(8, 4), (44, 10)], "最先：比头早 1–3 帧，一拍一"),
        ("② 眨眼", "不眨眼 → 恐怖、死板", VIOLET, [(30, 4), (60, 4)], "独立：2–6 秒一次，3–4 帧画全"),
        ("③ 呼吸（胸腹+肩）", "静止帧变成「照片」", MINT, [(0, 72)], "24–36 帧一轮，永不停止"),
        ("④ 头部微动", "头僵直如支架", ORANGE, [(10, 10)], "比眼睛晚 2–4 帧，1–2 度"),
        ("⑤ 手 / 袖", "手突然出现或消失", LIME, [(24, 16)], "比意图晚 4–8 帧"),
        ("⑥ 嘴（口型）", "只有嘴在动 → 口型机", PINK, [(16, 6), (56, 6)], "独立：随台词，与其余五条无关"),
    ]
    y = 340
    for name, bad, col, segs, note in rows:
        T(d, 402, y - 14, name, 30, True, INK, "rm")
        T(d, 402, y + 18, bad, 22, False, INK3, "rm")
        d.line([(X0, y), (fx(72), y)], fill=LINE, width=2)
        for st, ln in segs:
            d.rounded_rectangle([fx(st), y - 13, fx(st + ln), y + 13], radius=13, fill=col)
        T(d, X0 + 6, y + 40, note, 23, True, col, "la")
        y += 95
    return im


# ================================================================ 图 8 三秒结构
def fig_three_sec():
    im, d = newfig()
    head(d, "图 8 · 三秒结构（72 帧 · 一拍二）：一段近景的标准弧线",
         "三条铁律：反应延迟 4–8 帧｜建立快、收回慢（8–12 : 20–30 帧）｜峰值后必须 hold。")
    X0, X1 = 190, 1520
    U = (X1 - X0) / 72.0
    BASE = 690
    AMP = 400

    def fx(fr):
        return X0 + fr * U

    keys = [(0, .10), (8, .10), (11, .18), (14, .19), (20, .35), (24, .60), (28, .86),
            (43, .86), (45, 1.00), (48, .88), (54, .82), (60, .55), (66, .32), (72, .26)]

    def v(fr):
        for i in range(len(keys) - 1):
            a, b = keys[i], keys[i + 1]
            if a[0] <= fr <= b[0]:
                t = (fr - a[0]) / float(b[0] - a[0])
                return a[1] + (b[1] - a[1]) * t
        return keys[-1][1]

    ph = [(0, 8, "①", L_VIOLET), (8, 12, "②", L_PINK), (12, 20, "③", L_ORANGE), (20, 28, "④", (255, 250, 224)),
          (28, 44, "⑤", L_MINT), (44, 54, "⑥", L_VIOLET), (54, 66, "⑦", L_PINK), (66, 72, "⑧", L_ORANGE)]
    BAND_Y = 730
    for f1, f2, num, col in ph:
        d.rounded_rectangle([fx(f1) + 2, BAND_Y, fx(f2) - 2, BAND_Y + 52], radius=10, fill=col, outline=INK, width=2)
        T(d, (fx(f1) + fx(f2)) / 2, BAND_Y + 26, num, 26, True, INK, "mm")
        if f1 > 0:
            d.line([(fx(f1), BASE - AMP * 1.06), (fx(f1), BAND_Y + 52)], fill=(226, 221, 232), width=2)
    d.line([(X0, BASE), (X1, BASE)], fill=INK, width=3)
    pts = [(fx(fr), BASE - AMP * v(fr)) for fr in range(0, 73)]
    d.line(pts, fill=INK, width=7, joint="curve")
    T(d, 176, BASE - AMP * 0.45, "情绪强度 →", 24, False, INK3, "rm")
    # 标注
    T(d, fx(1), BASE - 62, "别立刻反应", 25, True, INK2, "la")
    d.line([(fx(4), BASE - 52), (fx(9), BASE - 40)], fill=INK2, width=2)
    T(d, fx(21), 246, "建立 8–12 帧（快）", 26, True, CLAY, "la")
    d.line([(fx(23), 258), (fx(26), 300)], fill=CLAY, width=2)
    T(d, fx(30), 278, "hold —— 这一段就是「戏」", 26, True, MINT, "la")
    d.line([(fx(38), 292), (fx(39), 300)], fill=MINT, width=2)
    T(d, fx(44.6), 232, "微表情泄露 1 帧", 24, True, VIOLET, "la")
    T(d, fx(56), BASE - 96, "收回 20–30 帧（慢 2–3 倍）", 26, True, ORANGE, "la")
    d.line([(fx(58), BASE - 84), (fx(59), BASE - 150)], fill=ORANGE, width=2)
    T(d, 60, 826, "① 0–8 反应延迟　② 8–12 眼神微移　③ 12–20 头部跟随　④ 20–28 表情建立", 25, False, INK2, "la")
    T(d, 60, 862, "⑤ 28–44 hold（敢停才有重量）　⑥ 44–54 微表情泄露　⑦ 54–66 收势　⑧ 66–72 归位（留一点东西）", 25, False, INK2, "la")
    return im


def sheet(ims, path):
    s = Image.new("RGB", (1600, 900), PAPER)
    for i, im in enumerate(ims):
        s.paste(im.resize((800, 450), Image.LANCZOS), ((i % 2) * 800, (i // 2) * 450))
    s.save(path)


if __name__ == "__main__":
    figs = [("02-acting-1-au-map", fig_au_map), ("02-acting-2-layers", fig_layers),
            ("02-acting-3-six-clocks", fig_clocks), ("02-acting-4-three-seconds", fig_three_sec)]
    made = []
    for name, fn in figs:
        im = fn()
        p = os.path.join(OUT, name + ".png")
        im.save(p)
        made.append(im)
        print(name, os.path.getsize(p) // 1024, "KB")
    p = os.path.join(OUT, "02-acting-图证总览.png")
    sheet(made, p)
    print("总览", os.path.getsize(p) // 1024, "KB")
