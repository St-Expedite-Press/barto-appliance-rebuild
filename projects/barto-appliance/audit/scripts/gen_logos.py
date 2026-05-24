"""
gen_logos.py
Uses DALL-E 3 to generate logo variant images for each of the 10 Barto design
variants. Saves to audit/designs/images/logo-variant-[letter].png
"""

import os, re, urllib.request
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

OUT = os.path.join(os.path.dirname(__file__), '..', 'designs', 'images')

# Shared constraints injected into every prompt
BASE = (
    "Flat vector graphic logo design, no gradients, no shadows, no photography, "
    "no people, white background unless specified. The wordmark reads exactly: "
    "\"Barto\" (large, italic) with \"APPLIANCE\" in smaller caps below it. "
    "Clean, professional retail brand identity. Tight crop, horizontal layout. "
    "Do not add decorative flourishes unless the brief specifies them. "
    "Render text crisply and legibly."
)

VARIANTS = {
    'a': (
        "Flat vector logo for Barto Appliance. Solid teal (#004A6E) filled rectangle. "
        "White bold italic 'Barto' wordmark inside, 'APPLIANCE' in white small caps below. "
        "Minimal, polished, retail-professional. " + BASE
    ),
    'b': (
        "Flat vector logo for Barto Appliance. Solid teal (#004A6E) rectangle. "
        "White bold italic 'Barto', white 'APPLIANCE' small caps. "
        "A 4px amber/yellow (#FFC20E) horizontal rule along the bottom edge of the box. "
        "Commercial, confident. " + BASE
    ),
    'c': (
        "Flat vector logo for Barto Appliance. White rectangle with a 2px teal (#004A6E) border. "
        "Teal bold italic 'Barto' wordmark, teal 'APPLIANCE' small caps. "
        "High contrast inversion of the standard teal box. " + BASE
    ),
    'd': (
        "Wordmark-only flat vector logo for Barto Appliance — no box, no rectangle background. "
        "Teal (#004A6E) bold italic 'Barto' in a large serif italic font. "
        "'APPLIANCE' in teal small caps with wide letter-spacing beneath. "
        "White background. Minimal, newspaper editorial feel. " + BASE
    ),
    'e': (
        "Flat vector logo for Barto Appliance. Solid teal (#004A6E) rectangle. "
        "White bold italic 'Barto', white 'APPLIANCE' small caps inside box. "
        "Below the box: 'Since 1947' in amber (#FFC20E) italic small text. "
        "Most expressive full brand application. " + BASE
    ),
    'f': (
        "Dark luxury flat vector logo for Barto Appliance. Dark charcoal (#1C1C1C) rectangle. "
        "Gold/amber (#E8A520) bold italic 'Barto' wordmark. Cream (#F0EBE3) 'APPLIANCE' small caps. "
        "A faint amber glow rectangle behind the main box at low opacity. "
        "Premium, showroom, upscale retailer feel. " + BASE
    ),
    'g': (
        "Heritage editorial flat vector logo for Barto Appliance. "
        "Cream (#FAF7F2) background rectangle with a thin teal (#004A6E) border. "
        "Thin teal ornamental horizontal rule above and below the text. "
        "Teal serif italic 'Barto'. 'APPLIANCE' in teal small caps with wide tracking. "
        "New Orleans heritage, newspaper masthead aesthetic. " + BASE
    ),
    'h': (
        "Ultra-minimal modern flat vector logo for Barto Appliance. "
        "No box. 'BARTO' in bold geometric all-caps teal (#004A6E). "
        "A 3px orange (#E8871A) horizontal rule beneath 'BARTO'. "
        "'APPLIANCE' in small medium-gray caps below the rule. "
        "Pure 2025 modern, bento-grid aesthetic. " + BASE
    ),
    'i': (
        "Bold American signage flat vector logo for Barto Appliance. "
        "Full-width teal (#004A6E) rectangle. 'BARTO' in massive all-caps white bold type, centered. "
        "'APPLIANCE' in amber (#FFC20E) small caps centered below. "
        "No decorative elements. Maximum storefront impact, billboard energy. " + BASE
    ),
    'j': (
        "Coastal premium flat vector logo for Barto Appliance. "
        "Teal (#004A6E) rectangle with rounded corners (pill-ish, 8px radius). "
        "White italic 'Barto' wordmark. Amber (#FFC20E) 'APPLIANCE' small caps inside box. "
        "Warm, approachable, Gulf Coast premium feel. " + BASE
    ),
}


def generate(letter, prompt):
    import base64
    resp = client.images.generate(
        model="gpt-image-2",
        prompt=prompt,
        size="1536x1024",
        quality="high",
        n=1,
        output_format="png",
    )
    out_path = os.path.join(OUT, f'logo-variant-{letter}.png')
    # gpt-image-2 returns base64 by default
    img_data = resp.data[0].b64_json
    if img_data:
        with open(out_path, 'wb') as f:
            f.write(base64.b64decode(img_data))
    else:
        # fallback: url
        urllib.request.urlretrieve(resp.data[0].url, out_path)
    size = os.path.getsize(out_path)
    return out_path, size


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for letter, prompt in VARIANTS.items():
        out_path = os.path.join(OUT, f'logo-variant-{letter}.png')
        if os.path.exists(out_path):
            print(f'  Skipping logo-variant-{letter}.png (exists)')
            continue
        print(f'  Generating logo-variant-{letter}.png ...')
        path, size = generate(letter, prompt)
        print(f'    Saved {size:,} bytes -> {path}')
    print('Done.')
