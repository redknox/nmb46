# 《乃木坂女学院》单集产出物命名规范

> 状态：**项目级 LOCKED 标准。**
>
> 适用于 EP02 及之后所有新开发单集；EP01 作为迁移样板，EP05 等早期开发目录不要求一次性重构历史文件，但必须明确当前权威文本。
>
> 核心原则：**文件回答“现在是什么”；Git 回答“以前是什么”。**

---

# 一、目录与基础命名

每集固定目录：

```text
docs/episodes/epNN/
```

其中 `NN` 使用两位数字：`ep01`、`ep02`、`ep12`。

当前权威产出物统一使用**稳定英文 kebab-case 文件名**。正常迭代不得在文件名中加入：

- `v0.1` / `v0.2`；
- `revision-v1.3`；
- `final-final`；
- 日期；
- `new` / `latest` / `updated`。

版本历史由 Git commit 保存。

---

# 二、STEP 0–17 标准产出物

正式开发前的 `ROOM OPEN` 不创建 episode 产出物。只有主创确认感觉已经对齐、允许进入工作状态以后，才建立 STEP 0 的 `episode-brief.md`。不要为了证明发散发生过而增加 `brainstorm-v1`、`pre-brief` 或空白占位文件。

| STEP | 流程节点 | 标准文件 | 说明 |
|---|---|---|---|
| 0 | 本集任务定义 | `episode-brief.md` | 表层事件、真正变化、M/S/L/R、禁止提前消费内容、结尾新增认知 |
| 1 | 现实 / 制度压力测试 | `reality-review.md` | 日本学校制度、流程、权限、空间、时间、现实资料与 Gate 1 结论 |
| 2 | 人物行为引擎跑测 | `behavior-run.md` | 关键人物默认反应顺序、求助阈值、关系选择、相遇来源与 Gate 2 结论 |
| 3–4 | Beat Sheet + 压力测试 | `beat-sheet.md` | 当前唯一故事骨架；压力测试结果吸收回正文，不另堆版本 |
| 5–6 | Scene List + 压力测试 | `scene-list.md` | 当前唯一场景 / sequence 连续结构 |
| 7–8 | Treatment + 压力测试 | `treatment.md` | 可拍执行层：动作、人流、空间、道具、声音、时间成本 |
| 9 | Screenplay | `screenplay.md` | 正片剧本母稿；FINAL 后仍使用同一文件名 |
| 10 | 完整连续性审查 | `continuity-review.md` | 时间、地点、位置、信息、道具、设施、物理与因果 |
| 11 | 观众视角审查 | `audience-review.md` | A/B/C 信息与 GREEN/YELLOW/RED |
| 12 | 逐场五层锁定 | `scene-locks.md` | 人物、常识、关系对白、解释减法、观众复核 |
| 13 | 整集节奏 / 重复审查 | `rhythm-review.md` | 长度、重复动作、群像点名感、气口与情绪换挡 |
| 14 | 表演 / 镜头 / 空间 / 声音审查 | `performance-review.md` | 表演、轴线、视线、声音、反应镜头与制作硬锁 |
| 15 | 最终无工具通读 | `final-read.md` | 关闭 checklist 后的纯观看判断 |
| 16 | FINAL | `FINAL.md` | **只做状态索引 / 制作说明，不复制 screenplay 正文** |
| 17 | Canon Propagation | `canon-propagation.md` | 全库同步清单与传播结果 |

## 关于“必需步骤”与“文件长度”

从 EP03 的流程复盘起，明确区分两件事：

> **标准步骤是必需的；长篇文档不是必需的。**

也就是说，一集进入 FINAL 前，上表中的标准产出物必须真实存在并反映该步骤已经完成；但如果某一关没有复杂发现，对应文件可以非常短，只需要记录：

- 检查了什么；
- 结论；
- 是否有 RED / YELLOW；
- 是否需要回退；
- 当前状态。

不能再用“这一步我们聊天里其实做过”代替稳定产出物，也不能为了显得完整而机械扩写没有信息价值的长文。

## 关于 STEP 3–8 的 review

Beat Sheet / Scene List / Treatment 的压力测试原则上**吸收回同一个稳定权威文件**，而不是自动生成：

- `beat-sheet-review.md`；
- `scene-list-review.md`；
- `treatment-review.md`。

只有当某次测试具有独立、长期研究或制作价值时，才进入 `research/`。

---

# 三、标准 episode 目录

一集完整走到 FINAL 后，标准目录骨架为：

```text
docs/episodes/epNN/
├── episode-brief.md
├── reality-review.md
├── behavior-run.md
├── beat-sheet.md
├── scene-list.md
├── treatment.md
├── screenplay.md
├── continuity-review.md
├── audience-review.md
├── scene-locks.md
├── rhythm-review.md
├── performance-review.md
├── final-read.md
├── FINAL.md
├── canon-propagation.md
└── research/                 # 仅在确有独立研究材料时存在
```

**不要为了目录整齐预先创建空文件。**

进入某个流程节点时再建立对应产出物。文件的存在本身应当说明：这一关已经实际开始。

但在请求 FINAL 前，必须执行一次目录级机械核对：

