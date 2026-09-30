# -*- coding: utf-8 -*-
"""生成《动漫原画设计》流程卡两张：① 动画一天·开工流程卡 ② 抽卡日志（可打印手填）。
配色沿用站点多巴胺色系（暖白纸底 + 墨黑 + 陶土红/赭黄/薄荷/紫）。"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))
PAPER = (255, 253, 247)
INK = (34, 27, 46)
INK2 = (92, 82, 102)
CLAY = (228, 87, 46)
YELLOW = (255, 198, 26)
MINT = (18, 199, 154)
VIOLET = (123, 77, 255)
TINTS = [(255, 241, 244), (255, 246, 232), (239, 251, 246), (243, 238, 255)]
FR = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FB = "/System/Library/Fonts/STHeiti Medium.ttc"


def f(sz, bold=False):
    return ImageFont.truetype(FB if bold else FR, sz)


# ============================================================ 卡 A
W, H = 1500, 1980
im = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(im)
d.text((60, 44), "动画一天 · 开工流程卡", font=f(58, True), fill=INK)
d.text((62, 132), "一天只推一段。先拧旋钮（帧数·间距·形变），再谈画技。", font=f(28), fill=INK2)
d.line([(60, 196), (1440, 196)], fill=INK, width=3)

d.text((60, 232), "① 一天的四个时段", font=f(42, True), fill=INK)
rows = [
    ("08:30", "定段：读施工单，今天只做这一段", "不许重画昨天那一段", MINT),
    ("09:00", "出关键姿势 3–6 张（不画中间画）", "不许抠线条、不许上色", YELLOW),
    ("14:00", "补间 + 落摄影表（打数 / hold / 斜线）", "不许临时改意图句", VIOLET),
    ("16:30", "回放三层自查 + 记一行抽卡日志", "不许「顺手再改一点」", CLAY),
]
y = 300
for i, (t, task, ban, col) in enumerate(rows):
    d.rounded_rectangle([60, y, 1440, y + 118], radius=18, fill=TINTS[i], outline=INK, width=3)
    d.rounded_rectangle([80, y + 26, 200, y + 92], radius=14, fill=col, outline=INK, width=3)
    d.text((100, y + 40), t, font=f(30, True), fill=INK)
    d.text((230, y + 22), task, font=f(31, True), fill=INK)
    d.text((230, y + 68), "× " + ban, font=f(25), fill=CLAY)
    y += 146

d.text((60, 920), "② 动作拆解五步（填完施工单才动笔）", font=f(42, True), fill=INK)
steps = [
    ("1  意图句", "主语+动词+对象+为什么是此刻 —— 写不出来就别画"),
    ("2  分三段", "起势（反向 2–6 帧）/ 动势（间距最大）/ 收势（缓冲+依次停）"),
    ("3  数关键姿势", "3–6 张，每张写「这张负责什么信息」；超过 8 张＝没有取舍"),
    ("4  落摄影表", "帧号 / 打数 / hold / 斜线（形变）+ 标力的起点 → 末端"),
    ("5  自查三问", "剪影读得出？重心在支撑面内？末端最后动、最后停？"),
]
y = 990
for k, v in steps:
    d.text((66, y), k, font=f(30, True), fill=CLAY)
    d.text((300, y + 1), v, font=f(27), fill=INK)
    y += 64
d.rounded_rectangle([60, 1330, 1440, 1442], radius=18, fill=(255, 250, 236), outline=INK, width=3)
d.text((86, 1348), "帧数分配：起势 15–25%　·　动势 40–50%　·　收势 30–40%", font=f(30, True), fill=INK)
d.text((86, 1394), "想更「重」就把比例往后挪；一刀砍掉收势 → 立刻变塑料。", font=f(26), fill=INK2)

d.text((60, 1500), "③ 回放三层自查（16:30 固定动作）", font=f(42, True), fill=INK)
checks = ["□ 缩到拇指大小看一遍 —— 读得懂动作吗", "□ 静音看一遍 —— 动作自身成立吗", "□ 只听声音 —— 节奏与声音合得上吗"]
y = 1572
for c in checks:
    d.text((70, y), c, font=f(29), fill=INK)
    y += 58

d.rounded_rectangle([60, 1770, 1440, 1930], radius=20, fill=(255, 241, 244), outline=CLAY, width=4)
d.text((88, 1792), "铁律三条", font=f(34, True), fill=CLAY)
d.text((88, 1844), "一天只推一段　·　一次只改一个变量　·　不许回头改昨天那一段（记进「下次改」）", font=f(28, True), fill=INK)
im.save(f"{OUT}/卡1-动画一天-开工流程卡.png")
print("card A", im.size)

# ============================================================ 卡 B
W2, H2 = 1500, 1120
im2 = Image.new("RGB", (W2, H2), PAPER)
d2 = ImageDraw.Draw(im2)
d2.text((60, 40), "抽卡日志 · 一次一变量", font=f(54, True), fill=INK)
d2.text((62, 116), "填不出「下一轮只改哪一项」，就不要开下一轮。抽卡不累积，日志才累积。", font=f(26), fill=INK2)
d2.line([(60, 176), (1440, 176)], fill=INK, width=3)
d2.rounded_rectangle([60, 200, 1440, 274], radius=16, fill=(239, 251, 246), outline=INK, width=3)
d2.text((86, 222), "四锚（全片不改）：角色参考图　·　风格串（8–15 词）　·　种子 seed　·　镜头参数", font=f(28, True), fill=INK)

cols = [("#", 56), ("段号", 76), ("目标（唯一）", 196), ("输入（首帧·尾帧·骨架·参考图）", 268),
        ("参数（种子·时长·运动）", 232), ("差在哪（只写 1 项）", 196), ("下一轮只改哪一项", 196), ("可用帧区间", 128)]
x0, hdr_h, row_h = 50, 78, 96
table_w = sum(c[1] for c in cols)
d2.rectangle([x0, 310, x0 + table_w, 310 + hdr_h], fill=(255, 246, 232), outline=INK, width=3)
x = x0
for name, w in cols:
    d2.multiline_text((x + 10, 324), name.replace("（", "\n（"), font=f(21, True), fill=INK, spacing=4)
    x += w
ty = 310 + hdr_h
for r in range(5):
    d2.rectangle([x0, ty, x0 + table_w, ty + row_h], fill=(255, 255, 255) if r % 2 else PAPER,
                 outline=(214, 208, 198), width=2)
    ty += row_h
d2.rectangle([x0, 310, x0 + table_w, ty], outline=INK, width=3)
x = x0
for _, w in cols[:-1]:
    x += w
    d2.line([(x, 310), (x, ty)], fill=(214, 208, 198), width=2)

d2.text((60, ty + 26), "范例：", font=f(28, True), fill=CLAY)
d2.text((170, ty + 30), "S3 ｜ 目标：脆桃「在减少」 ｜ 输入：首帧+尾帧+骨架 ｜ 参数：seed1234 / 2s / 缓推", font=f(24), fill=INK2)
d2.text((170, ty + 66), "差在哪：体积没变 ｜ 下一轮只改：加「第一处缺口」 ｜ 可用帧区间：12–26", font=f(24), fill=INK2)
d2.rounded_rectangle([60, ty + 118, 1440, ty + 212], radius=16, fill=(255, 241, 244), outline=CLAY, width=3)
d2.text((86, ty + 136), "研究用再加一列：与上一轮的相似度 —— 抽得越多越趋同，这就是「选择性密度」的实证。", font=f(26, True), fill=INK)
im2.save(f"{OUT}/卡2-抽卡日志.png")
print("card B", im2.size)
