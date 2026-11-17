import json, subprocess, sys
# 用法：python -I set_email.py 信箱    把合作邀約信箱寫進頁面，檢查後 commit 並推上線
d = json.load(open("data.json", encoding="utf-8"))
d["channel"]["email"] = sys.argv[1]
json.dump(d, open("data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
for cmd in (["python", "-I", "check.py"], ["git", "add", "-A"], ["git", "commit", "-q", "-m", "加入合作邀約信箱"], ["git", "push", "-q"]):
    subprocess.run(cmd, check=True)
print("done")
