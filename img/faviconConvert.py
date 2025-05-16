from PIL import Image
import os

# === 配置部分 ===
input_file = "my-blog/source/img/favicon.png"  # 替换为你的图片路径
output_dir = "./output"        # 输出目录
sizes = [(32, 32), (64, 64), (128, 128)]  # 输出的尺寸

# === 创建输出目录 ===
os.makedirs(output_dir, exist_ok=True)

# === 打开源图像 ===
with Image.open(input_file) as img:
    for size in sizes:
        resized = img.resize(size, Image.LANCZOS)
        output_png_path = os.path.join(output_dir, f"favicon_{size[0]}x{size[1]}.png")
        resized.save(output_png_path, format="PNG", dpi=(72, 72))
        print(f"[✓] Saved {output_png_path}")

    # === 生成 ICO 文件 ===
    ico_path = os.path.join(output_dir, "favicon.ico")
    img.save(ico_path, format="ICO", sizes=sizes)
    print(f"[✓] Saved {ico_path} (multi-size)")
