# Writing System

本目录保存《乃木坂女学院》的项目级编剧操作系统。

## 强制入口

后续单集开发、长时间中断后的恢复、以及任何新的 ChatGPT 对话，默认按以下顺序读取并遵守：

1. `writers-room-collaboration-principles.md` —— **我们怎样一起创作**：编剧参与边界、双阶段创作、逐场协作、一场一锁、Scene → World canon、特殊形式合同、FINAL readiness 与跨对话恢复协议；
2. `episode-development-workflow.md` —— **按什么顺序工作**：STEP 0–17 的流程、Gate 与回退规则；
3. `episode-artifact-naming-standard.md` —— **每一步的当前真相放在哪里**：标准产出物、文件名、状态与版本纪律；
4. `dialogue-principles.md` —— 中文呈现下的日本关系对白；
5. `audience-perspective-review.md` —— 去编剧知识后的观众视角审查。

其中：

> **collaboration principles 决定“我们怎样一起写”；workflow 决定“按什么顺序工作”；naming standard 决定“每一步的当前真相放在哪里”。**

这三层共同构成 Writers’ Room Operating System，均为默认强制标准。

## 新对话 / 上下文中断恢复

不要要求编剧重新口述整个项目历史。

默认恢复顺序：

1. 本文件；
2. `writers-room-collaboration-principles.md`；
3. `episode-development-workflow.md`；
4. `episode-artifact-naming-standard.md`；
5. 上一集 `FINAL.md` / `canon-propagation.md`；
6. 当前开发集已有文件；
7. 与当前集有关的 Series Bible / World / Structure 权威文件。

恢复后先确认：当前做到哪个 Gate、什么已经 LOCK / FINAL、什么仍是创意未决项。

## 核心纪律

> **把编剧从流程劳动里解放出来，不是把编剧从创作里解放出来。**

> **前期结构负责搭脚手架；逐场阶段仍然是正式创作。**

> **Assistant 负责把流程看牢；编剧始终留在“这场戏到底应该怎么活”的房间里。**

> **文件回答“现在是什么”；Git 回答“以前是什么”；Writers’ Room 原则回答“我们怎样一起继续写”。**

正常修订直接修改稳定产出物并 commit，不通过 `v0.1 / v0.2 / final-final` 保存版本历史。
