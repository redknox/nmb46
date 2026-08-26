#!/usr/bin/env python3
"""Generate the fixed-layout A4 showrunner episode work sheet."""

from pathlib import Path
from urllib.request import urlretrieve

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "showrunner-episode-work-sheet.pdf"
FONT_CACHE = ROOT / "tmp" / "pdfs" / "fonts" / "LXGWWenKaiLite-Medium.ttf"
FONT_URL = "https://raw.githubusercontent.com/lxgw/LxgwWenKai-Lite/main/fonts/TTF/LXGWWenKaiLite-Medium.ttf"

PAGE_W, PAGE_H = A4
MARGIN = 14 * mm
CONTENT_W = PAGE_W - 2 * MARGIN
INK = colors.HexColor("#182231")
ACCENT = colors.HexColor("#334C6D")
PALE = colors.HexColor("#E9EEF4")
LIGHT = colors.HexColor("#F6F8FA")
GRID = colors.HexColor("#AAB4C0")
WHITE = colors.white

if not FONT_CACHE.exists():
    FONT_CACHE.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve(FONT_URL, FONT_CACHE)

pdfmetrics.registerFont(TTFont("WorkSheetCN", str(FONT_CACHE)))
CN = "WorkSheetCN"
EN = "Helvetica"
EN_BOLD = "Helvetica-Bold"


def width(text, font=CN, size=8):
    return pdfmetrics.stringWidth(str(text), font, size)


def wrap(text, max_width, font=CN, size=8):
    text = str(text)
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        line = ""
        for ch in paragraph:
            trial = line + ch
            if line and width(trial, font, size) > max_width:
                lines.append(line)
                line = ch
            else:
                line = trial
        if line:
            lines.append(line)
    return lines


def draw_wrapped(c, text, x, top, max_width, size=8, leading=None, color=INK, max_lines=None):
    leading = leading or size * 1.45
    lines = wrap(text, max_width, CN, size)
    if max_lines is not None:
        lines = lines[:max_lines]
    c.setFont(CN, size)
    c.setFillColor(color)
    y = top
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def checkbox(c, x, y, size=3.4 * mm):
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.7)
    c.rect(x, y - size, size, size, fill=0, stroke=1)


def header(c, page_no, title, subtitle):
    c.setFillColor(INK)
    c.rect(0, PAGE_H - 22 * mm, PAGE_W, 22 * mm, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont(CN, 15)
    c.drawString(MARGIN, PAGE_H - 11.5 * mm, title)
    c.setFont(CN, 7.5)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 11.5 * mm, subtitle)
    c.setFillColor(ACCENT)
    c.rect(0, PAGE_H - 24 * mm, PAGE_W, 2 * mm, fill=1, stroke=0)
    footer(c, page_no)


def footer(c, page_no):
    c.setStrokeColor(GRID)
    c.setLineWidth(0.35)
    c.line(MARGIN, 11 * mm, PAGE_W - MARGIN, 11 * mm)
    c.setFont(EN, 7)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN, 6.8 * mm, "NOGIZAKA GIRLS' ACADEMY - WRITERS' ROOM")
    c.drawRightString(PAGE_W - MARGIN, 6.8 * mm, f"{page_no} / 6")


