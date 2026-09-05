import os
import io
import base64
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.ndimage import distance_transform_edt, binary_dilation

def run():
    public_dir = r"d:\Learn\AI\02.Weeding\02._V2\public"
    os.makedirs(public_dir, exist_ok=True)

    # 1. Clean the full annotated image by inpainting the thin black pen lines
    annotated_path = r"C:\Users\lemon\.gemini\antigravity-ide\brain\5423af7d-f4aa-4698-b280-cdfe0ca4c2b2\.user_uploaded\media_1788595967089.jpg"
    img_full = Image.open(annotated_path).convert("RGB")
    arr_full = np.array(img_full, dtype=np.float32)

    black_mask = (arr_full[:,:,0] < 50) & (arr_full[:,:,1] < 50) & (arr_full[:,:,2] < 50)
    dilated_mask = binary_dilation(black_mask, iterations=2)
    indices = distance_transform_edt(dilated_mask, return_distances=False, return_indices=True)
    clean_full_arr = arr_full[indices[0], indices[1]]
    clean_full = Image.fromarray(np.uint8(clean_full_arr)).convert("RGBA")
    w_f, h_f = clean_full.size

    # Also load the pristine bottom panorama (which has no compression artifacts or annotations)
    bottom_pristine_path = r"C:\Users\lemon\.gemini\antigravity-ide\brain\5423af7d-f4aa-4698-b280-cdfe0ca4c2b2\.user_uploaded\media_1788594673588.png"
    bottom_pristine = Image.open(bottom_pristine_path).convert("RGBA")
    w_bp, h_bp = bottom_pristine.size

    def save_asset_trio(name, img_rgba, view_box_w, view_box_h, align="xMidYMid"):
        # Save PNG (transparency)
        png_path = os.path.join(public_dir, f"{name}.png")
        img_rgba.save(png_path, format="PNG", optimize=True)

        # Save JPG (clean light backdrop)
        jpg_bg = Image.new("RGB", img_rgba.size, (253, 250, 246))
        jpg_bg.paste(img_rgba, mask=img_rgba.split()[3])
        jpg_path = os.path.join(public_dir, f"{name}.jpg")
        jpg_bg.save(jpg_path, format="JPEG", quality=95)

        # Save SVG (self-contained with embedded image & shadow filter)
        buffered = io.BytesIO()
        img_rgba.save(buffered, format="PNG", optimize=True)
        b64 = base64.b64encode(buffered.getvalue()).decode("ascii")

        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {view_box_w} {view_box_h}" width="100%" height="100%" preserveAspectRatio="{align} meet">
  <defs>
    <filter id="shadow-{name}" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="3" stdDeviation="8" flood-color="#8c5848" flood-opacity="0.22" />
    </filter>
  </defs>
  <g filter="url(#shadow-{name})">
    <image href="data:image/png;base64,{b64}" width="{view_box_w}" height="{view_box_h}" x="0" y="0" />
  </g>
