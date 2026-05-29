#!/usr/bin/env python3
"""Genera los HTML de preview de Gravity Sort en 6 idiomas.
Estructura producida:
  gs/<lang>/c/index.html  · sirve para /gs/<lang>/c/ y /gs/<lang>/c/?id=N
  gs/<lang>/index.html    · sirve para /gs/<lang>/ y /gs/<lang>/?id=N

Después de correr este script, hacer: git add gs/{es,en,pt,fr,de,ja}/ && git push
"""
from pathlib import Path

ROOT = Path("/Users/juancornejo/Developer/burrnny.github.io/gs")

LOCALES = {
    "es": {
        "html_lang": "es",
        "og_title": "Gravity Sort — ¿Puedes superar este reto? 🧪",
        "og_desc": "Ordena los líquidos por color hasta que cada tubo tenga uno solo. Parece simple… hasta que llegan los modificadores. 420 niveles. Descarga gratis.",
        "og_alt": "Gravity Sort — puzzle de ordenar líquidos por color",
        "page_title": "Gravity Sort — Abrir reto",
        "meta_desc": "Ordena los líquidos por color. 420 niveles, 21 mundos. Descarga gratis.",
        "card_text": "Abriendo el reto en la App Store…",
        "btn_text": "Descargar gratis",
        "footer_text": "Si ya tienes la app, iOS la abre automáticamente.",
    },
    "en": {
        "html_lang": "en",
        "og_title": "Gravity Sort — Can you beat this challenge? 🧪",
        "og_desc": "Sort liquids by color until each tube has only one. Sounds simple… until the modifiers show up. 420 levels. Free download.",
        "og_alt": "Gravity Sort — sort liquids by color puzzle",
        "page_title": "Gravity Sort — Open challenge",
        "meta_desc": "Sort liquids by color. 420 levels, 21 worlds. Free download.",
        "card_text": "Opening challenge in the App Store…",
        "btn_text": "Download free",
        "footer_text": "If you already have the app, iOS opens it automatically.",
    },
    "pt": {
        "html_lang": "pt",
        "og_title": "Gravity Sort — Consegues vencer este desafio? 🧪",
        "og_desc": "Ordena os líquidos por cor até cada tubo ter uma só. Parece simples… até chegarem os modificadores. 420 níveis. Download grátis.",
        "og_alt": "Gravity Sort — puzzle de ordenar líquidos por cor",
        "page_title": "Gravity Sort — Abrir desafio",
        "meta_desc": "Ordena os líquidos por cor. 420 níveis, 21 mundos. Download grátis.",
        "card_text": "A abrir o desafio na App Store…",
        "btn_text": "Download grátis",
        "footer_text": "Se já tens a app, o iOS abre-a automaticamente.",
    },
    "fr": {
        "html_lang": "fr",
        "og_title": "Gravity Sort — Peux-tu relever ce défi ? 🧪",
        "og_desc": "Trie les liquides par couleur jusqu'à ce que chaque tube n'en contienne qu'une. Simple… jusqu'à l'arrivée des modificateurs. 420 niveaux. Téléchargement gratuit.",
        "og_alt": "Gravity Sort — puzzle de tri de liquides par couleur",
        "page_title": "Gravity Sort — Ouvrir le défi",
        "meta_desc": "Trie les liquides par couleur. 420 niveaux, 21 mondes. Téléchargement gratuit.",
        "card_text": "Ouverture du défi dans l'App Store…",
        "btn_text": "Télécharger gratuitement",
        "footer_text": "Si tu as déjà l'app, iOS l'ouvre automatiquement.",
    },
    "de": {
        "html_lang": "de",
        "og_title": "Gravity Sort — Schaffst du diese Herausforderung? 🧪",
        "og_desc": "Sortiere Flüssigkeiten nach Farbe, bis jede Röhre nur eine enthält. Klingt einfach… bis die Modifikatoren auftauchen. 420 Level. Gratis-Download.",
        "og_alt": "Gravity Sort — Puzzle zum Sortieren von Flüssigkeiten nach Farbe",
        "page_title": "Gravity Sort — Herausforderung öffnen",
        "meta_desc": "Sortiere Flüssigkeiten nach Farbe. 420 Level, 21 Welten. Gratis-Download.",
        "card_text": "Herausforderung wird im App Store geöffnet…",
        "btn_text": "Gratis herunterladen",
        "footer_text": "Wenn du die App schon hast, öffnet iOS sie automatisch.",
    },
    "ja": {
        "html_lang": "ja",
        "og_title": "Gravity Sort — このチャレンジに挑戦できる？🧪",
        "og_desc": "色ごとに液体を整理し、各チューブを1色にしよう。シンプルに見えても…モディファイアが登場すると別物。420レベル、無料ダウンロード。",
        "og_alt": "Gravity Sort — 色で液体を整理するパズル",
        "page_title": "Gravity Sort — チャレンジを開く",
        "meta_desc": "色ごとに液体を整理。420レベル、21ワールド。無料ダウンロード。",
        "card_text": "App Storeでチャレンジを開いています…",
        "btn_text": "無料ダウンロード",
        "footer_text": "アプリが既にあれば、iOSが自動的に開きます。",
    },
}

TEMPLATE = """<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<!-- OPEN GRAPH / TWITTER CARD ({html_lang}) -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Gravity Sort">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:image" content="https://burrnny.com/gs/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_alt}">
<meta property="og:url" content="https://burrnny.com/gs/{html_lang}/">
<meta property="og:locale" content="{html_lang}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="https://burrnny.com/gs/og.png">
<title>{page_title}</title>
<meta name="description" content="{meta_desc}">
<meta name="apple-itunes-app" content="app-id=6767609526">
<!-- Redirect solo para humanos sin JS -->
<noscript>
  <meta http-equiv="refresh" content="0; url=https://apps.apple.com/app/id6767609526">
</noscript>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif;
         background: linear-gradient(180deg, #0e1140, #1a1052);
         color: #fff; min-height: 100vh; margin: 0;
         display: flex; align-items: center; justify-content: center;
         text-align: center; padding: 20px; }}
  .card {{ max-width: 360px; padding: 32px 24px;
          background: rgba(255,255,255,0.06); border-radius: 24px;
          backdrop-filter: blur(20px); }}
  .icon {{ font-size: 64px; margin-bottom: 16px; }}
  h1 {{ font-size: 28px; margin: 8px 0; font-weight: 800;
       background: linear-gradient(90deg, #ff6ad5, #6ad8ff);
       -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
  p {{ opacity: 0.85; line-height: 1.5; margin: 12px 0 24px; }}
  a.btn {{ display: inline-block; padding: 14px 28px; border-radius: 999px;
          background: #fff; color: #000; text-decoration: none;
          font-weight: 700; font-size: 16px; }}
  small {{ display: block; margin-top: 20px; opacity: 0.55; font-size: 12px; }}
</style>
</head>
<body>
<div class="card">
  <div class="icon">💧</div>
  <h1>Gravity Sort</h1>
  <p>{card_text}</p>
  <a class="btn" href="https://apps.apple.com/app/id6767609526">{btn_text}</a>
  <small>{footer_text}</small>
</div>
<script>
  setTimeout(function(){{
    window.location.href = "https://apps.apple.com/app/id6767609526";
  }}, 600);
</script>
</body>
</html>
"""


def main():
    for lang, data in LOCALES.items():
        html = TEMPLATE.format(**data)
        # Crear /gs/<lang>/index.html y /gs/<lang>/c/index.html
        for sub in ["", "c/"]:
            target = ROOT / lang / sub / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(html, encoding="utf-8")
            print(f"  ✓ {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
