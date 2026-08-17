# 《放学后，坡道之上》

项目 / 世界观名：**《乃木坂女学院》**

这是一个以乃木坂46一期生为核心的虚构名门女子学院群像企划。当前以电视剧剧本为主要开发形态，并计划在剧本结构稳定后改编为轻小说。

舞台是一所真正意义上的名门私立女子学院：制度严整、资源充足、传统深厚，也与普通社会保持一定距离。

## 核心命题

这不是“谁最强”的校园剧，而是关于：

- 谁最像这所学校的人？
- 传统与个人如何共存？
- 已经为你准备好的道路，要不要照着走？
- 明知会离开，为什么还是会舍不得？
- 人会毕业，但学校会继续存在。

一句总原则：

> 乃木坂成员负责青春，外部演员负责时间。

## 当前形式 / 开发状态

- 单季 12 集
- 常规集约 50 分钟
- 最终回《放学后》约 90 分钟
- EP01《入学》：**FINAL / LOCKED**
- EP02《裙摆》：**FINAL / LOCKED**
- EP03《午休》：**FINAL / LOCKED**
- EP05《文化祭》：**FINAL**
- 下一开发对象：**EP04《音乐室》**

## 文档结构

- `docs/series-bible/`：系列核心、人物关系与行为原则
- `docs/structure/`：12 集结构、人物弧、伏笔与 Callback
- `docs/episodes/`：逐集开发产出与正片剧本
- `docs/world/`：学校空间、制度、世代与外部世界设定
- `docs/writing/`：项目级编剧操作系统
- `docs/writers-room/`：编剧室非正式传承、AI 助手留言与合作记忆；不是 canon
- `docs/decisions/`：仍会影响后续创作的真正未决事项

## 单集开发标准

从 EP02 起，单集开发默认同时遵守：

- `docs/writing/writers-room-collaboration-principles.md`
- `docs/writing/episode-development-workflow.md`
- `docs/writing/episode-artifact-naming-standard.md`
- `docs/writing/github-usage-standard.md`
- `docs/writing/dialogue-principles.md`
- `docs/writing/audience-perspective-review.md`

其中：

> **Writers’ Room 原则决定“我们怎样一起写”；workflow 决定“按什么顺序工作”；naming standard 决定“每一步的当前真相放在哪里”；GitHub standard 决定“锁定怎样成为可验证的远端历史”。**

> **把编剧从流程劳动里解放出来，不是把编剧从创作里解放出来。**

> **前期结构负责搭脚手架；逐场阶段仍然是正式创作。**

核心文档纪律：

> **文件回答“现在是什么”；Git 回答“以前是什么”。**

每个流程节点使用稳定文件名，状态写在文件头；正常迭代不再通过 `v0.1 / v0.2 / final-final` 保存版本历史。

标准单集权威链：

```text
episode-brief.md
→ reality-review.md
→ behavior-run.md
→ beat-sheet.md
→ scene-list.md
→ treatment.md
→ screenplay.md
→ continuity-review.md
→ audience-review.md
→ scene-locks.md
→ rhythm-review.md
→ performance-review.md
→ final-read.md
→ FINAL.md
→ canon-propagation.md
```

标准步骤在 FINAL 前都必须完成并留下稳定产出物；没有复杂发现的步骤可以写得很短，不为证明工作量而扩写。

只有真正不同信息职能的专题研究进入 `research/`；不为同一职能复制版本文件。

## 新对话 / 上下文中断恢复

新的协作会话不要求重新口述整个项目历史。默认先读：

1. `docs/writing/README.md`
2. `docs/writing/writers-room-collaboration-principles.md`
3. `docs/writing/episode-development-workflow.md`
4. `docs/writing/episode-artifact-naming-standard.md`
5. `docs/writing/github-usage-standard.md`
6. 上一集 `FINAL.md` / `canon-propagation.md`
7. 当前开发集已有文件与相关 Series Bible / World / Structure 权威文件

恢复后先确认当前 Gate、已 LOCK / FINAL 的事实与真正未决的创意，再继续写。

正式状态恢复以后，也可以去读 `docs/writers-room/assistant-letters/`。那里不是流程，也不提供权威事实，只保留曾经一起坐在这间编剧室里的 AI 助手留下的话。

## 创作基调

整体希望具有宫藤官九郎式的节奏：刚让人哭出来就强迫人笑，笑着笑着反而更难受。

名门女校的高雅感是真的，后台的狼狈也是真的；幕布拉开以后，裙摆依然能站成一条线。

进一步的长期风格与协作原则见：

`docs/writing/writers-room-collaboration-principles.md`
