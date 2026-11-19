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
- Inven Global 與 Dot Esports 列為固定來源（Vic 11/18 指定）。兩家轉述球隊官方公告時，可標 `official` 並附文章連結；自己的消息與爆料標 `report`。

## 固定更新
每天 12:00、17:00、23:00（23:00 場另產貼文素材）由排程任務 `transfer-board-update` 掃描並推上線。電腦與 Claude 桌面版要開著，沒開會在下次開啟時補跑。

## LPL 官方微博 UID（只讀，需 Vic 在 Chrome 登入 weibo.com）
BLG 5926660141、WBG 5937903233、TES 5449734852、iG 2099708877、JDG 6174976862、AL 6198774314、LNG 5511584320、WE 1869429662、NIP 6420953344、LGD 2157471171、UP 6424306175、OMG 3165008832、EDG 5235726837。皆為藍 V 官方帳號。

## 2027 欄（原「明年可能人選」，Vic 11/18 改）
- 網頁右欄顯示 2027：選手已續約（renewed）或合約到 2027 年（含）以上，直接列選手本人；新加入選手（joins）列自己；其餘顯示 `next` 人選。

- 欄位 `next`：`{"n":"人選","lv":"report","src":"Sheep 文章網址"}`，放在「目前選手」那一列，對應 Sheep 轉會追蹤頁的同位置。
- 來源頁：https://www.sheepesports.com/en/all/transfers/ 的 lec、lcs、lck、lpl、lcp 分頁。連結文字是新人選，連結網址是來源文章。
- 全是記者報導，標 `report`。球隊官宣後，把該選手改成官方狀態並拿掉 `next` 或改成官方。

- 取材範圍：Sheep 轉會追蹤頁、具名媒體（Inven、Dot Esports、Insider Gaming 等）、記者的 X 與微博貼文、球隊與選手官方社群。匿名、論壇、自媒體整理一律不收，查不到出處不寫。
- `next.srcX`：Sheep X 爆料貼文網址（選填），頁面顯示成「X」連結。Sheep X 的 [SOURCES] 與 [BREAKING] 貼文都可當明年人選來源。

## 補充來源（Vic 11/17 指定）
- LCP 各隊另看 Facebook 粉專（Vic 的 Chrome 已登入，只讀）：CTBC Flying Oyster `facebook.com/ctbc.flyingoyster`、Deep Cross Gaming `facebook.com/DeepCrossGaming`、GAM `facebook.com/GAMeSportsVN`、MVK `facebook.com/MVKEsportsLOL`、Team Secret Whales `facebook.com/TeamSecretWhales`。
- Cool-Style 轉會整理文可信，標 `report`，對外只寫英文名 Cool-Style，不寫中文名（Vic 11/17）；文中沒列原始出處的項目，備註要寫明並待官方確認。

## 每日 23:00 貼文素材
排程 23:00 場更新完會跑 `python -I make_post.py 輸出資料夾`，比對今天 00:00 前最後一版 data.json，產出多圖（01.png 封面，之後每頁 6 筆異動）加 changes.txt，再由 V 寫 Threads 文案。圖與文案放 vault `03 GamePacker\近期\轉會看板貼文\日期\`，Vic 自己發。

## CBLOL（Vic 11/18 加入）
- 名單與約期：Riot 官方合約庫 Americas 分頁（gid 0），只收一軍，不收 Two-Way 與 Inactive。
- 消息來源只看 CBLOL 官方 X（x.com/CBLOL）、各隊官方 X、Sheep（轉會追蹤頁 /cblol 分頁與 X）。
- 尚無隊徽（Leaguepedia 圖檔 curl 會 403，需用 Chrome 取）。
