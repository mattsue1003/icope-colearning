# 由 deck.html 組出直式 A4 講義 handout.html（再用 handout_pdf.cjs 轉 PDF）
#   python3 handout_build.py <qr_web.svg>
import re, sys, pathlib
here = pathlib.Path(__file__).parent
deck = (here / "deck.html").read_text(encoding="utf-8")
qr = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")

style = re.search(r"<style>(.*?)</style>", deck, re.S).group(1)
links = "".join(re.findall(r"<link [^>]*>", deck))
script = re.search(r"<script>(.*?)</script>", deck, re.S).group(1)
ui = deck[deck.index('<div class="bar" id="bar">'):deck.index("<script>")]
secs = {re.search(r'data-title="([^"]+)"', x).group(1): x
        for x in re.findall(r"<section class=\"slide.*?</section>", deck, re.S)}

TILES = re.search(r'<div class="tiles".*?</div>\s*</div>\s*</div>', secs["封面"], re.S).group(0)

COVER = f'''<section class="hcover">
  <div class="hd"><span class="sec">115 年度 長者內在能力檢測服務｜共學活動講義</span><span>學員版</span></div>
  <p class="kicker">ICOPE · Integrated Care for Older People</p>
  <h1>長者量六力<br>共學活動講義</h1>
  <p class="cover-sub"><b>微觀</b>看個案 ✕ <b>宏觀</b>看數據</p>
  <dl class="cover-meta">
    <div><dt>主辦單位</dt><dd>基隆市衛生局</dd></div>
    <div><dt>協辦單位</dt><dd>台灣生活復能健康促進協會</dd></div>
    <div><dt>專家委員</dt><dd>長庚科技大學 倪麗芬 副教授</dd></div>
    <div><dt>主持人</dt><dd>鍾孟修 職能治療師</dd></div>
  </dl>
  <div class="hqr">
    <div class="hqr-code">{qr}</div>
    <div class="hqr-txt">
      <b>掃描開啟網頁版講義</b>
      <p>網頁版有互動圖表與「單位自我診斷計算器」，會後可隨時查看。</p>
      <p class="num url">mattsue1003.github.io/icope-colearning</p>
    </div>
  </div>
  {TILES}
  <div class="htoc">
    <div><b>一、開場</b><span>議程・分組・進行方式・服務流程</span></div>
    <div><b>二、案例討論與反饋</b><span>模擬個案・分組討論・討論記錄頁</span></div>
    <div><b>三、數據分析與策略研討</b><span>指標・全市數據・自我診斷工作單・行動承諾卡・討論記錄頁</span></div>
    <div><b>四、會後帶回</b><span>七個流程優化做法・參考資料</span></div>
  </div>
</section>'''

def rec(title, time, hint1, hint2, aid):
    return f'''<section class="rec">
  <div class="hd"><span class="sec">討論記錄｜{title}</span><span class="num">{time}</span></div>
  <div class="rec-meta">組別：□ 第一組　□ 第二組　　組長：＿＿＿＿＿＿　　記錄：＿＿＿＿＿＿　　單位：＿＿＿＿＿＿＿＿</div>
  <div class="rec-sec" style="flex:1.2">
    <h3>一、討論的記錄重點</h3>
    <p class="hint">{hint1}</p>
    <div class="lines"></div>
  </div>
  <div class="rec-sec" style="flex:1">
    <h3>二、相關記錄內容</h3>
    <p class="hint">{hint2}</p>
    {aid}
    <div class="lines"></div>
  </div>
</section>'''

TL_AID = '''<div class="rec-tl"><div class="ax"></div>
  <span style="left:0">Day 0 初評</span><span style="left:16.8%">1 個月</span><span style="left:50%">3 個月</span><span style="left:100%;transform:translateX(-100%)">6 個月</span>
  <i style="left:0"></i><i style="left:16.8%"></i><i style="left:50%"></i><i style="left:100%"></i></div>'''
GAP_AID = '''<table class="tb rec-tb"><thead><tr><th style="width:30%">缺口</th><th style="width:30%">原因</th><th>改善做法（誰、何時）</th></tr></thead>
  <tbody><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></tbody></table>'''

REC1 = rec("共學主題報告（一）案例討論與反饋", "10:15–10:57",
           "可依題號記錄：Q1 可以更早攔截的環節／Q2 追蹤的時間點與方式／Q3 介入的功勞與情境改變／Q4 單位分工與後測日",
           "在時間軸上標出你們會加的接觸點（第幾天、誰負責）；也可記下第二組的補充與專家回饋重點。", TL_AID)
