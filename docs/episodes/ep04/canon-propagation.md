# EP04《音乐室》｜Canon Propagation

> 状态：**STEP 17 COMPLETE / CLOSED。**
>
> 本文件记录 EP04 FINAL 后向项目级权威文件传播的新增事实、删除旧方案、重新分类与后续集依赖核对。

---

# 一、传播源

正片最高权威：

- [screenplay.md](screenplay.md) — **FINAL / LOCKED**
- 正片 FINAL commit：`323102ba6cdcc4501384e0a6f12fa7340ffea56c`
- [FINAL.md](FINAL.md) — 状态索引与制作入口

项目级 canon 传播 commit：

- `6e1dd71875c70df1c7944781e2a7e126c772c9c5`

---

# 二、Add｜新增长期事实

1. 生田的问题不是不会演奏、听不出差异或不理解松下，而是当充分条件不存在、多个方案都成立时，正确不能替她承担选择。
2. Fukase 没有教会生田 free。他让她看见作品形成以前可以只有一点材料、可以不知道、也可以一天没有成果。
3. 松隆子持有长期教育关系；她把第一次尝试限制为“只用右手，四小节”，但不替生田指定第一个音。
4. 生田 EP04 的结束状态只是主动开始第二次：相同第一个音以后，第二个音改变。
5. 松下洸平是对作品负责的外部一线创作者，不承担生田的长期教育成长。
6. 堀以仍能独立站立的声音承担 optional first voice；中元以成熟 S2 声部长身份承担不同作品位置。两人不是竞争或替代关系。
7. 万理华选择改变作品被怎样看见，不改变作品本身；第二展示室人流较少，但仍有导览与展示编号。
8. Fukase 自己看见并索要万理华的模型；万理华直接拒绝。该场不构成成名艺术家认证作品价值。

# 三、Remove｜删除旧计划

已从长期权威删除：

- “随便弹 / 调随便 / 节拍随便”的旧 Fukase 教学场；
- 桌子、瓶子与脚步共同制造节奏，生田加入后说“后面乱了”，Fukase 回答“但你笑了”的旧方案；
- 把 EP04 概括为松隆子、Fukase 与生田围绕“技术 / 正确 / 表达”发生冲突；
- 把万理华写成作品受到质疑后捍卫作品；
- 把中元的 EP04 线解释为努力没有得到同等回报，或与堀发生替代焦虑；
- 把松隆子与 Fukase 分成“规则 / 技巧”与“感受 / free”的价值两端。

# 四、Reclassify｜重新分类

## 生田

从“技巧压制本能，需要找回训练以前的音乐”重新分类为：

> **保留全部技术、听辨与完成能力，并逐渐学会在条件不足时仍让一点材料先出现。**

## 中元

从“生田的天赋 / 努力对照”重新分类为具有自身专业岗位的 S2 声部长。天赋与努力差异仍可存在，但不能吞掉她的能力、位置和其他关系。

## 松下 / 松隆子 / Fukase

三人不是三套互相竞争的教育理念：

- 松下：已经存在的作品需要什么；
- Fukase：作品尚未存在时，材料怎样先出现；
- 松隆子：具体学生进入陌生领域时，第一步需要多大的可执行容器。

## EP04 人物受力

- M：生田；
- S：万理华、中元；
- L：西野；
- R：其余一期生；
- 堀不进入一期生受力矩阵，也不因取得特殊作品位置自动开启独立成长线。

---

# 五、本轮更新的长期权威

## 项目状态

- `README.md`
  - EP04 更新为 **FINAL / LOCKED**；
  - 下一正式开发对象改为待主创指定，落实“一集一编剧”。

## 季结构

- `docs/structure/season-12-episodes.md`
  - 用 FINAL 的五日工作、三条人物线与结尾状态替换早期“创作冲突”摘要。
- `docs/structure/season-behavior-run-v0.1.md`
  - 整体替换 EP04 早期行为跑测，回写实际动作链。
