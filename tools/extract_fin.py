# Finale extraction — the footer reference itself becomes the layer stack:
#   public/fin/man.png    the smoking man, matted out of the artwork (his
#                         grade, rim and pose are the reference's own pixels)
#   public/fin/plate.jpg  everything else — the giant wordmark, the red fog,
#                         his cigarette smoke — with the man diffusion-filled
#                         away and the baked captions blanked (they return as
#                         live DOM so they can type themselves in)
#   public/fin/fin.json   the man's box, for placement
#
# The man and the plate are cover-fitted with the SAME mapping on the site,
# so at rest the reassembly is pixel-identical to the reference; splitting
# him out is what buys the reveal and the parallax depth.

import json
import os

import cv2
import numpy as np
from PIL import Image
from rembg import new_session, remove

SRC = os.path.join(os.path.dirname(__file__), "..", "Footer image.jpg")
OUT = os.path.join(os.path.dirname(__file__), "..", "public", "fin")
os.makedirs(OUT, exist_ok=True)

img = cv2.imread(SRC)
H, W = img.shape[:2]
assert (W, H) == (1600, 900), f"unexpected reference size {W}x{H}"

BOX = (580, 50, 1030, 900)          # x0, y0, x1, y1

# caption zones that become live DOM (incl. their red rules and dashes)
LABELS = [
    (36, 50, 235, 170),      # IDEAS / DESIGNS / EXPERIENCES / REAL IMPACT
    (36, 330, 235, 495),     # the quote + its dash
    (36, 730, 190, 840),     # A / DESIGNER'S / WORLD
    (1450, 50, 1580, 175),   # SAME / PASSION / A BRIGHTER / TOMORROW
    (1450, 730, 1580, 830),  # DESIGN / BUILD / EXPLORE / REPEAT
]

x0, y0, x1, y1 = BOX

# The suit is nearly the same dark red-black as the letters/fog behind it,
# so colour-based cutting (GrabCut) can't tell them apart. A trained person
# segmentation model doesn't care about colour, only "is this a person", so
# it cuts a clean silhouette regardless of what's printed behind him.
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
session = new_session("u2net_human_seg")
seg = remove(Image.fromarray(rgb), session=session, only_mask=True)
alpha = np.array(seg)  # single-channel mask, 0..255
_, alpha = cv2.threshold(alpha, 20, 255, cv2.THRESH_BINARY)
alpha = cv2.morphologyEx(alpha, cv2.MORPH_CLOSE,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
alpha = cv2.GaussianBlur(alpha, (5, 5), 0)
alpha[:y0, :] = 0
alpha[:, :x0] = 0
alpha[:, x1:] = 0

pa = alpha[y0:, x0:x1]
pc = img[y0:, x0:x1]
# mild pre-sharpen against the cover fit's upscale on large displays
pc = cv2.addWeighted(pc, 1.30, cv2.GaussianBlur(pc, (0, 0), 1.1), -0.30, 0)
cv2.imwrite(os.path.join(OUT, "man.png"), np.dstack([pc, pa]))
print("man alpha px:", int((pa > 128).sum()))

# ---- the plate -------------------------------------------------------------
plate = img.copy()
remove = cv2.dilate(alpha, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
for lx0, ly0, lx1, ly1 in LABELS:
    remove[ly0:ly1, lx0:lx1] = 255
remove = cv2.dilate(remove, np.ones((5, 5), np.uint8))

m = remove.astype(np.float32) / 255.0
out = plate.astype(np.float32)
keepm = (1.0 - m)[..., None]


def nconv(sig):
    wgt = cv2.GaussianBlur(1.0 - m, (0, 0), sig)
    val = cv2.GaussianBlur(out * keepm, (0, 0), sig)
    return val / np.maximum(wgt, 1e-4)[..., None], wgt


coarse, _wc = nconv(75)
fine, wf = nconv(17)
blend = np.clip(wf * 8.0, 0.0, 1.0)[..., None]
diff = fine * blend + coarse * (1.0 - blend)
out = out * keepm + diff * m[..., None]
noise = np.random.default_rng(3).normal(0, 2.0, out.shape).astype(np.float32)
plate = np.clip(out + noise * m[..., None], 0, 255).astype(np.uint8)

cv2.imwrite(os.path.join(OUT, "plate.jpg"), plate,
            [cv2.IMWRITE_JPEG_QUALITY, 90])

with open(os.path.join(OUT, "fin.json"), "w") as f:
    json.dump({"man": [x0, y0, x1 - x0, H - y0], "size": [W, H]}, f)

sizes = {f: os.path.getsize(os.path.join(OUT, f)) // 1024
         for f in sorted(os.listdir(OUT))}
print(json.dumps(sizes, indent=0))