REC2 = rec("共學主題報告（二）數據分析與策略研討", "11:30–12:05",
           "可依題號記錄：Q1 最大的流失段／Q2 流程原因／Q3 介入只給單張的比例／Q4 下個月先改的一件事",
           "整理缺口、原因與改善做法；也可記下需要衛生局協助的事與專家回饋重點。", GAP_AID)

order = ["今日議程", "人員介紹與分組", "兩個單元怎麼進行", "共學活動注意事項", "115 年服務流程",
         "第一段：案例討論與反饋", "認識李阿嬤", "Day 0 初評", "Day 14 複評", "個人介入計畫", "Day 90 追蹤",
         "Day 177 後測", "介入的貢獻", "案例分組討論", "@REC1", "案例反饋",
         "第二段：數據分析與策略研討", "指標怎麼算", "全市總覽", "服務漏斗", "評估效能", "介入率", "轉介率",
         "追蹤與後測", "新開案分析", "單位自我診斷", "策略研討", "30 天行動承諾", "@REC2",
         "流程優化建議", "參考資料"]
body = [COVER] + [{"@REC1": REC1, "@REC2": REC2}.get(t) or secs[t] for t in order]

CASE_TABLE = '''<table class="tb"><thead><tr><th style="width:24%">時間</th><th>發生的事</th></tr></thead><tbody>
<tr><td class="num">Day 0・3/10</td><td>初評：4 項異常</td></tr>
<tr><td class="num">Day 14・3/24</td><td>複評＋擬定個人介入計畫</td></tr>
<tr><td class="num">Day 35・4/14</td><td class="t-orange"><b>據點中斷（單位不知道）</b></td></tr>
<tr><td class="num">Day 90・6/08</td><td>3 個月追蹤：電訪＋慢箋回診順測</td></tr>
<tr><td class="num">Day 98・6/16</td><td>失智共照中心收案</td></tr>
<tr><td class="num">Day 177・9/03</td><td>6 個月後測（6 個月窗口 9/10 截止，只剩 1 週）</td></tr>
</tbody></table><p class="cap muted" style="margin-top:4px">規定窗口：追蹤＝評估滿 1 個月起至後測當日；後測＝評估後 3～6 個月（6/10–9/10）。</p>'''

POST = '''
(function(){
  document.body.classList.remove("scroll");document.body.classList.add("handout");
  new MutationObserver(function(){if(document.body.classList.contains("scroll"))document.body.classList.remove("scroll")}).observe(document.body,{attributes:true,attributeFilter:["class"]});
  var ins=document.querySelectorAll("#calc input");ins.forEach(function(i){i.value=""});if(ins[0])ins[0].dispatchEvent(new Event("input"));
  document.querySelectorAll("#calcOut .orow").forEach(function(r){var v=r.querySelector(".ov");if(v)v.textContent="＿＿＿%";var st=r.lastElementChild;if(st&&st!==v)st.innerHTML=""});
  var cs=document.querySelector('[data-title="單位自我診斷"] h2');if(cs)cs.textContent="單位自我診斷工作單";
  var src=document.getElementById("calcSrc");if(src)src.textContent="請填入你們單位的人數，再依右側公式計算各項指標（網頁版可自動計算）。";
  document.querySelectorAll("[data-reveal]").forEach(function(b){var c=b.closest(".card"),p=c&&c.querySelector("p.cap");
    if(p)p.textContent="答案於現場說明，也可在網頁版查看。";else{var n=document.createElement("p");n.className="cap muted";n.textContent="其他做法於現場說明，也可在網頁版查看。";b.after(n)}});
  var tl=document.getElementById("caseTl");if(tl)tl.parentNode.outerHTML=CASE_TABLE;
  var pc=document.getElementById("pdcaClear");if(pc){var nx=pc.nextElementSibling;pc.remove();if(nx)nx.remove()}
  document.querySelectorAll(".slegend .muted").forEach(function(e){e.remove()});
  document.querySelectorAll(".slide .pg").forEach(function(e){e.textContent=""});
  document.querySelectorAll('a[href="handout.pdf"]').forEach(function(a){var li=a.closest("li");if(li)li.remove()});
})();
'''.replace("CASE_TABLE", repr(CASE_TABLE))

