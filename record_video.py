"""
Record the smooth-pan poster presentation as MP4.
Steps the JS animation forward frame-by-frame.

Usage:
  python3 record_video.py

Reads presentation.html, outputs presentation_video.mp4.
Update poster content in presentation.html before running.

NOTE: This produces a SILENT video. For the actual submission,
record with QuickTime + microphone for live voice narration.
This script is useful for producing a reference/practice video.
"""

import os
import shutil
import subprocess
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
FRAME_DIR = os.path.join(ROOT, "_frames")
OUT_FILE = os.path.join(ROOT, "presentation_video.mp4")
HTML_FILE = "file://" + os.path.join(ROOT, "presentation.html")
FPS = 15
DURATION = 181
W, H = 1920, 1080

if os.path.exists(FRAME_DIR):
    shutil.rmtree(FRAME_DIR)
os.makedirs(FRAME_DIR)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument(f"--window-size={W},{H}")
opts.add_argument("--force-device-scale-factor=1")
opts.add_argument("--force-color-profile=srgb")
opts.add_argument("--hide-scrollbars")

driver = webdriver.Chrome(options=opts)
driver.set_window_size(W, H)

dt = 1.0 / FPS
total_frames = int(DURATION * FPS)

try:
    print(f"Loading presentation ({W}x{H}, {FPS}fps, {DURATION}s = {total_frames} frames)...")
    driver.get(HTML_FILE)
    time.sleep(5)  # Extra time for Google Fonts to load

    driver.execute_script("""
        document.getElementById('teleprompter').style.display = 'none';
        document.getElementById('hud').style.display = 'none';
        pausedAt = 0;
        applyCamera(lerpCam(0));
    """)
    time.sleep(0.5)

    print("Capturing frames...")
    for i in range(total_frames):
        driver.save_screenshot(os.path.join(FRAME_DIR, f"f_{i:06d}.png"))
        driver.execute_script(f"advanceFrame({dt})")

        if i % (FPS * 5) == 0:
            t = i / FPS
            pct = (i / total_frames) * 100
            print(f"  {t:.0f}s / {DURATION}s  ({pct:.0f}%)  [{i}/{total_frames} frames]")

    print(f"\nCaptured {total_frames} frames")

finally:
    driver.quit()

print("Encoding video...")
subprocess.run([
    "ffmpeg", "-y",
    "-framerate", str(FPS),
    "-start_number", "0",
    "-i", os.path.join(FRAME_DIR, "f_%06d.png"),
    "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2",
    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
    OUT_FILE,
], check=True, capture_output=True)

size_mb = os.path.getsize(OUT_FILE) / (1024 * 1024)
print(f"Saved: {OUT_FILE} ({DURATION}s, {size_mb:.1f} MB)")

shutil.rmtree(FRAME_DIR, ignore_errors=True)
print("Done.")
