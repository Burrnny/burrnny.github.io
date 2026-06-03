#!/usr/bin/env python3
"""Genera las páginas de invitación a sala 1v1 de Gravity Sort en 6 idiomas.
  gs/<lang>/r/index.html  · preview localizado para /gs/<lang>/r/?c=CODE
  gs/r/index.html         · fallback (español)
La app comparte el link con el idioma del que invita → WhatsApp scrapea el
OG localizado. Si el receptor tiene la app, iOS la abre vía AASA (auto-join).
Después: cd gs && python3 _build_room.py && cd .. && git add gs && git commit && git push
"""
from pathlib import Path

ROOT = Path("/Users/juancornejo/Developer/burrnny.github.io/gs")

LOCALES = {
    "es": {"lang": "es", "og_title": "⚔️ Te retan a un 1v1 · Gravity Sort", "og_desc": "Te invitaron a una partida 1 vs 1 en Gravity Sort. Toca para entrar a la sala.", "h1": "Te retan a un duelo 1v1", "code_label": "Código de sala", "open_btn": "Abrir en Gravity Sort", "dl_btn": "Descargar gratis · App Store", "ios_hint": "Si ya tienes la app, abrirá sola. Si no, descárgala y mete el código.", "desktop_hint": "Gravity Sort es para iPhone. Abre este link desde tu iPhone o anota el código.", "invalid": "Código no válido"},
    "en": {"lang": "en", "og_title": "⚔️ You've been challenged · Gravity Sort 1v1", "og_desc": "You're invited to a 1 vs 1 match in Gravity Sort. Tap to join the room.", "h1": "You've been challenged to a 1v1", "code_label": "Room code", "open_btn": "Open in Gravity Sort", "dl_btn": "Download free · App Store", "ios_hint": "If you have the app, it opens automatically. Otherwise download it and enter the code.", "desktop_hint": "Gravity Sort is iPhone-only. Open this link on your iPhone or note the code.", "invalid": "Invalid code"},
    "pt": {"lang": "pt", "og_title": "⚔️ Desafiaram-te para um 1v1 · Gravity Sort", "og_desc": "Convidaram-te para uma partida 1 vs 1 no Gravity Sort. Toca para entrar na sala.", "h1": "Desafiaram-te para um 1v1", "code_label": "Código de sala", "open_btn": "Abrir no Gravity Sort", "dl_btn": "Download grátis · App Store", "ios_hint": "Se já tens a app, abre sozinha. Caso contrário, descarrega-a e mete o código.", "desktop_hint": "Gravity Sort é para iPhone. Abre este link no teu iPhone ou anota o código.", "invalid": "Código inválido"},
    "fr": {"lang": "fr", "og_title": "⚔️ On te défie en 1c1 · Gravity Sort", "og_desc": "Tu es invité à un match 1 contre 1 dans Gravity Sort. Touche pour rejoindre le salon.", "h1": "On te défie en 1c1", "code_label": "Code du salon", "open_btn": "Ouvrir dans Gravity Sort", "dl_btn": "Télécharger gratuit · App Store", "ios_hint": "Si tu as l'app, elle s'ouvre toute seule. Sinon, télécharge-la et entre le code.", "desktop_hint": "Gravity Sort est pour iPhone. Ouvre ce lien sur ton iPhone ou note le code.", "invalid": "Code invalide"},
    "de": {"lang": "de", "og_title": "⚔️ Du wirst zum 1v1 herausgefordert · Gravity Sort", "og_desc": "Du bist zu einem 1-gegen-1-Match in Gravity Sort eingeladen. Tippe, um dem Raum beizutreten.", "h1": "Du wirst zum 1v1 herausgefordert", "code_label": "Raum-Code", "open_btn": "In Gravity Sort öffnen", "dl_btn": "Kostenlos laden · App Store", "ios_hint": "Wenn du die App hast, öffnet sie sich automatisch. Sonst lade sie und gib den Code ein.", "desktop_hint": "Gravity Sort ist für iPhone. Öffne diesen Link auf deinem iPhone oder notiere den Code.", "invalid": "Ungültiger Code"},
    "ja": {"lang": "ja", "og_title": "⚔️ 1v1の挑戦状 · Gravity Sort", "og_desc": "Gravity Sortの1対1マッチに招待されました。タップしてルームに参加。", "h1": "1v1に挑戦されました", "code_label": "ルームコード", "open_btn": "Gravity Sortで開く", "dl_btn": "無料ダウンロード · App Store", "ios_hint": "アプリがあれば自動で開きます。なければダウンロードしてコードを入力。", "desktop_hint": "Gravity SortはiPhone専用です。iPhoneでこのリンクを開くか、コードをメモしてください。", "invalid": "無効なコード"},
}

TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<meta name="theme-color" content="#0e1140">
<title>{og_title}</title>
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:image" content="https://burrnny.com/gs/og-{lang}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Gravity Sort">
<meta property="og:locale" content="{lang}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="https://burrnny.com/gs/og-{lang}.png">
<meta name="apple-itunes-app" content="app-id=6767609526">
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: linear-gradient(180deg, #0e1140, #1a1052); color: #fff;
    min-height: 100vh; margin: 0; display: flex; align-items: center;
    justify-content: center; text-align: center; padding: 20px; }}
  .card {{ max-width: 380px; width: 100%; padding: 36px 24px;
    background: rgba(255,255,255,0.06); border-radius: 26px;
    backdrop-filter: blur(20px); }}
  .brand {{ font-size: 13px; letter-spacing: 2px; opacity: 0.6; font-weight: 700; }}
  h1 {{ font-size: 26px; margin: 10px 0 4px; font-weight: 800;
    background: linear-gradient(90deg, #ff6ad5, #6ad8ff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
  .code-card {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px; padding: 22px 12px; margin: 24px 0; }}
  .code-label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1.4px; opacity: 0.55; margin-bottom: 8px; }}
  .code {{ font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 34px; font-weight: 700; letter-spacing: 6px; }}
  .btn {{ display: block; width: 100%; padding: 15px; border-radius: 14px; text-decoration: none;
    font-size: 16px; font-weight: 700; margin: 10px 0; }}
  .btn-primary {{ background: #fff; color: #0e1140; }}
  .btn-secondary {{ background: rgba(255,255,255,0.10); color: #fff; border: 1px solid rgba(255,255,255,0.18); }}
  .hint {{ opacity: 0.6; font-size: 13px; line-height: 1.5; margin-top: 18px; }}
</style>
</head>
<body>
<div class="card">
  <div class="brand">GRAVITY SORT</div>
  <h1>{h1}</h1>
  <div class="code-card" id="codeCard" style="display:none">
    <div class="code-label">{code_label}</div>
    <div class="code" id="codeValue">——————</div>
  </div>
  <a id="openBtn" class="btn btn-primary" href="#">{open_btn}</a>
  <a class="btn btn-secondary" href="https://apps.apple.com/app/id6767609526">{dl_btn}</a>
  <p class="hint" id="iosHint" style="display:none">{ios_hint}</p>
  <p class="hint" id="desktopHint" style="display:none">{desktop_hint}</p>
</div>
<script>
(function(){{
  var code = (new URLSearchParams(window.location.search).get('c') || '').toUpperCase().replace(/[^A-Z0-9]/g,'');
  if (!/^[A-Z0-9]{{4,8}}$/.test(code)) {{
    document.getElementById('openBtn').style.display='none';
    document.querySelector('h1').textContent = '{invalid}';
    return;
  }}
  document.getElementById('codeCard').style.display='block';
  document.getElementById('codeValue').textContent = code;
  // Custom scheme: abre la app DIRECTO en la sala 1v1. Es más fiable que el
  // universal link cuando ya estás en el navegador (same-domain no lo abre).
  var appLink = 'gravitysort://r/' + code;
  document.getElementById('openBtn').href = appLink;
  var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform==='MacIntel' && navigator.maxTouchPoints>1);
  document.getElementById(isIOS ? 'iosHint' : 'desktopHint').style.display='block';
  if (isIOS) {{
    // Auto-abre la app; si no está instalada, cae al App Store tras 1.6s.
    var t = setTimeout(function(){{ window.location.href = 'https://apps.apple.com/app/id6767609526'; }}, 1600);
    window.addEventListener('pagehide', function(){{ clearTimeout(t); }});
    window.location.href = appLink;
  }} else {{
    document.getElementById('openBtn').style.display='none';
  }}
}})();
</script>
</body>
</html>
"""


def main():
    for lang, data in LOCALES.items():
        html = TEMPLATE.format(apath=f"/gs/{lang}/r/", **data)
        target = ROOT / lang / "r" / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print(f"  ✓ {target.relative_to(ROOT)}")
    # Fallback en /gs/r/ (español)
    html = TEMPLATE.format(apath="/gs/r/", **LOCALES["es"])
    (ROOT / "r").mkdir(parents=True, exist_ok=True)
    (ROOT / "r" / "index.html").write_text(html, encoding="utf-8")
    print("  ✓ r/index.html")


if __name__ == "__main__":
    main()
