# 数据库与检索式

> 找**连续动作素材**、找**镜头归属**、找**学术支撑**——三条检索线。

---

## 一、找连续动作（素材线）

| 站点 | 用途 | 检索方式 | 备注 |
|------|------|----------|------|
| **sakugabooru** | 按原画师/动作标签检索镜头片段（**最重要**） | 标签组合，如 `toshiyuki_inoue`、`effects`、`hair`、`impact_frames` | ⚠️ 标签体系以其站点自动补全为准 |
| **Sakuga Blog**（sakugabooru 的博客） | 深度分析文章（原画师专题） | 站内搜索人名/作品 | English |
| **AniPages Daily** | 日本动画作画评论的历史资料库（博文量大） | Google `site:` 检索 | English；老文章多 |
| **Animation Obsessive** | 高质量动画分析通讯 | 站内栏目检索 | English |
| **原画@wiki** | 逐集记录原画担当 | 按作品名检索 | ⚠️ 常有不全/有误 |
| **BD 映像特典 / 原画集** | **最可靠**的原画表记来源 | 购买/图书馆 | 值得为关键作品投入 |
| **B站 / YouTube** | 作画 MAD、原画集翻页、逐格讲解 | 关键词见下 | 便于课堂演示（注意版权使用范围） |
| **Internet Archive** | 早期动画/老片 | 片名检索 | 公共领域材料 |

### 关键词模板（直接可用）

```
YouTube：  原画 作画MAD / アニメ 作画 / "sakuga" MAD 2020 / <animator name> 作画
B站：      作画MAD / 原画集 / <作品名> 作画 / 逐格 / 原画讲解
sakugabooru：<artist tag> + <action tag>   （例：toshiyuki_inoue hair）
影片搜索： <作品名> + 該当シーン / <作品名> + 原画
```

---

## 二、找镜头归属（核验线）

| 步 | 做什么 |
|----|--------|
| 1 | sakugabooru 找片段，记下标注的原画师与"confidence" |
| 2 | 原画@wiki / BD 特典 交叉核对 |
| 3 | 两者一致 → 可写；不一致或空缺 → **写"归属存疑"** |
| 4 | 记录到 [../references/sourcing-log.md](../references/sourcing-log.md) |

> **原则**：宁可写"《某作品》某段落"，不写"某人的某镜头"。这是这个领域最容易翻车的地方。

---

## 三、找学术支撑（论文线）

| 库 | 用途 | 技巧 |
|----|------|------|
| **CNKI** | 中文期刊/学位论文（戏曲动画、动画教学、表演） | 用"主题"检索；导出题录；核对年卷期页 |
| **读秀 / 超星** | 中文图书的**页码与版次**核对 | 图书"原文传递"可查具体页 |
| **豆瓣** | 中文版书名/出版社/页数（快速核对） | ⚠️ 以其书页信息为准，仍需与纸本比对 |
| **CNKI/万方** | 戏曲表演理论的当代研究 | 关键词：程式、身段、四功五法 |
| **JSTOR / Project MUSE / 图书馆外文库** | 动画理论（LaMarre、日本动画研究） | 英文检索 |
| **动画学相关英文期刊** | *Animation: An Interdisciplinary Journal* 等 ⚠️ 以你校可用库为准 | 找"key animation""sakuga""acting" |

---

## 四、常用检索式（可复制）

```
sakugabooru：  hair + walk_cycle
sakugabooru：  impact_frames + effects
B站：          "原画" "间距" 讲解
B站：          "水袖" 动画
YouTube：      "Animator's Survival Kit" spacing
CNKI：         主题 = (动画 OR 原画) AND 动作规律
CNKI：         主题 = 戏曲 AND (动画 OR 漫画)
Google：       site:sakugabooru.com <animator name>
Google：       "原画" <作品名> 原画担当 一覧
```

---

## 五、工具（本机与通用）

| 用途 | 工具 |
|------|------|
| 逐格导出 | `ffmpeg -i in.mp4 -vf fps=24 frames/%04d.png`（本机可用 cv2 替代） |
| 逐格查看/标注 | QuickTime 逐帧（方向键）、剪辑软件、`mpv` 逐帧 |
| 参考对比播放 | 双窗口并排 / 逐格同步（做"我的版本 vs 参考"） |
| 摄影表 | 手写（推荐）/ 表格软件 / 2D 软件内置 |
| 2D 制作 | 按需选择（本库不推荐具体软件，见 [03-courses.md](03-courses.md)） |
