# 轉會期看板

遊者 GamePacker 的英雄聯盟轉會期看板。純靜態網頁：`index.html` 讀 `data.json` 畫出來，沒有後端。

## 更新流程（V 做）
1. 掃 Sheep X、Leaguepedia、合約庫，只收官方公告與具名報導，傳聞不收。
2. 改 `data.json`：選手的 `s`（狀態）、`y`（年）、`lv`（來源級別）、`note`，最後更新 `updated` 與 `updatedLabel`。
3. 跑 `python -I check.py`，沒報錯才推。
4. `git add -A && git commit && git push`，Pages 幾分鐘內更新。

## 欄位
- `s`：`expired` 約滿、`until` 約到（要有 `y`）、`left` 官方離隊、`renewed` 官方續約（要有 `y`）、`unknown` 合約庫沒有約期。
- `lv`：`official` 球隊或 Riot 公告、`gcd` 官方合約庫、`report` 具名媒體或記者。
- `nlv`：`note` 那句話的來源級別，沒寫就用 `lv`。
- 位置 `r`：上、野、中、下、輔，不確定留空字串。

## 素材
- `logos/`：各隊隊徽，96px webp，取自 Leaguepedia，檔名是隊伍代號小寫。
- `assets/`：頻道頭像、最新長片縮圖、YouTube 與 Threads 圖示（Simple Icons，CC0）。換最新長片時改 `data.json` 的 `channel.latest` 並換 `assets/kmn.jpg`。

## 守則
- 不放選手本名與個資，只放暱稱、隊伍、位置、約期、官宣。
- 不放傳聞。查不到出處的，不寫。
- 不用破折號，不用 emoji。
- 每次更新都要改最後更新時間。

## 來源信任規則（Vic 11/17 定）
- 球隊或賽區官方 X 的公告可直接信任，標 `official`。Sheep 轉述的官方公告也算。
- 記者爆料與具名媒體報導標 `report`，寫出處。傳聞不收。

## 固定更新
每天 12:00 與 17:00 由排程任務 `transfer-board-update` 掃描並推上線。電腦與 Claude 桌面版要開著，沒開會在下次開啟時補跑。

## LPL 官方微博 UID（只讀，需 Vic 在 Chrome 登入 weibo.com）
BLG 5926660141、WBG 5937903233、TES 5449734852、iG 2099708877、JDG 6174976862、AL 6198774314、LNG 5511584320、WE 1869429662、NIP 6420953344、LGD 2157471171、UP 6424306175、OMG 3165008832、EDG 5235726837。皆為藍 V 官方帳號。