</svg>
'''
        svg_path = os.path.join(public_dir, f"{name}.svg")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Generated: {name} (PNG, JPG, SVG)")

    # =========================================================================
    # ITEM 1: TOP LEFT ARCH FLORAL CORNER
    # =========================================================================
    c1_raw = clean_full.crop((0, 0, 235, 260))
    scale = 2
    w1, h1 = c1_raw.size[0] * scale, c1_raw.size[1] * scale
    c1 = c1_raw.resize((w1, h1), Image.Resampling.LANCZOS)
    c1 = c1.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=2))

    # Mask: Outer boundary stays solid, inner arch & bottom wisteria soft fade
    mask1 = Image.new("L", (w1, h1), 255)
    arr_m1 = np.array(mask1, dtype=np.float32)
    # Fade right side towards center arch
    for y in range(h1):
        for x in range(int(w1 * 0.65), w1):
            fade_x = 1.0 - (x - w1 * 0.65) / (w1 * 0.35)
            arr_m1[y, x] *= max(0.0, float(fade_x ** 1.3))
    # Fade bottom wisteria tips into transparency
    for y in range(int(h1 * 0.75), h1):
        fade_y = 1.0 - (y - h1 * 0.75) / (h1 * 0.25)
        arr_m1[y, :] *= max(0.0, float(fade_y ** 1.3))

    c1_mask = Image.fromarray(np.uint8(np.clip(arr_m1, 0, 255))).filter(ImageFilter.GaussianBlur(radius=3))
    c1.putalpha(c1_mask)
    save_asset_trio("wedding_arch_corner_left", c1, w1, h1, align="xMinYMin")

    # =========================================================================
    # ITEM 2: TOP RIGHT ARCH FLORAL CORNER
    # =========================================================================
    c2_raw = clean_full.crop((447, 0, 682, 260))
    w2, h2 = c2_raw.size[0] * scale, c2_raw.size[1] * scale
    c2 = c2_raw.resize((w2, h2), Image.Resampling.LANCZOS)
    c2 = c2.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=2))

    mask2 = Image.new("L", (w2, h2), 255)
    arr_m2 = np.array(mask2, dtype=np.float32)
    # Fade left side towards center arch
    for y in range(h2):
        for x in range(int(w2 * 0.35)):
            fade_x = x / (w2 * 0.35)
            arr_m2[y, x] *= max(0.0, float(fade_x ** 1.3))
    # Fade bottom wisteria tips
    for y in range(int(h2 * 0.75), h2):
        fade_y = 1.0 - (y - h2 * 0.75) / (h2 * 0.25)
        arr_m2[y, :] *= max(0.0, float(fade_y ** 1.3))

    c2_mask = Image.fromarray(np.uint8(np.clip(arr_m2, 0, 255))).filter(ImageFilter.GaussianBlur(radius=3))
    c2.putalpha(c2_mask)
    save_asset_trio("wedding_arch_corner_right", c2, w2, h2, align="xMaxYMin")

    # =========================================================================
    # ITEM 3: MIDDLE ARCH / HANGING FLORAL CANOPY
    # =========================================================================
    c3_raw = clean_full.crop((95, 220, 587, 480))
    w3, h3 = c3_raw.size[0] * scale, c3_raw.size[1] * scale
    c3 = c3_raw.resize((w3, h3), Image.Resampling.LANCZOS)
    c3 = c3.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=2))

    mask3 = Image.new("L", (w3, h3), 255)
    arr_m3 = np.array(mask3, dtype=np.float32)
    # Soft fade on left and right ends
    fade_margin_x = int(w3 * 0.12)
    for y in range(h3):
        for x in range(fade_margin_x):
            fade_l = x / fade_margin_x
            arr_m3[y, x] *= max(0.0, float(fade_l ** 1.2))
        for x in range(w3 - fade_margin_x, w3):
            fade_r = (w3 - x) / fade_margin_x
            arr_m3[y, x] *= max(0.0, float(fade_r ** 1.2))
    # Soft fade at top and bottom wisteria ends
    fade_top = int(h3 * 0.08)
    for y in range(fade_top):
        arr_m3[y, :] *= (y / fade_top) ** 1.2
    fade_bot = int(h3 * 0.2)
    for y in range(h3 - fade_bot, h3):
        fade_b = (h3 - y) / fade_bot
        arr_m3[y, :] *= max(0.0, float(fade_b ** 1.3))

    c3_mask = Image.fromarray(np.uint8(np.clip(arr_m3, 0, 255))).filter(ImageFilter.GaussianBlur(radius=3))
    c3.putalpha(c3_mask)
    save_asset_trio("wedding_arch_canopy_center", c3, w3, h3, align="xMidYMid")

    # =========================================================================
    # ITEM 4: BOTTOM LEFT FLORAL MOUND
    # =========================================================================
    w_crop_l = int(w_bp * 0.52)
    c4_raw = bottom_pristine.crop((0, 0, w_crop_l, h_bp))
    scale_b = 3
    w4, h4 = w_crop_l * scale_b, h_bp * scale_b
    c4 = c4_raw.resize((w4, h4), Image.Resampling.LANCZOS)
    c4 = c4.filter(ImageFilter.UnsharpMask(radius=1.5, percent=125, threshold=2))

    mask4 = Image.new("L", (w4, h4), 0)
    draw4 = ImageDraw.Draw(mask4)
    pts4 = [
        (0, 0),
        (225, 0),
        (250, 40),
        (275, 100),
        (295, 160),
        (w_crop_l, 210),
        (w_crop_l, h_bp),
        (0, h_bp),
    ]
    draw4.polygon([(x * scale_b, y * scale_b) for x, y in pts4], fill=255)
    arr_m4 = np.array(mask4, dtype=np.float32)

    # Right fade towards center aisle
    fade_start_x4 = int(w4 * 0.56)
    for y in range(h4):
        for x in range(fade_start_x4, w4):
            fade = 1.0 - (x - fade_start_x4) / (w4 - fade_start_x4)
            arr_m4[y, x] *= max(0.0, float(fade ** 1.25))
    # Top fade so columns and upper florals blend smoothly
    top_fade_h4 = int(32 * scale_b)
    for y in range(top_fade_h4):
        arr_m4[y, :] *= (y / top_fade_h4) ** 1.4

    c4_mask = Image.fromarray(np.uint8(np.clip(arr_m4, 0, 255))).filter(ImageFilter.GaussianBlur(radius=scale_b * 2.0))
    c4.putalpha(c4_mask)
    save_asset_trio("wedding_bottom_left", c4, w4, h4, align="xMinYMax")

    # =========================================================================
    # ITEM 5: BOTTOM RIGHT FLORAL MOUND
    # =========================================================================
    x_crop_r = int(w_bp * 0.48)
    w_crop_r = w_bp - x_crop_r
    c5_raw = bottom_pristine.crop((x_crop_r, 0, w_bp, h_bp))
    w5, h5 = w_crop_r * scale_b, h_bp * scale_b
    c5 = c5_raw.resize((w5, h5), Image.Resampling.LANCZOS)
    c5 = c5.filter(ImageFilter.UnsharpMask(radius=1.5, percent=125, threshold=2))

    mask5 = Image.new("L", (w5, h5), 0)
    draw5 = ImageDraw.Draw(mask5)
    pts5 = [
        (w_crop_r, 0),
        (85, 0),
        (65, 40),
        (40, 100),
        (22, 160),
        (0, 210),
        (0, h_bp),
        (w_crop_r, h_bp),
    ]
    draw5.polygon([(x * scale_b, y * scale_b) for x, y in pts5], fill=255)
    arr_m5 = np.array(mask5, dtype=np.float32)

    # Left fade towards center aisle
    fade_end_x5 = int(w5 * 0.44)
    for y in range(h5):
        for x in range(fade_end_x5):
            fade = x / fade_end_x5
            arr_m5[y, x] *= max(0.0, float(fade ** 1.25))
    # Top fade
    top_fade_h5 = int(32 * scale_b)
    for y in range(top_fade_h5):
        arr_m5[y, :] *= (y / top_fade_h5) ** 1.4

    c5_mask = Image.fromarray(np.uint8(np.clip(arr_m5, 0, 255))).filter(ImageFilter.GaussianBlur(radius=scale_b * 2.0))
    c5.putalpha(c5_mask)
    save_asset_trio("wedding_bottom_right", c5, w5, h5, align="xMaxYMax")

    print("\nAll 5 assets (SVG, PNG, JPG) generated and saved successfully!")

if __name__ == "__main__":
    run()
