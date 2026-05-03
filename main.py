from PIL import Image
import numpy as np

# Load the target image
target_img = Image.open("target.png").convert("RGB")
W, H = target_img.size
target_array = np.array(target_img)

print(f"Image size: {W}x{H}")
print(f"Array shape: {target_array.shape}")

def render(chromosome):
    img = Image.new("RGB", (W, H), (255, 255, 255))  # white background
    draw = ImageDraw.Draw(img, "RGBA")  # RGBA mode enables transparency
    for shape in chromosome:
        draw.polygon(shape["points"], fill=shape["color"])
    return img