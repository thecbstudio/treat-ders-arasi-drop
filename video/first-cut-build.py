"""Sunum videosu: python -X utf8 build.py [cek]  ('cek' = site karelerini yeniden çek)"""
import os, sys, subprocess, shutil, glob
from PIL import Image, ImageDraw, ImageFont

H = os.path.dirname(os.path.abspath(__file__))
os.chdir(H)
W, HH, FPS = 1920, 1080, 30
SITE = "https://treat-ders-arasi-drop.netlify.app"
INK, PAPER, CORAL, YEL = "#21312d", "#f9f6ee", "#ff6b4a", "#ffe55f"
F = "C:/Windows/Fonts/"
def font(n, s): return ImageFont.truetype(F + n, s)
SERIF, SANS, SANSB, MONO = "georgiab.ttf", "segoeui.ttf", "segoeuib.ttf", "consola.ttf"

def run(a): subprocess.run(a, check=True)
def enc(args, out):
    run(["ffmpeg", "-v", "error", "-y"] + args + ["-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-an", out])

def card(name, dur, eyebrow, lines, sub="", bg=PAPER, fg=INK, accent=CORAL):
    im = Image.new("RGB", (W, HH), bg); d = ImageDraw.Draw(im)
    d.ellipse((W - 420, -220, W + 160, 360), fill=accent if bg != CORAL else YEL)
    d.text((140, 190), eyebrow.upper(), font=font(MONO, 30), fill=fg)
    y = 290
    for t in lines:
        col = accent if t.startswith("*") else fg
        d.text((136, y), t.lstrip("*"), font=font(SERIF, 104), fill=col); y += 128
    if sub: d.text((140, y + 40), sub, font=font(SANS, 44), fill=fg)
    d.text((140, HH - 110), "treat  ×  Manus  ·  Istanbul Ignited by Slush’D  ·  12 Oct 2026", font=font(MONO, 26), fill=fg)
    im.save(name + ".png"); enc(["-loop", "1", "-t", str(dur), "-i", name + ".png"], name + ".mp4")