- 标准产出物是否齐全；
- 文件头状态是否与实际 Gate 一致；
- 是否还有旧 `DRAFT / 暂名 / IN PROGRESS` 与当前事实冲突；
- `FINAL.md` 将引用的文件是否真实存在。

> **Scene Locks 全部 CLOSED 不等于 episode 已经 FINAL。**

---

# 四、`research/` 的命名规则

`research/` 只保存与当前权威母稿不同信息职能的材料，例如：

- 专题现实研究；
- 空间 / 建筑验证；
- 两条真正互斥、需要并排比较的路线；
- 有长期参考价值的压力测试；
- 专业机制因果模型。

命名采用描述性 kebab-case：

```text
research/uniform-rules-reality-study.md
research/skirt-length-visual-test.md
research/classroom-study-rhythm-test.md
```

禁止把 `research/` 当成版本仓库：

```text
research/beat-sheet-v0.2.md        # 禁止
research/new-scene-list.md         # 禁止
research/screenplay-final-final.md # 禁止
```

如果某个研究结论已经被权威文件吸收，研究稿可保留作为依据，但文件头必须说明其角色：`REFERENCE` 或 `SUPERSEDED`。

---

# 五、状态字段规范

所有稳定产出物文件头建议使用以下状态之一：

- `DRAFT`：当前流程节点正在形成；
- `REVIEW`：正文已形成，正在本节点压力测试；
- `LOCKED`：本节点已通过，后续只因硬问题重开；
- `PASS / CLOSED`：审查型文件已完成并关闭；
- `FINAL / LOCKED`：正片最终权威；
- `REFERENCE`：研究 / 制作参考，不是当前正片权威；
- `SUPERSEDED`：已被后续方案完全取代，保留仅供历史阅读。

`ROOM OPEN / DEVELOPMENT / FINALIZATION / POST-FINAL` 是编剧室工作状态，不是 episode 文件头状态，不能代替上列文档状态。

不要用：

- `最新版`；
- `差不多定稿`；
- `基本 final`；
- `v2 probably final`。

状态必须让下一位读者知道：**这个文件现在能不能被当作事实引用。**

---

# 六、权威优先级

同一集出现冲突时：

1. `screenplay.md`（FINAL 后为正片最高权威）；
2. 当前 `scene-list.md` / `beat-sheet.md` / `treatment.md`；
3. `scene-locks.md` 与各 review 的制作硬锁；
4. `research/` 中的 REFERENCE；
5. SUPERSEDED / 历史文件。

如果高层权威发生硬伤修订，必须向下游传播，不允许让 review 或研究稿继续描述旧事实。

`FINAL.md` 是状态索引，不是第二份正片正文；它不能与 `screenplay.md` 竞争内容权威。

---

# 七、FINAL 的文件规则

`screenplay.md` 在 FINAL 后**不改名**。

文件头改为：

> 状态：**FINAL / LOCKED。正片权威文本。**

`FINAL.md` 不复制剧本，只记录：

- 正片权威文件；
- FINAL commit；
- 已通过的 Gate；
- 仍存在的制作级注意事项；
- Canon Propagation 状态。

这样不会出现两个“最终剧本”互相漂移。

在 `FINAL.md` 建立前，必须确认：

- `final-read.md` 已 PASS / CLOSED；
- 所有 Scene Locks 已 CLOSED；
- 标准 episode 文件齐全；
- 文件状态没有互相矛盾。

---

# 八、Canon Propagation 的文件纪律

`canon-propagation.md` 不只是记录“新增了什么”。至少分辨：

- **Add**：新增长期事实；
- **Remove**：删除已经被正片推翻的旧计划 / 旧未来；
- **Reclassify**：调整事实等级、人物受力、信息确定性、前置方式等。

传播完成后还必须记录一次 **Link / Status Audit**：

- `FINAL.md` 中所有引用存在；
- FINAL commit 正确；
- README / 当前开发对象正确；
- 没有悬空链接；
- 没有继续宣称旧状态的项目级权威文件。

---

# 九、迁移规则

## EP01

EP01 已按新流程完成，可作为命名标准的迁移样板。现有稳定权威文件继续保留；历史 sequence / pressure-test 文件不要求为了形式整齐全部删除。

## EP05

EP05 在本标准建立前已产生大量 `v0.x / revision-v1.x` 文件。

不进行无意义的大规模改名。先确认：

- 当前 FINAL 正文；
- 当前 scene locks；
- 当前 revision / 制作硬锁；

再逐步建立权威索引。Git 历史继续保存旧开发过程。

## EP02 及之后

从创建第一份文件开始直接执行本标准，不再新增同职能版本文件。

---

# 十、最终纪律

> **稳定文件名描述“它是什么”；文件头描述“它现在到哪一步”；Git 描述“它以前是什么”。**

如果一个修改只是让同一产出物变得更准确，就修改原文件并 commit。

只有信息职能真的不同，才创建新文件。

> **不要用聊天记忆代替项目状态，不要用“场景都锁了”代替 FINAL，不要用新增 canon 掩盖仍然存活的旧 canon。**
