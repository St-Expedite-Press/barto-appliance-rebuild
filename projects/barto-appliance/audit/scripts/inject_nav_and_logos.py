"""
inject_nav_and_logos.py
1. Injects a floating variant navigator into every homepage variant HTML file.
2. Replaces the generic barto-logo.png reference with the variant-specific logo image.
Idempotent — safe to re-run.
"""

import re, os

BASE = os.path.join(os.path.dirname(__file__), '..', 'designs')

VARIANTS = [
    ('barto-homepage.html',            'a', 'A — Teal Split'),
    ('variant-b-navy-brass.html',      'b', 'B — Full-Width'),
    ('variant-c-slate-rust.html',      'c', 'C — Inverted Split'),
    ('variant-d-editorial-white.html', 'd', 'D — Editorial'),
    ('variant-e-brand-true.html',      'e', 'E — Brand True'),
    ('variant-f-dark-luxury.html',     'f', 'F — Dark Luxury'),
    ('variant-g-heritage-editorial.html', 'g', 'G — Heritage'),
    ('variant-h-bento-modern.html',    'h', 'H — Bento Modern'),
    ('variant-i-bold-signage.html',    'i', 'I — Bold Signage'),
    ('variant-j-coastal-premium.html', 'j', 'J — Coastal Premium'),
]

NAV_JS_FILES = ',\n    '.join(
    f"{{f:'{v[0]}',l:'{v[2]}'}}" for v in VARIANTS
)

NAV_HTML = f"""
<!-- ═══ VARIANT NAVIGATOR ═══ -->
<style>
#vnav {{
  position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%);
  background: #003256; border-radius: 100px;
  padding: 10px 20px; display: flex; align-items: center; gap: 16px;
  box-shadow: 0 8px 40px rgba(0,50,86,0.55); z-index: 99999;
  font-family: 'DM Sans', system-ui, sans-serif; white-space: nowrap;
  user-select: none;
}}
#vnav button {{
  background: none; border: none; color: #FFC20E;
  font-size: 20px; cursor: pointer; padding: 0; line-height: 1;
  transition: transform 0.1s;
}}
#vnav button:hover {{ transform: scale(1.2); }}
#vnav-label {{
  color: #ffffff; font-size: 12px; font-weight: 700;
  letter-spacing: 0.09em; text-transform: uppercase;
  min-width: 180px; text-align: center;
}}
#vnav-dot {{
  width: 6px; height: 6px; border-radius: 50%;
  background: #FFC20E; flex-shrink: 0;
}}
#vnav a {{
  color: rgba(255,255,255,0.45); font-size: 11px; font-weight: 600;
  text-decoration: none; letter-spacing: 0.06em;
  border-left: 1px solid rgba(255,255,255,0.18); padding-left: 16px;
  transition: color 0.15s;
}}
#vnav a:hover {{ color: rgba(255,255,255,0.9); }}
</style>
<div id="vnav">
  <button id="vnav-prev" title="Previous variant">&#8592;</button>
  <div id="vnav-dot"></div>
  <span id="vnav-label">Loading...</span>
  <div id="vnav-dot"></div>
  <button id="vnav-next" title="Next variant">&#8594;</button>
  <a href="design-system-docs.html">DOCS</a>
</div>
<script>
(function(){{
  var V=[
    {NAV_JS_FILES}
  ];
  var cur=window.location.pathname.split('/').pop()||V[0].f;
  var idx=V.findIndex(function(v){{return v.f===cur;}});
  if(idx<0)idx=0;
  document.getElementById('vnav-label').textContent=V[idx].l;
  document.getElementById('vnav-prev').onclick=function(){{
    window.location.href=V[(idx-1+V.length)%V.length].f;
  }};
  document.getElementById('vnav-next').onclick=function(){{
    window.location.href=V[(idx+1)%V.length].f;
  }};
}})();
</script>
<!-- ═══ END VARIANT NAVIGATOR ═══ -->
"""

LOGO_IMG_RE = re.compile(
    r'<img\s+src=["\']images/(?:barto-logo\.png|logo-variant-[a-j]\.png)["\'][^>]*>',
    re.IGNORECASE
)


def make_logo_tag(letter, height='44px'):
    return (
        f'<img src="images/logo-variant-{letter}.png" '
        f'alt="Barto Appliance" '
        f'style="height:{height}; width:auto; display:block;">'
    )


def inject(html, letter):
    # 1. Replace navigator if already present, else append before </body>
    html = re.sub(
        r'<!-- ═══ VARIANT NAVIGATOR ═══ -->[\s\S]*?<!-- ═══ END VARIANT NAVIGATOR ═══ -->',
        '',
        html
    )
    html = html.replace('</body>', NAV_HTML + '\n</body>', 1)

    # 2. Replace logo images — first occurrence (header) stays 44px, rest 36px
    occurrences = list(LOGO_IMG_RE.finditer(html))
    if not occurrences:
        return html

    # Replace from last to first so positions don't shift
    for i, m in enumerate(reversed(occurrences)):
        height = '44px' if (len(occurrences) - 1 - i) == 0 else '36px'
        new_tag = make_logo_tag(letter, height)
        html = html[:m.start()] + new_tag + html[m.end():]

    return html


if __name__ == '__main__':
    print('Injecting navigator and logos...')
    for filename, letter, label in VARIANTS:
        path = os.path.join(BASE, filename)
        if not os.path.exists(path):
            print(f'  MISSING {filename} - skipping')
            continue
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = inject(html, letter)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  OK {filename}')
    print('Done.')