def cap_png(name, big, small=""):
    im = Image.new("RGBA", (W, HH), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle((0, HH - 190, W, HH), fill=(33, 49, 45, 240))
    d.rectangle((0, HH - 190, 16, HH), fill=CORAL)
    d.text((70, HH - 165), big, font=font(SANSB, 54), fill="#ffffff")
    if small: d.text((72, HH - 88), small, font=font(SANS, 34), fill=YEL)
    im.save(name + "_cap.png")

def clip(name, src, ss, t, speed, big, small=""):
    cap_png(name, big, small)
    vf = f"[0:v]setpts=PTS/{speed},scale={W}:{HH - 190}:force_original_aspect_ratio=decrease,pad={W}:{HH}:(ow-iw)/2:0:color={PAPER.replace('#', '0x')}[v];[v][1:v]overlay=0:0"
    enc(["-ss", str(ss), "-t", str(t * speed), "-i", src, "-i", name + "_cap.png", "-filter_complex", vf], name + ".mp4")

def frames(name, d, big, small=""):
    cap_png(name, big, small)
    enc(["-framerate", str(FPS), "-i", f"{d}/%04d.jpg", "-i", name + "_cap.png", "-filter_complex", f"[0:v]scale={W}:{HH - 190},pad={W}:{HH}:0:0[v];[v][1:v]overlay=0:0"], name + ".mp4")

def cek():
    from playwright.sync_api import sync_playwright
    def shots(page, d, plan):
        shutil.rmtree(d, ignore_errors=True); os.makedirs(d); n = 0
        y = 0
        for target, move, hold in plan:
            ty = page.evaluate("(s)=>{const e=document.querySelector(s);return e?Math.max(0,e.getBoundingClientRect().top+scrollY-40):0}", target) if isinstance(target, str) else target
            for i in range(1, move + 1):
                k = i / move; k = k * k * (3 - 2 * k)
                page.evaluate("(v)=>scrollTo(0,v)", y + (ty - y) * k)
                page.screenshot(path=f"{d}/{n:04d}.jpg", type="jpeg", quality=88); n += 1
            y = ty
            for i in range(hold):
                page.screenshot(path=f"{d}/{n:04d}.jpg", type="jpeg", quality=88); n += 1
        print(d, n)
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome", headless=True)
        pg = b.new_page(viewport={"width": 1280, "height": 593}, device_scale_factor=1.5)
        pg.add_style_tag  # noqa
        pg.goto(SITE + "/", wait_until="networkidle"); pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        shots(pg, "f_site", [(0, 1, 45), ("#built", 30, 75), ("#proof", 30, 60), (".decision-table-wrap", 25, 60)])
        pg.goto(SITE + "/tracker/", wait_until="networkidle"); shots(pg, "f_tracker", [(0, 1, 90)])
        m = b.new_page(viewport={"width": 412, "height": 860}, device_scale_factor=2)
        m.goto(SITE + "/tr/?cafe=glane-coffee", wait_until="networkidle"); m.add_style_tag(content="html{scroll-behavior:auto!important}")
        shots(m, "f_mob_raw", [(0, 1, 30), ("#cafe-brief", 30, 75)])
        b.close()
    # telefon karelerini 1920x890 sahneye yerleştir (yanında QR)
    shutil.rmtree("f_mob", ignore_errors=True); os.makedirs("f_mob")
    qr = Image.open("../site/qr/glane-coffee.png").convert("RGB").resize((420, 420))
    for f in sorted(glob.glob("f_mob_raw/*.jpg")):
        bg = Image.new("RGB", (1920, 890), "#e8dfff"); d = ImageDraw.Draw(bg)
        ph = Image.open(f).resize((384, 802))
        d.rounded_rectangle((560, 28, 560 + 408, 28 + 826), 34, fill=INK); bg.paste(ph, (572, 40))
        bg.paste(qr, (1130, 150)); d.rectangle((1130, 150, 1550, 570), outline=INK, width=4)
        d.text((1130, 600), "One page + one QR per café", font=font(SANSB, 40), fill=INK)
        d.text((1130, 660), "/tr/?cafe=glane-coffee", font=font(MONO, 30), fill=INK)
        bg.save("f_mob/" + os.path.basename(f), quality=88)

if "cek" in sys.argv or not os.path.isdir("f_site"): cek()

segs = []
def add(n): segs.append(n + ".mp4")

card("s01", 3.0, "Hackathon build · Manus track", ["treat had an app.", "*It had zero cafés."], "Three students. No marketing team. No budget."); add("s01")
clip("s02", "m1_x20.mp4", 14, 7, 5, "Manus + Apify: 184 cafés, 3,290 reviews", "Scraped, read and scored in 13 minutes · one prompt"); add("s02")
frames("s03", "f_site", "Manus built the launch kit: offers, pages, content plan", "Generic offer vs. an offer built on each café’s own reviews"); add("s03")
frames("s04", "f_mob", "Every café gets its own page", "Its name, its own customer quote, its own proposed drop"); add("s04")
if os.path.exists("fal_ad.mp4"):
    clip("s05", "fal_ad.mp4", 0, 4, 1, "Campaign visual and video ad: fal.ai", "FLUX 1.1 Pro Ultra + Kling image-to-video"); add("s05")
for i, f in enumerate(sorted(glob.glob("saha/*.mp4"))[:4]):
    n = f"s06_{i}"; clip(n, f, 0, 4, 1, "Then we walked in", "Real cafés, same day · answers logged as they were"); add(n)
frames("s07", "f_tracker", "Live pipeline: found → scored → offer → sent → reply", "Only stages that really happened are ticked"); add("s07")
card("s08", 4.0, "Before → after", ["1 café per hour by hand.", "*5 personal offers in 29.5 min."], "Next campus: one prompt.  treat-ders-arasi-drop.netlify.app", bg=INK, fg="#ffffff", accent=CORAL); add("s08")

open("list.txt", "w").write("".join(f"file '{s}'\n" for s in segs))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "sessiz.mp4"])
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", "sessiz.mp4"], capture_output=True, text=True).stdout)
mz = os.path.join(H, "..", "..", "treat-video", "proje", "assets", "muzik.mp3")
out = "treat-manus-sunum.mp4"
if os.path.exists(mz):
    run(["ffmpeg", "-v", "error", "-y", "-i", "sessiz.mp4", "-i", mz, "-filter_complex", f"[1:a]volume=0.35,afade=t=in:d=1,afade=t=out:st={dur - 2:.2f}:d=2[a]", "-map", "0:v", "-map", "[a]", "-t", f"{dur:.2f}", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", out])
else:
    shutil.copy("sessiz.mp4", out)
print("sure", round(dur, 1), "sn ·", segs)
