# frames/ · 图证与帧素材

> 本目录放**图证**（示意图 / 帧序列接触印相）。命名规则：`<来源条目>-<序号>-<内容>.png`。
> 例：`07-clinic-1-spacing.png` = 01-principles/07-clinic 的第 1 张图。

---

## 一、现有图证（《原画门诊》四张，2026-09-30）

| 文件 | 内容 | 配哪一节 |
|------|------|----------|
| `07-clinic-1-spacing.png` | 间距三版对比：匀速 / 缓入缓出 / 缓入后急停（12 帧点阵） | [门诊](../01-principles/07-clinic.md) 工位③ 重量感 |
| `07-clinic-2-arc.png` | 直线 vs 弧线（轨迹连点），含「轨迹连点法」 | 工位④ 弧线 |
| `07-clinic-3-follow.png` | 跟随重叠的起停时序：同时停 vs 依次停 | 工位② 惯性 |
| `07-clinic-4-anticipation.png` | 蓄力：无预备 / 预备 2 帧 / 预备 6 帧 的位置—时间曲线 | 工位① 蓄力 |
| `07-clinic-图证总览.png` | 上面四张的 2×2 拼版（投屏 / 打印用） | — |

**版权**：这五张全部是**程序生成的原创示意图**，不含任何影片帧，可自由用于课堂、论文与公开仓库。

---

## 一·B、现有图证（《02 表演原画》四张，2026-09-30）

| 文件 | 内容 | 配哪一节 |
|------|------|----------|
| `02-acting-1-au-map.png` | 面部 AU 地图：7 个常用 AU 的位置 + 「只动嘴的笑是假笑」 | [微表情 FACS](../02-acting/01-microexpression-facs.md) §二 |
| `02-acting-2-layers.png` | 三层表情（macro / subtle / micro）的强度谱与时间尺度 + 近景配比条 | 同上 §四 |
| `02-acting-3-six-clocks.png` | 六条时钟的错拍时间轴（视线/眨眼/呼吸/头/手/嘴） | [近景表演清单](../02-acting/02-closeup-acting.md) §一 |
| `02-acting-4-three-seconds.png` | 三秒结构 72 帧的情绪强度弧线（反应延迟 → hold → 慢收回） | 同上 §二 |
| `02-acting-图证总览.png` | 上面四张的 2×2 拼版（投屏 / 打印用） | — |

脚本：`python3 frames/make_figs_acting.py`（同上，改数值即出新图）。

## 二、怎么重绘（改数值即出新图）

```bash
python3 frames/make_figs.py        # 重写本目录五张 PNG
```

脚本内可改的参数都在各函数顶部（帧数、间距曲线、错开帧数、预备时长与幅度、配色）。配色沿用站点多巴胺色系（暖白纸底 + 墨黑 + 陶土红/赭黄/薄荷/紫），改色请同步 [../css/style.css](../css/style.css) 的变量。

依赖：`Pillow`；中文字体 `Hiragino Sans GB` / `STHeiti Medium`（macOS 自带）。

---

## 三、真实影片帧怎么进这里（规矩）

示意图形不能替代真实片段。要放**影片帧**（逐格导出的参考图）时：

1. 逐格导出（剪辑软件 / `cv2.VideoCapture`），不要只存视频 —— 见 [03-motion 收集方法学](../03-motion/00-index.md)。
2. 命名 `M-06-水袖抛-01.png` 这类「条目-内容-序号」。
3. **必须**在 [../references/sourcing-log.md](../references/sourcing-log.md) 记：作品 / 集数或时间码 / 原画师（查 [sakugabooru](https://www.sakugabooru.com/)）/ 核验日期。
4. 公开仓库里放他人作品的帧有版权风险 —— 教学自用可，**公开发布前先换成自绘描摹或只留外链**。

> 一句话：**示意图可以随便放，影片帧要留证据链。**
