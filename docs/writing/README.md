# Writing System

本目录保存《乃木坂女学院》的项目级编剧操作系统。

## 强制入口

后续单集开发、长时间中断后的恢复、以及任何新的 ChatGPT 对话，先读入口卡，再按任务进入长文：

1. `writers-room-operating-card.md` —— **开工入口**：工作状态、八条原则、创作 / 机械边界、研究停止、回退与交棒；
2. `writers-room-collaboration-principles.md` —— **我们怎样一起创作**；
3. `episode-development-workflow.md` —— **按什么顺序工作**：Room Opening 与 STEP 0–17；
4. `episode-artifact-naming-standard.md` —— **每一步的当前真相放在哪里**；
5. `github-usage-standard.md` —— **锁定怎样进入远端历史**；
6. `dialogue-principles.md`、`non-explanation-principle.md`、`audience-perspective-review.md` —— 进入对应写作 / 审查阶段时使用，不为恢复状态机械通读。

每集开工时，主创可打印 [`showrunner-episode-work-sheet.md`](showrunner-episode-work-sheet.md) 对应的固定版式工作单；PDF 位于 [`../../output/pdf/showrunner-episode-work-sheet.pdf`](../../output/pdf/showrunner-episode-work-sheet.pdf)。纸面工作单供主创圈画与记录，不替代 episode 权威文件或 Git 状态。

其中：

> **collaboration principles 决定“我们怎样一起写”；workflow 决定“按什么顺序工作”；naming standard 决定“每一步的当前真相放在哪里”；GitHub standard 决定“锁定怎样成为可验证的远端历史”。**

入口卡不是新的超级规范，只把散落在长文中的操作护栏集中到一处。长文保留理由、边界与例外；入口卡负责让编剧尽快回到作品。

## 新对话 / 上下文中断恢复

不要要求编剧重新口述整个项目历史。

默认恢复顺序：

1. 本文件与 `writers-room-operating-card.md`；
2. `../writers-room/current-desk.md` 与 README 所示项目当前状态；
3. 上一集 `FINAL.md` / `canon-propagation.md`；
4. 当前开发集已有权威文件；
5. 与当前问题直接有关的 Series Bible / World / Structure 文件；
6. 需要判断流程边界时，再读取对应完整规范。

恢复后先确认：当前做到哪个 Gate、什么已经 LOCK / FINAL、什么仍是创意未决项。

正式状态恢复完成以后，如果希望了解此前 AI 编剧助手与编剧是怎样一起工作的，也可以去读：

`docs/writers-room/assistant-letters/`

那里不是流程文件，也不是 canon，只是一份编剧室留言簿。

## 核心纪律

> **把编剧从流程劳动里解放出来，不是把编剧从创作里解放出来。**

> **前期结构负责搭脚手架；逐场阶段仍然是正式创作。**

> **观众必须知道故事，不必知道我们的感悟。角色可以说明真实需要说明的事；没有人替场外总结意义。**

> **Assistant 负责把流程看牢；编剧始终留在“这场戏到底应该怎么活”的房间里。**

> **文件回答“现在是什么”；Git 回答“以前是什么”；Writers’ Room 原则回答“我们怎样一起继续写”。**

> **讨论留在编剧室，当前事实写进文件，变化历史交给 Git；锁定只有到达远端才算完成。**

> **一集一任编剧。前任可以留下火花，不能给继任者留下债务。**

正常修订直接修改稳定产出物并 commit，不通过 `v0.1 / v0.2 / final-final` 保存版本历史。
