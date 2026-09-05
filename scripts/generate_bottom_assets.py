import os
import io
import base64
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def generate_assets():
    input_path = r"C:\Users\lemon\.gemini\antigravity-ide\brain\5423af7d-f4aa-4698-b280-cdfe0ca4c2b2\.user_uploaded\media_1788594673588.png"
    public_dir = r"d:\Learn\AI\02.Weeding\02._V2\public"
    os.makedirs(public_dir, exist_ok=True)

    img = Image.open(input_path).convert("RGBA")
    orig_w, orig_h = img.size
    print(f"Original: {orig_w}x{orig_h}")

    # Scale factor for crisp retina resolution
    scale = 3

    # ==========================================
    # 1. LEFT SIDE ASSET
    # ==========================================
    # Crop left half with slight overlap (0 to 52% of width)
    w_crop_l = int(orig_w * 0.52)
    left_raw = img.crop((0, 0, w_crop_l, orig_h))
    
    w_l = w_crop_l * scale
    h_l = orig_h * scale
    left_scaled = left_raw.resize((w_l, h_l), Image.Resampling.LANCZOS)
    # Subtle unsharp mask for petal definition
    left_scaled = left_scaled.filter(ImageFilter.UnsharpMask(radius=1.5, percent=125, threshold=2))

    # Mask for left side
    mask_l = Image.new('L', (w_l, h_l), 0)
    draw_l = ImageDraw.Draw(mask_l)

    # Base polygon boundary on unscaled coordinates
    pts_l = [
        (0, 0),
        (225, 0),       # top edge of upper floral mound
        (250, 40),      # soft edge of sunlight
        (275, 100),     # edge of second mound into aisle
        (295, 160),     # edge of foreground mound into aisle
        (w_crop_l, 210),# aisle floor
        (w_crop_l, orig_h),
        (0, orig_h),
    ]
    draw_l.polygon([(x * scale, y * scale) for x, y in pts_l], fill=255)

    arr_l = np.array(mask_l, dtype=np.float32)
    # Smooth gradient fade on right side towards aisle center
    fade_start_xl = int(w_l * 0.56)
    for y in range(h_l):
        for x in range(fade_start_xl, w_l):
            fade = 1.0 - (x - fade_start_xl) / (w_l - fade_start_xl)
            arr_l[y, x] = arr_l[y, x] * max(0.0, float(fade ** 1.25))

    # Soft fade at the top boundary so columns and flowers emerge seamlessly
    top_fade_hl = int(32 * scale)
    for y in range(top_fade_hl):
        fade_y = (y / top_fade_hl) ** 1.4
        arr_l[y, :] *= fade_y

    # Soft Gaussian blur on mask edge for natural organic blend
    mask_l_final = Image.fromarray(np.uint8(np.clip(arr_l, 0, 255))).filter(ImageFilter.GaussianBlur(radius=scale * 2.0))
    left_scaled.putalpha(mask_l_final)

    # Save PNG
    left_png_path = os.path.join(public_dir, "wedding_bottom_left.png")
    left_scaled.save(left_png_path, format="PNG", optimize=True)
    print(f"Saved: {left_png_path} ({left_scaled.size})")

    # Encode to Base64 for self-contained SVG
    buffered_l = io.BytesIO()
    left_scaled.save(buffered_l, format="PNG", optimize=True)
    left_b64 = base64.b64encode(buffered_l.getvalue()).decode("ascii")

    # Generate Left SVG
    svg_left_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w_l} {h_l}" width="100%" height="100%" preserveAspectRatio="xMinYMax meet">
  <defs>
    <filter id="shadow-left" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="-4" stdDeviation="12" flood-color="#8c5848" flood-opacity="0.22" />
    </filter>
  </defs>
  <g filter="url(#shadow-left)">
    <image href="data:image/png;base64,{left_b64}" width="{w_l}" height="{h_l}" x="0" y="0" />
  </g>
</svg>
'''
    left_svg_path = os.path.join(public_dir, "wedding_bottom_left.svg")
    with open(left_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_left_content)
    print(f"Saved: {left_svg_path}")

    # ==========================================
    # 2. RIGHT SIDE ASSET
    # ==========================================
    # Crop right half with slight overlap (48% of width to end)
    x_crop_r = int(orig_w * 0.48)
    w_crop_r = orig_w - x_crop_r
    right_raw = img.crop((x_crop_r, 0, orig_w, orig_h))

    w_r = w_crop_r * scale
    h_r = orig_h * scale
    right_scaled = right_raw.resize((w_r, h_r), Image.Resampling.LANCZOS)
    right_scaled = right_scaled.filter(ImageFilter.UnsharpMask(radius=1.5, percent=125, threshold=2))

    # Mask for right side
    mask_r = Image.new('L', (w_r, h_r), 0)
    draw_r = ImageDraw.Draw(mask_r)

    pts_r = [
        (w_crop_r, 0),
        (85, 0),        # top of upper floral mound
        (65, 40),       # soft edge of sunlight
        (40, 100),      # edge of second mound into aisle
        (22, 160),      # edge of foreground mound into aisle
        (0, 210),       # aisle floor
        (0, orig_h),
        (w_crop_r, orig_h),
    ]
    draw_r.polygon([(x * scale, y * scale) for x, y in pts_r], fill=255)

    arr_r = np.array(mask_r, dtype=np.float32)
    # Smooth gradient fade on left side towards aisle center
    fade_end_xr = int(w_r * 0.44)
    for y in range(h_r):
        for x in range(fade_end_xr):
            fade = x / fade_end_xr
            arr_r[y, x] = arr_r[y, x] * max(0.0, float(fade ** 1.25))

    # Soft fade at the top boundary so columns and flowers emerge seamlessly
    top_fade_hr = int(32 * scale)
    for y in range(top_fade_hr):
        fade_y = (y / top_fade_hr) ** 1.4
        arr_r[y, :] *= fade_y

    mask_r_final = Image.fromarray(np.uint8(np.clip(arr_r, 0, 255))).filter(ImageFilter.GaussianBlur(radius=scale * 2.0))
    right_scaled.putalpha(mask_r_final)

    # Save PNG
    right_png_path = os.path.join(public_dir, "wedding_bottom_right.png")
    right_scaled.save(right_png_path, format="PNG", optimize=True)
    print(f"Saved: {right_png_path} ({right_scaled.size})")

    # Encode to Base64 for self-contained SVG
    buffered_r = io.BytesIO()
    right_scaled.save(buffered_r, format="PNG", optimize=True)
    right_b64 = base64.b64encode(buffered_r.getvalue()).decode("ascii")

    # Generate Right SVG
    svg_right_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w_r} {h_r}" width="100%" height="100%" preserveAspectRatio="xMaxYMax meet">
  <defs>
    <filter id="shadow-right" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="-4" stdDeviation="12" flood-color="#8c5848" flood-opacity="0.22" />
    </filter>
  </defs>
  <g filter="url(#shadow-right)">
    <image href="data:image/png;base64,{right_b64}" width="{w_r}" height="{h_r}" x="0" y="0" />
  </g>
</svg>
'''
    right_svg_path = os.path.join(public_dir, "wedding_bottom_right.svg")
    with open(right_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_right_content)
    print(f"Saved: {right_svg_path}")

    print("All 4 assets (2 PNG photos + 2 SVGs) generated successfully!")

if __name__ == "__main__":
    generate_assets()
