import json, re, sys

d = json.load(open("data.json", encoding="utf-8"))
bad = []
for lg in d["leagues"]:
    for t in lg["teams"]:
        for p in t["players"]:
            where = f'{lg["id"]} {t["name"]} {p["n"]}'
            if p["s"] not in ("expired", "until", "left", "renewed", "unknown"):
                bad.append(where + " 狀態不合法")
            if p["s"] in ("until", "renewed") and not p.get("y"):
                bad.append(where + " 缺年份")
            if p["lv"] not in ("official", "gcd", "report"):
                bad.append(where + " 來源級別不合法")
text = open("data.json", encoding="utf-8").read()
if re.search("[—–]", text):
    bad.append("含破折號")
print("OK" if not bad else "\n".join(bad))
sys.exit(1 if bad else 0)
