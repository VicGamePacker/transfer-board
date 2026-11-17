"""產生當日轉會異動的多圖貼文素材。用法：python -I make_post.py 輸出資料夾
基準是今天 00:00 之前的最後一版 data.json，沒有就用今天最早的一版。只比兩邊都有的選手。"""
import json, subprocess, sys, os
from datetime import datetime, timezone, timedelta
from PIL import Image, ImageDraw, ImageFont

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
tw = timezone(timedelta(hours=8))
today = datetime.now(tw).strftime("%Y-%m-%d")

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8").stdout.strip()

base = sys.argv[2] if len(sys.argv) > 2 else git("log", "--before", today + " 00:00 +0800", "--format=%h", "-1")
if not base:
    base = git("log", "--since", today + " 00:00 +0800", "--format=%h").splitlines()[-1]
bases = base.split(",")  # 可給多個基準 commit，同一選手取最前面有他的那版
olds = [json.loads(git("show", b + ":data.json")) for b in bases]
new = json.load(open("data.json", encoding="utf-8"))

def index(d):
    m = {}
    for lg in d["leagues"]:
        for t in lg["teams"]:
            for p in t["players"]:
                m[(lg["id"], t["name"], p["n"])] = p
    return m

LV = {"official": "官方", "report": "報導", "gcd": "合約庫"}
o = {}
for od in olds:
    for k, v in index(od).items():
        o.setdefault(k, v)
n = index(new)
rows = []  # (排序, 賽區, 隊, 選手, 文字)
for k, p in n.items():
    q = o.get(k)
    if q is None:
        continue
    lgid, team, name = k
    txt = None
    if p["s"] != q["s"] or p.get("y") != q.get("y") or p["lv"] != q["lv"]:
        s, lv = p["s"], LV[p["lv"]]
        if s == "left":
            txt = f"離隊（{lv}）"
        elif s == "renewed":
            txt = f"續約到 {p.get('y')}（{lv}）"
        elif s == "expired" and p["lv"] == "official":
            txt = "合約到期（官方）"
    pn, qn = p.get("next"), q.get("next")
    if pn and (not qn or pn["n"] != qn["n"] or pn["lv"] != qn["lv"]):
        t2 = f"明年人選 {pn['n']}（{LV[pn['lv']]}）"
        txt = f"{txt}；{t2}" if txt else t2
    if txt:
        rows.append((0 if "官方" in txt.split("；")[0] else 1, lgid, team, name, txt))
if os.environ.get("ONLY_STATUS"):
    rows = [r for r in rows if not r[4].startswith("明年人選")]
rows.sort()

FB = "C:/Windows/Fonts/msjhbd.ttc"
FR = "C:/Windows/Fonts/msjh.ttc"
f = lambda s, b=True: ImageFont.truetype(FB if b else FR, s)
W, H = 1080, 1350
BG, FG, SUB, OFF, REP = (14, 17, 22), (240, 242, 245), (150, 158, 170), (80, 200, 140), (240, 180, 70)

def canvas():
    im = Image.new("RGB", (W, H), BG)
    return im, ImageDraw.Draw(im)

def footer(d):
    d.text((60, H - 80), "遊者 GamePacker　轉會期看板", font=f(30), fill=SUB)

label = datetime.now(tw).strftime("%m/%d")
nof = sum(1 for r in rows if r[0] == 0)
im, d = canvas()
d.text((60, 200), f"{label} 轉會期", font=f(120), fill=FG)
d.text((60, 360), "今日異動整理", font=f(120), fill=FG)
d.text((60, 560), f"共 {len(rows)} 筆更新", font=f(56), fill=SUB)
d.text((60, 650), f"官方 {nof} 筆　報導 {len(rows) - nof} 筆", font=f(56), fill=OFF)
d.text((60, 820), "英雄聯盟 LCK LPL LCP LEC LCS", font=f(44, False), fill=SUB)
footer(d)
im.save(os.path.join(out, "01.png"))

PER = 6
pages = [rows[i:i + PER] for i in range(0, len(rows), PER)]
for i, pg in enumerate(pages[:9]):
    im, d = canvas()
    d.text((60, 70), f"{label} 異動 {i + 1}/{min(len(pages), 9)}", font=f(52), fill=SUB)
    y = 190
    for r in pg:
        d.text((60, y), f"{r[1]}　{r[2]}", font=f(34), fill=SUB)
        d.text((60, y + 46), r[3], font=f(60), fill=FG)
        col = OFF if r[0] == 0 else REP
        d.text((60, y + 124), r[4], font=f(38), fill=col)
        d.line((60, y + 176, W - 60, y + 176), fill=(40, 46, 56), width=2)
        y += 176
    footer(d)
    im.save(os.path.join(out, f"{i + 2:02d}.png"))

lines = [f"{r[1]} {r[2]} {r[3]}：{r[4]}" for r in rows]
open(os.path.join(out, "changes.txt"), "w", encoding="utf-8").write("\n".join(lines))
print(f"基準 {base}，異動 {len(rows)} 筆（官方 {nof}），圖 {1 + min(len(pages), 9)} 張，輸出 {out}")
