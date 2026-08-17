# Writing System

本目录保存《乃木坂女学院》的项目级编剧操作系统。

## 强制入口

后续单集开发、长时间中断后的恢复、以及任何新的 ChatGPT 对话，默认按以下顺序读取并遵守：

1. `writers-room-collaboration-principles.md` —— **我们怎样一起创作**：编剧参与边界、双阶段创作、逐场协作、一场一锁、Scene → World canon、特殊形式合同、FINAL readiness、一集一任编剧与跨对话恢复协议；
2. `episode-development-workflow.md` —— **按什么顺序工作**：STEP 0–17 的流程、Gate 与回退规则；
3. `episode-artifact-naming-standard.md` —— **每一步的当前真相放在哪里**：标准产出物、文件名、状态与版本纪律；
4. `github-usage-standard.md` —— **锁定怎样进入远端历史**：草稿确认、直接 `main` / PR 双路径、原子提交、工作区安全、推送校验与交接；
5. `dialogue-principles.md` —— 中文呈现下的日本关系对白；
6. `non-explanation-principle.md` —— **本剧的主旨：不解释**。角色只负责活在场里，不负责把场解释给场外；
7. `audience-perspective-review.md` —— 去编剧知识后的观众视角审查。

每集开工时，主创可打印 [`showrunner-episode-work-sheet.md`](showrunner-episode-work-sheet.md) 对应的固定版式工作单；PDF 位于 [`../../output/pdf/showrunner-episode-work-sheet.pdf`](../../output/pdf/showrunner-episode-work-sheet.pdf)。纸面工作单供主创圈画与记录，不替代 episode 权威文件或 Git 状态。

其中：

> **collaboration principles 决定“我们怎样一起写”；workflow 决定“按什么顺序工作”；naming standard 决定“每一步的当前真相放在哪里”；GitHub standard 决定“锁定怎样成为可验证的远端历史”。**

这四层共同构成 Writers’ Room Operating System，均为默认强制标准。

## 新对话 / 上下文中断恢复

不要要求编剧重新口述整个项目历史。

默认恢复顺序：

1. 本文件；
2. `writers-room-collaboration-principles.md`；
3. `episode-development-workflow.md`；
4. `episode-artifact-naming-standard.md`；
5. `github-usage-standard.md`；
6. `non-explanation-principle.md`；
7. 上一集 `FINAL.md` / `canon-propagation.md`；
8. 当前开发集已有文件；
9. 与当前集有关的 Series Bible / World / Structure 权威文件。

恢复后先确认：当前做到哪个 Gate、什么已经 LOCK / FINAL、什么仍是创意未决项。

正式状态恢复完成以后，如果希望了解此前 AI 编剧助手与编剧是怎样一起工作的，也可以去读：

`docs/writers-room/assistant-letters/`

那里不是流程文件，也不是 canon，只是一份编剧室留言簿。

## 核心纪律

> **把编剧从流程劳动里解放出来，不是把编剧从创作里解放出来。**

> **前期结构负责搭脚手架；逐场阶段仍然是正式创作。**

> **本剧的主旨：不解释。观众理解不是角色的工作。**

> **Assistant 负责把流程看牢；编剧始终留在“这场戏到底应该怎么活”的房间里。**

> **文件回答“现在是什么”；Git 回答“以前是什么”；Writers’ Room 原则回答“我们怎样一起继续写”。**

> **讨论留在编剧室，当前事实写进文件，变化历史交给 Git；锁定只有到达远端才算完成。**

> **一集一任编剧。前任可以留下火花，不能给继任者留下债务。**

正常修订直接修改稳定产出物并 commit，不通过 `v0.1 / v0.2 / final-final` 保存版本历史。
