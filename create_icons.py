
from PIL import Image, ImageOps
from pathlib import Path

photo_path = Path("school.png")

if not photo_path.exists():
    print("ERROR: school.png not found!")
    raise SystemExit

image = Image.open(photo_path).convert("RGB")

width, height = image.size
side = min(width, height)

left = (width - side) // 2
top = (height - side) // 2

image = image.crop((left, top, left + side, top + side))

output_folder = Path("static/images")
output_folder.mkdir(parents=True, exist_ok=True)

for size in [192, 512]:
    icon = ImageOps.fit(
        image,
        (size, size),
        method=Image.Resampling.LANCZOS
    )

    output_path = output_folder / f"icon-{size}x{size}.png"
    icon.save(output_path, "PNG")

    print(f"Created: {output_path}")

print("SUCCESS! Both icons are ready.")
