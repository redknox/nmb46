# Writing System

本目录保存《乃木坂女学院》的项目级编剧操作系统。

## 强制入口

后续单集开发默认同时遵守：

1. `episode-development-workflow.md` —— STEP 0–17 的流程、Gate 与回退规则；
2. `episode-artifact-naming-standard.md` —— 每个流程节点的标准产出物、文件名、状态与版本纪律；
3. `dialogue-principles.md` —— 中文呈现下的日本关系对白；
4. `audience-perspective-review.md` —— 去编剧知识后的观众视角审查。

其中：

> **workflow 决定“按什么顺序工作”；naming standard 决定“每一步的当前真相放在哪里”。**

从 EP02 起，两者均为默认强制标准。

## 核心纪律

> 文件回答“现在是什么”；Git 回答“以前是什么”。

> 稳定文件名描述“它是什么”；文件头描述“它现在到哪一步”。

正常修订直接修改稳定产出物并 commit，不通过 `v0.1 / v0.2 / final-final` 保存版本历史。