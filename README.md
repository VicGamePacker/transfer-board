# 轉會期看板

遊者 GamePacker 的英雄聯盟轉會期看板。純靜態網頁：`index.html` 讀 `data.json` 畫出來，沒有後端。

## 更新流程（V 做）
1. 掃 Sheep X、Leaguepedia、合約庫，只收官方公告與具名報導，傳聞不收。
2. 改 `data.json`：選手的 `s`（狀態）、`y`（年）、`lv`（來源級別）、`note`，最後更新 `updated` 與 `updatedLabel`。
3. 跑 `python -I check.py`，沒報錯才推。
4. `git add -A && git commit && git push`，Pages 幾分鐘內更新。

## 欄位
- `s`：`expired` 約滿、`until` 約到（要有 `y`）、`left` 官方離隊、`renewed` 官方續約（要有 `y`）。
- `lv`：`official` 球隊或 Riot 公告、`gcd` 官方合約庫、`report` 具名媒體或記者。
- `nlv`：`note` 那句話的來源級別，沒寫就用 `lv`。
- 位置 `r`：上、野、中、下、輔，不確定留空字串。

## 守則
- 不放選手本名與個資，只放暱稱、隊伍、位置、約期、官宣。
- 不放傳聞。查不到出處的，不寫。
- 不用破折號，不用 emoji。
- 每次更新都要改最後更新時間。
