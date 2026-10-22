#!/bin/zsh
# 產生可離線開啟／放 GitHub Pages 的 index.html（deck.html 是 Artifact 用的內容檔）
cd "${0:A:h}"
{
  print -r -- '<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'
  cat deck.html
  print -r -- '</body></html>'
} > index.html