PRINT_CSS = '''
@page{size:A4;margin:13mm 12mm 15mm}
*{-webkit-print-color-adjust:exact;print-color-adjust:exact}
:root{--u:.62px!important}
html,body{height:auto;background:#fff}
body.handout{background:#fff}
.handout .deck{position:static;display:block;padding:0}
.handout .slide{display:flex!important;width:auto!important;height:auto!important;box-shadow:none;border:1px solid var(--rule);border-radius:8px;padding:14px 18px 16px;margin:0 0 9px;break-inside:avoid;page-break-inside:avoid;overflow:visible;animation:none}
.handout .bar,.handout .fab,.handout .toc,.handout .notes-panel,.handout .tip,.handout aside.notes,.handout .timer,.handout [data-reveal],.handout [data-fill]{display:none!important}
.handout .xscroll{overflow:visible}
.handout .xscroll>*{min-width:0!important}
.handout .flow{grid-template-columns:repeat(4,1fr)}
.handout .steps{grid-template-columns:repeat(3,1fr)}
.handout .slide.divider{background:var(--tealbg);color:var(--ink);border:0}
.handout .slide.divider.mi{background:var(--orangebg)}
.handout .divider .hd{color:var(--ink2);border-color:var(--rule)}
.handout .divider .hd .sec{color:var(--tealink)!important}
.handout .divider.mi .hd .sec{color:var(--orangeink)!important}
.handout .divider .big{font-size:40px}
.handout .divider .lead{font-size:15px}
.handout .slide .body{flex:none}
.handout .disc,.handout .calc{flex:none}
.handout .divider .big small,.handout .divider .qs span{color:var(--ink2)}
.handout .divider .body{gap:14px!important}
.handout .calc input,.handout .pdca input,.handout .pdca textarea{background:#fff}
.handout .calc input{height:30px}
.handout .pdca textarea{height:64px}
.hcover{break-after:page;display:flex;flex-direction:column;gap:14px;padding:4px 2px}
.hcover h1{font-size:54px;margin:4px 0 6px}
.hcover .cover-meta{margin-top:6px}
.hqr{display:grid;grid-template-columns:44mm 1fr;gap:18px;align-items:center;border:1.5px solid var(--teal);border-radius:12px;padding:14px 18px;background:var(--tealbg)}
.hqr-code svg{width:44mm;height:44mm;display:block;border-radius:6px}
.hqr-txt b{font-size:22px;display:block;margin-bottom:6px}
.hqr-txt p{font-size:14px;color:var(--ink2)}
.hqr-txt .url{font-size:15px;color:var(--tealink);margin-top:8px;word-break:break-all}
.hcover .tiles{grid-template-columns:repeat(3,1fr)}
.hcover .tile{min-height:0;padding:10px}
.htoc{display:grid;grid-template-columns:1fr 1fr;gap:8px 18px;border-top:1px solid var(--rule);padding-top:10px}
.htoc div{display:flex;flex-direction:column;font-size:13px}
.htoc span{color:var(--ink2);font-size:12px}
.rec{break-before:page;break-after:page;height:262mm;display:flex;flex-direction:column;gap:10px}
.rec .hd{font-size:13px}
.rec-meta{font-size:13.5px;color:var(--ink2);padding:6px 0 2px}
.rec-sec{display:flex;flex-direction:column;gap:4px;border:1.5px solid var(--rule);border-radius:10px;padding:10px 14px 6px;min-height:0}
.rec-sec h3{font-size:17px}
.rec-sec .hint{font-size:11.5px;color:var(--ink3)}
.lines{flex:1;min-height:20mm;background-image:repeating-linear-gradient(to bottom,transparent 0,transparent calc(9mm - 1px),#C6D4D3 calc(9mm - 1px),#C6D4D3 9mm)}
.rec-tl{position:relative;height:56px;margin:8px 4px 4px}
.rec-tl .ax{position:absolute;left:0;right:0;top:30px;border-top:2px solid var(--ink)}
.rec-tl i{position:absolute;top:24px;width:2px;height:13px;background:var(--ink);transform:translateX(-1px)}
.rec-tl span{position:absolute;top:40px;font-size:11.5px;color:var(--ink2);white-space:nowrap;transform:translateX(-50%)}
.rec-tl span:first-of-type{transform:none}
.rec-tb td{height:15mm;border:1px solid var(--rule)}
.rec-tb th{border-bottom:1.5px solid var(--ink)}
'''

html = f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ICOPE 長者量六力共學講義</title>{links}
<style>[hidden]{{display:none!important}}{style}</style><style>{PRINT_CSS}</style></head>
<body class="handout"><div class="deck" id="deck">
{chr(10).join(body)}
</div>
{ui}
<script>{script}</script>
<script>{POST}</script>
</body></html>'''
(here / "handout.html").write_text(html, encoding="utf-8")
print("handout.html", len(html))
