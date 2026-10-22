# ICOPE 長者量六力 共學活動簡報

115 年度長者內在能力檢測服務單位共學活動（09:30–12:30）用的互動簡報：
- 共學主題報告（一）案例討論與反饋＝微觀：機構版個案模擬，初評 → 複評 → 介入計畫 → 3 個月追蹤 → 6 個月後測
- 共學主題報告（二）數據分析與策略研討＝宏觀：全市數據、指標、漏斗、新開案分析、單位自我診斷計算器、行動承諾

線上版：https://mattsue1003.github.io/icope-colearning/

## 操作
- ← → 或空白鍵換頁，`T` 目錄，`N` 講者備註，`F` 全螢幕
- 網址加 `#s9` 可直接開第 9 頁
- 手機會自動切換成上下捲動

## 檔案
- `index.html`：可直接開啟／GitHub Pages 用（由 `build.sh` 產生）
- `deck.html`：簡報內容原始檔，修改後執行 `zsh build.sh`
- `img/qr-line.png`：LINE 社群 QR code（第 2 頁，報到時投影）
- `img/qr-survey.png`：滿意度問卷 QR code（最後一頁）
  圖檔放進 `img/` 後重新整理即顯示；沒有圖檔時會顯示提示框。

## 學員講義（直式 A4 PDF）
- `handout.pdf`：首頁有網頁版 QR code；兩次討論後各有一頁空白討論記錄頁（一、討論的記錄重點／二、相關記錄內容）
- 重新產生：`python3 handout_build.py img/qr-web.svg` → `NODE_PATH=<puppeteer-core 所在 node_modules> node handout_pdf.cjs handout.pdf`

## 資料說明
宏觀數據來自 2026 機構訪查篩選表，已去識別化為單位代碼，只呈現比率與類型加總。個案「李阿嬤」為教學用虛構個案。規定內容以國民健康署最新函文公告為準。