- `docs/structure/character-pressure-matrix-v0.1.md`
  - 按 FINAL 调整 EP04 的 M / S / L / R。
- `docs/structure/callbacks.md`
  - 回写生田“相同第一音、改变第二音”；
  - 新增中元与堀不同作品位置的跨集回声。

## 人物与关系

- `docs/characters/main-cast.md`
  - 删除生田旧 Fukase 场与“找回技巧以前本能”的定义；
  - 回写 EP04 的真实创作入口。
- `docs/characters/supporting-students.md`
  - 中元不再只是生田的努力参照；加入 S2 声部长与专业追问事实。
- `docs/series-bible/relationships.md`
  - 生田 × 中元从简单“天赋 / 努力”改为不同音乐能力与工作位置。
- `docs/characters/adult-cast.md`
  - 删除松隆子“没有错，但像考试”的旧提示；
  - 补全松下的作品权限与三位成人的专业边界。

## 后辈与世界

- `docs/world/next-generation.md`
  - 回写堀在 EP04 从低年级旁听区到 optional first voice、再并入 S1 的实际位置。
- `docs/world/sakuraryo-student-casting-entry-v0.1.md`
  - 将旧“音乐创作冲突”用语修正为作品选择与创作入口，继续锁定不让男技术角色介入解决。

## EP05 接口

- `docs/episodes/ep05/screenplay-scene-locks-v0.1.md`
  - 不改变 EP05 正文动作；
  - 只修正 S04 表演说明，删除 Fukase = 感受 / free、松隆子 = 规则 / 技巧的旧二元；
  - 明确 Fukase 的轻笑不是认证，生田也没有因 EP04 自动“学会 free”。

---

# 六、已核对、无需重复修改

以下文件已经与 EP04 FINAL 一致：

- `docs/structure/festival-week-calendar-lock.md`；
- `docs/world/music-and-art-annex-lock.md`；
- `docs/world/old-auditorium-space-lock.md`；
- `docs/world/club-and-afterschool-system-lock.md`；
- `docs/world/individual-arts-mentorship-lock.md`；
- `docs/world/curriculum.md`；
- `docs/series-bible/behavior-engine-v0.1.md`；
- `docs/series-bible/behavior-stress-test-v0.1.md`；
- `docs/series-bible/relationship-network-v0.2.md`。

这些文件已有正确的空间、制度、专业权限或长期行为边界，不为留下修改痕迹重复改写。

---

# 七、EP05 依赖检查

EP05 FINAL 正文不因 EP04 定稿重开。

成立原因：

- EP05 让生田在新的现场条件下继续使用 EP04 打开的工作方式，不把 EP04 的第一步追认为已经完成 free；
- 堀在 EP05 的开场位置、暂时取消与条件恢复，直接继承 EP04 的作品岗位；
- 中元继续清点、整队和完成声部工作，保持与堀不同角色；
- 万理华的作品已经移动到第二展示室，Fukase 不再在 EP05 承担作品认证功能；
- 旧礼堂确认框、正式景片加固与文化祭换场困难之间的物理因果仍成立。

本轮没有修改 EP05 当前未提交的 `screenplay-scene-locks-v1.1.md`。

---

# 八、Link / Status Audit

- EP04 标准产出物齐全；
- `screenplay.md` 为 `FINAL / LOCKED`；
- `FINAL.md` 引用的文件全部存在；
- STEP 10—15 均为 PASS / CLOSED；
- Day 2—Day 5 阶段性工作稿均为 SUPERSEDED；
- README 已显示 EP04 FINAL；
- 下一正式开发对象没有被 EP04 编剧擅自指定；
- 唯一保留的制作级 pending 是 S07 剧目片段版权许可。

---

# 九、STEP 17 结论

**COMPLETE / CLOSED。**

EP04 FINAL 已传播到需要知道它的项目级权威文件；没有发现需要重新打开 EP04 或 EP05 正片的新硬问题。

下一正式开发对象由主创另行指定。EP04 编剧不进入下一集正式编写。