def section_title(c, text, x, top, w):
    c.setFillColor(PALE)
    c.roundRect(x, top - 8 * mm, w, 8 * mm, 2 * mm, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont(CN, 9.5)
    c.drawString(x + 3 * mm, top - 5.3 * mm, text)


def writing_box(c, x, top, w, h, title, prompt=None, lines=3):
    bottom = top - h
    c.setStrokeColor(GRID)
    c.setFillColor(WHITE)
    c.setLineWidth(0.65)
    c.roundRect(x, bottom, w, h, 2 * mm, fill=1, stroke=1)
    c.setFillColor(ACCENT)
    c.setFont(CN, 8.5)
    c.drawString(x + 3 * mm, top - 5.4 * mm, title)
    line_top = top - 10 * mm
    if prompt:
        line_top = draw_wrapped(c, prompt, x + 3 * mm, line_top, w - 6 * mm, 6.9, color=colors.HexColor("#5A6573"), max_lines=2) - 1 * mm
    if lines:
        available = max(line_top - (bottom + 4 * mm), 2 * mm)
        step = available / max(lines, 1)
        c.setStrokeColor(colors.HexColor("#D5DBE2"))
        c.setLineWidth(0.35)
        y = line_top - step * 0.7
        for _ in range(lines):
            if y <= bottom + 2.5 * mm:
                break
            c.line(x + 3 * mm, y, x + w - 3 * mm, y)
            y -= step
    return bottom


def field(c, x, top, w, label):
    c.setFillColor(LIGHT)
    c.setStrokeColor(GRID)
    c.roundRect(x, top - 13 * mm, w, 13 * mm, 1.5 * mm, fill=1, stroke=1)
    c.setFillColor(ACCENT)
    c.setFont(CN, 7)
    c.drawString(x + 2.5 * mm, top - 4.2 * mm, label)
    c.setStrokeColor(colors.HexColor("#CBD2DA"))
    c.line(x + 2.5 * mm, top - 10.3 * mm, x + w - 2.5 * mm, top - 10.3 * mm)


def step_box(c, x, top, w, h, number, title, purpose, creator, gate):
    bottom = top - h
    c.setStrokeColor(GRID)
    c.setFillColor(WHITE)
    c.setLineWidth(0.6)
    c.roundRect(x, bottom, w, h, 2 * mm, fill=1, stroke=1)
    c.setFillColor(PALE)
    c.roundRect(x, top - 10 * mm, w, 10 * mm, 2 * mm, fill=1, stroke=0)
    c.rect(x, top - 10 * mm, w, 4 * mm, fill=1, stroke=0)
    checkbox(c, x + 3 * mm, top - 3.1 * mm, 3.2 * mm)
    c.setFillColor(INK)
    c.setFont(EN_BOLD, 8.5)
    c.drawString(x + 8.2 * mm, top - 6.2 * mm, f"STEP {number}")
    c.setFont(CN, 9)
    c.drawString(x + 24 * mm, top - 6.2 * mm, title)
    y = top - 14 * mm
    y = draw_wrapped(c, "解决：" + purpose, x + 3 * mm, y, w - 6 * mm, 6.8, max_lines=2) - 1 * mm
    y = draw_wrapped(c, "主创：" + creator, x + 3 * mm, y, w - 6 * mm, 7.1, color=ACCENT, max_lines=3) - 1 * mm
    c.setStrokeColor(colors.HexColor("#D2D8DF"))
    c.setLineWidth(0.35)
    for line_y in (bottom + 10 * mm, bottom + 6 * mm):
        c.line(x + 3 * mm, line_y, x + w - 3 * mm, line_y)
    c.setFont(CN, 6.5)
    c.setFillColor(colors.HexColor("#697482"))
    c.drawString(x + 3 * mm, bottom + 2.4 * mm, f"通过：{gate}")
    c.drawRightString(x + w - 3 * mm, bottom + 2.4 * mm, "日期 / 状态：____________")
    return bottom


def page_one(c):
    header(c, 1, "《乃木坂女学院》主创单集工作单", "EPISODE CREATIVE DESK")
    top = PAGE_H - 30 * mm
    gap = 3 * mm
    widths = [20, 46, 42, 30, 32]
    labels = ["EP", "集名", "本任 Assistant 编剧", "开工日期", "目标时长 / 形式"]
    x = MARGIN
    for w_mm, label in zip(widths, labels):
        field(c, x, top, w_mm * mm, label)
        x += w_mm * mm + gap

    top -= 18 * mm
    room_top = top
    top = writing_box(
        c,
        MARGIN,
        top,
        CONTENT_W,
        31 * mm,
        "ROOM OPEN｜编剧室开场",
        "先发散：想看见谁？什么令人兴奋？编剧主动带来了什么？主创确认感觉对齐后，才进入 STEP 0。",
        2,
    ) - 4 * mm
    checkbox(c, MARGIN + CONTENT_W - 42 * mm, room_top - 3 * mm, 3.2 * mm)
    c.setFillColor(ACCENT)
    c.setFont(CN, 7.2)
    c.drawString(MARGIN + CONTENT_W - 37 * mm, room_top - 6.1 * mm, "主创：可以进入工作状态")
    left_w = 112 * mm
    right_x = MARGIN + left_w + 5 * mm
    right_w = CONTENT_W - left_w - 5 * mm
    b1 = writing_box(c, MARGIN, top, left_w, 29 * mm, "本集为什么存在", "一句话说不清，就先不进入 Beat Sheet。", 2)
    b2 = writing_box(c, right_x, top, right_w, 29 * mm, "表层发生什么", "观众这一集实际看见的事件。", 2)
    top = min(b1, b2) - 4 * mm
    b1 = writing_box(c, MARGIN, top, left_w, 28 * mm, "本集真正改变什么", "人物行为顺序、关系、世界状态或观众认知。", 2)
    b2 = writing_box(c, right_x, top, right_w, 28 * mm, "结尾状态 / 最后一幅画面", None, 2)
    top = min(b1, b2) - 4 * mm

    section_title(c, "人物压力等级", MARGIN, top, CONTENT_W)
    top -= 11 * mm
    col_gap = 3 * mm
    col_w = (CONTENT_W - 3 * col_gap) / 4
    for idx, (code, desc) in enumerate([
        ("M", "主推进"), ("S", "次推进"), ("L", "被照亮"), ("R", "休息")
    ]):
        x = MARGIN + idx * (col_w + col_gap)
        writing_box(c, x, top, col_w, 21 * mm, f"{code}｜{desc}", None, 1)
    top -= 25 * mm

    half = (CONTENT_W - 5 * mm) / 2
    b1 = writing_box(c, MARGIN, top, half, 25 * mm, "禁止提前消费", "人物弧、秘密、关系或后续集的重量。", 2)
    b2 = writing_box(c, MARGIN + half + 5 * mm, top, half, 25 * mm, "明确留给后续", None, 2)
    top = min(b1, b2) - 4 * mm
    b1 = writing_box(c, MARGIN, top, half, 31 * mm, "非拍不可的三场戏", "如果只能留下三场，会是哪三场？", 2)
    b2 = writing_box(c, MARGIN + half + 5 * mm, top, half, 31 * mm, "当前最大的担心", "如果不好看，最可能死在哪里？", 3)


STEPS_EARLY = [
    (0, "本集任务定义", "本集为什么存在。", "定表层事件、真正变化、M/S/L/R 与禁止提前消费。", "一句话成立；特殊形式已签 Form Contract。"),
    (1, "现实 / 制度", "世界本来怎样运转。", "判断现实可行方向中，哪一个仍然属于这部剧。", "现实、权限、空间、时间基本成立。"),
    (2, "人物行为引擎", "人物在真实条件下先怎样动。", "判断去掉剧情需要，她是否仍会这样做。", "人物自己能走到下一步。"),
    (3, "Beat Sheet", "核心因果、转折和结尾。", "选择值得拍的故事方向。", "大型因果能够成立。"),
    (4, "Beat 压力测试", "时长、假冲突与人物弧透支。", "决定收束、删除或重构。", "大型因果结构冻结。"),
    (5, "Scene List", "逻辑怎样成为连续生活。", "判断场景重量及哪些不值得单独拍。", "观看顺序不像流程图。"),
    (6, "Scene List 压测", "传送、荧光笔感、场次与空间。", "确认人物本来就在做事，摄影机只是撞见。", "Gate 6 PASS。"),
    (7, "Treatment", "演员和摄影机能否真的完成。", "逐场判断人物、情绪、关系和结尾。", "大型故事与物理机制稳定。"),
    (8, "Treatment 压测", "执行、专业、权重和时间成本。", "确认可以进入 Screenplay。", "Gate 8 PASS。"),
]


STEPS_LATE = [
    (9, "Screenplay", "动作、对白、停顿与节奏。", "磨人物、关系、喜剧、情绪和场景结尾。", "正片母稿完整。"),
    (10, "连续性审查", "时间、位置、信息、道具、物理、因果。", "只处理需要创作选择的修正。", "无现实 / 连续性 RED。"),
    (11, "观众视角", "只承认正片可见信息。", "决定哪些不解释，哪些确实必须知道。", "A 类信息 GREEN。"),
    (12, "逐场五层锁定", "人物、常识、关系、解释与观众。", "一场一场确认最终表演事实。", "全场 LOCKED / CLOSED。"),
    (13, "整集节奏 / 重复", "同质、过长、点名感与气口。", "判断是否愿意继续和人物待在一起。", "重复与节奏风险关闭。"),
    (14, "表演 / 镜头 / 声音", "轴线、视线、反应与制作硬锁。", "决定哪些交给演员和导演。", "不靠导演技巧补 A 类缺口。"),
    (15, "最终无工具通读", "关掉 checklist，只看电视剧。", "回答：好看吗？人活着吗？会不会太正确？", "PASS / CLOSED。"),
    (16, "FINAL", "停止偏好型无限润色。", "明确确认 FINAL；只因硬伤重开。", "FINAL READY CHECK 通过。"),
    (17, "Canon Propagation", "让全项目知道正片已经改变。", "确认哪些事实成为长期 canon。", "Add / Remove / Reclassify 与链接审计完成。"),
]


def workflow_page(c, page_no, title, subtitle, steps):
    header(c, page_no, title, subtitle)
    top = PAGE_H - 30 * mm
    gap = 4 * mm
    col_w = (CONTENT_W - gap) / 2
    left = steps[:5]
    right = steps[5:]
    for col, items in enumerate([left, right]):
        x = MARGIN + col * (col_w + gap)
        usable_h = PAGE_H - 45 * mm
        box_gap = 3 * mm
        h = (usable_h - (len(items) - 1) * box_gap) / len(items)
        y = top
        for step in items:
            y = step_box(c, x, y, col_w, h, *step) - box_gap


def page_four(c):
    header(c, 4, "逐场推进记录", "SCENE LEDGER")
    top = PAGE_H - 31 * mm
    cols_mm = [12, 30, 14, 22, 76, 28]
    labels = ["场次", "暂名", "时长", "状态", "主创真正关心的东西", "LOCK / commit"]
    x_positions = [MARGIN]
    for w_mm in cols_mm:
        x_positions.append(x_positions[-1] + w_mm * mm)
    table_w = sum(cols_mm) * mm
    header_h = 9 * mm
    row_h = 10.2 * mm
    rows = 16
    table_bottom = top - header_h - rows * row_h
    c.setFillColor(ACCENT)
    c.rect(MARGIN, top - header_h, table_w, header_h, fill=1, stroke=0)
    c.setFont(CN, 7.4)
    c.setFillColor(WHITE)
    for idx, label in enumerate(labels):
        c.drawCentredString((x_positions[idx] + x_positions[idx + 1]) / 2, top - 5.8 * mm, label)
    c.setStrokeColor(GRID)
    c.setLineWidth(0.45)
    c.rect(MARGIN, table_bottom, table_w, header_h + rows * row_h, fill=0, stroke=1)
    for x in x_positions[1:-1]:
        c.line(x, table_bottom, x, top)
    for row in range(rows + 1):
        y = top - header_h - row * row_h
        c.line(MARGIN, y, MARGIN + table_w, y)
    c.setFont(EN, 7)
    c.setFillColor(colors.HexColor("#7A8490"))
    for row in range(rows):
        y = top - header_h - row * row_h - 6.3 * mm
        c.drawCentredString((x_positions[0] + x_positions[1]) / 2, y, f"S{row + 1:02d}")

    top2 = table_bottom - 5 * mm
    gap = 4 * mm
    w = (CONTENT_W - 2 * gap) / 3
    writing_box(c, MARGIN, top2, w, 46 * mm, "尚未解决，但现在不解决", "不要让开放问题污染当前步骤。", 5)
    writing_box(c, MARGIN + w + gap, top2, w, 46 * mm, "突然长出来的好东西", "先记住，不自动升级结构或 canon。", 5)
    writing_box(c, MARGIN + 2 * (w + gap), top2, w, 46 * mm, "可能需要回退的硬伤", "注明应回到哪个 STEP。", 5)


COMMANDS = [
    ("发散", "给不同可能性，不决定、不落盘"),
    ("进入工作状态", "Room Opening 对齐完成，进入 STEP 0"),
    ("收束", "停止扩展，形成当前方案"),
    ("写一版看看", "给完整草案，只展示"),
    ("重构", "保留目标，重新组织实现"),
    ("磨", "留在当前场景继续找准确状态"),
    ("挑刺", "找不真实、不好看、太像编剧之处"),
    ("压力测试", "暂停推进，从反方攻击当前方案"),
    ("查现实", "先查行业、制度、礼仪、空间"),
    ("只看观众", "只承认正片可见信息"),
    ("克制", "减作者 / 表演痕迹，不灭情感"),
    ("去解释", "删掉替观众总结意义的部分"),
    ("先过", "方向认可；结合上下文判断是否锁"),
    ("锁", "落盘、状态同步、commit、push"),
    ("推进", "锁定当前单元，进入下一项"),
    ("继续", "结合上一句：继续磨或锁后推进"),
    ("完整推送", "清点全部已确认未发布内容"),
    ("回到 STEP N", "因明确原因回退，不在后段补洞"),
    ("先别落盘", "一切留在编剧室"),
]

TERMS = [
    ("ROOM OPEN / DEVELOPMENT", "发散对齐 / 正式单集开发"),
    ("FINALIZATION / POST-FINAL", "定稿传播 / 交棒后非 canon"),
    ("STEP / Gate", "流程节点 / 进入下一层的通过条件"),
    ("DRAFT / REVIEW", "正在形成 / 正在本节点压力测试"),
    ("LOCKED / CLOSED", "创作单元冻结 / 审查完成关闭"),
    ("FINAL", "停止整集偏好型无限润色"),
    ("Beat / Scene / Sequence", "因果节拍 / 场景 / 连续段落"),
    ("Treatment / Screenplay", "可拍执行层 / 正片剧本母稿"),
    ("M / S / L / R", "主推进 / 次推进 / 被照亮 / 休息"),
    ("A / B / C", "必须明白 / 最好感觉 / 潜意识"),
    ("GREEN / YELLOW / RED", "足够 / 依赖制作 / 必须修"),
    ("Canon", "后续可引用的当前权威事实"),
    ("Propagation", "FINAL 后把事实同步到全库"),
    ("Add / Remove / Reclassify", "新增 / 删除旧事实 / 调整等级"),
    ("Form Contract", "特殊形式集的时间与不可作弊合同"),
    ("Diegetic / Camera / Target", "世界时间 / 摄影机时间 / 成片时长"),
    ("Scene → World", "局部发现经主创确认升级长期规则"),
    ("硬伤", "现实、连续性、人物、A 类或制作问题"),
    ("偏好修改", "另一种喜欢，不足以重开 LOCK / FINAL"),
    ("原子提交", "一个确认决定及其必要传播"),
]


def mini_card(c, x, top, w, h, term, meaning, number=None):
    bottom = top - h
    c.setStrokeColor(GRID)
    c.setLineWidth(0.45)
    c.setFillColor(WHITE)
    c.roundRect(x, bottom, w, h, 1.4 * mm, fill=1, stroke=1)
    if number is not None:
        c.setFillColor(ACCENT)
        c.circle(x + 4.2 * mm, top - h / 2, 2.6 * mm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont(EN_BOLD, 6.2)
        c.drawCentredString(x + 4.2 * mm, top - h / 2 - 1.8, str(number))
        term_x = x + 8.5 * mm
    else:
        term_x = x + 3 * mm
    c.setFillColor(INK)
    c.setFont(CN, 7.5)
    c.drawString(term_x, top - 4.5 * mm, term)
    draw_wrapped(c, meaning, term_x, top - 8.7 * mm, w - (term_x - x) - 2.5 * mm, 6.3, max_lines=2, color=colors.HexColor("#566170"))
    return bottom


def page_five(c):
    header(c, 5, "主创指令集", "COMMANDS")
    top = PAGE_H - 30 * mm
    section_title(c, "主创指令集", MARGIN, top, CONTENT_W)
    top -= 11 * mm
    gap = 4 * mm
    col_w = (CONTENT_W - gap) / 2
    card_h = 12.2 * mm
    row_gap = 2 * mm
    for idx, (term, meaning) in enumerate(COMMANDS):
        col = idx % 2
        row = idx // 2
        x = MARGIN + col * (col_w + gap)
        card_top = top - row * (card_h + row_gap)
        mini_card(c, x, card_top, col_w, card_h, term, meaning, idx + 1)
    rows = (len(COMMANDS) + 1) // 2
    top -= rows * (card_h + row_gap) + 7 * mm
    writing_box(c, MARGIN, top, CONTENT_W, 58 * mm, "本集自定义指令 / 简称", "临时约定只服务本集；若要成为项目级指令，需另行确认。", 7)


def page_six(c):
    header(c, 6, "术语速查", "GLOSSARY")
    top = PAGE_H - 30 * mm
    section_title(c, "流程、文本与状态", MARGIN, top, CONTENT_W)
    top -= 11 * mm
    gap = 4 * mm
    col_w = (CONTENT_W - gap) / 2
    term_h = 13.2 * mm
    term_gap = 2 * mm
    for idx, (term, meaning) in enumerate(TERMS):
        col = idx % 2
        row = idx // 2
        x = MARGIN + col * (col_w + gap)
        card_top = top - row * (term_h + term_gap)
        mini_card(c, x, card_top, col_w, term_h, term, meaning)

    c.setFillColor(INK)
    c.roundRect(MARGIN, 18 * mm, CONTENT_W, 28 * mm, 2 * mm, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont(CN, 7.5)
    safeguards = [
        "如果摄影机今天没来，这件事本来会发生吗？",
        "不值得拍的，宁可不拍。    专业归专业，情感归情感。    克制不是没有反应。",
        "角色可以说明真实需要；不替观众总结意义。    文件回答现在是什么；Git 回答以前是什么。",
    ]
    y = 39 * mm
    for line in safeguards:
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 5.5 * mm


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("《乃木坂女学院》主创单集工作单")
    c.setAuthor("《乃木坂女学院》Writers' Room")
    page_one(c)
    c.showPage()
    workflow_page(c, 2, "STEP 0–8｜故事形成", "DEVELOPMENT", STEPS_EARLY)
    c.showPage()
    workflow_page(c, 3, "STEP 9–17｜剧本形成与定稿", "FINALIZATION", STEPS_LATE)
    c.showPage()
    page_four(c)
    c.showPage()
    page_five(c)
    c.showPage()
    page_six(c)
    c.showPage()
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
