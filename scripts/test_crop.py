import os
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

input_path = r"C:\Users\lemon\.gemini\antigravity-ide\brain\5423af7d-f4aa-4698-b280-cdfe0ca4c2b2\.user_uploaded\media_1788594673588.png"
out_dir = r"d:\Learn\AI\02.Weeding\02._V2\public"

img = Image.open(input_path).convert("RGBA")
w, h = img.size
print(f"Original image dimensions: {w}x{h}")

# Left side crop: 
# The left floral cluster and column extends from x=0 to approximately x=290
# Right side crop:
# The right floral cluster and column extends from x=338 to x=628
left_crop = img.crop((0, 0, int(w * 0.48), h))
right_crop = img.crop((int(w * 0.52), 0, w, h))

print(f"Left crop size: {left_crop.size}, Right crop size: {right_crop.size}")
