from PIL import Image
import numpy as np

#--------------- Loads the target image ---------------
target_img = Image.open("target.png").convert("RGB")
W, H = target_img.size
target_array = np.array(target_img)

print(f"Image size: {W}x{H}")
print(f"Array shape: {target_array.shape}")

#--------------- Render function - draws the chromosomes ---------------
def render(chromosome):
    img = Image.new("RGB", (W, H), (255, 255, 255))  # white background
    draw = ImageDraw.Draw(img, "RGBA")  # RGBA has transparency unlike RGB
    for shape in chromosome:
        draw.polygon(shape["points"], fill=shape["color"])
    return img

#--------------- Render function - draws the chromosomes ---------------

def fitness(chromosome):
    rendered = render(chromosome)
    rendered_array = np.array(rendered)
    
    diff = np.sum((rendered_array.astype(int) - target_array.astype(int)) ** 2)
    max_diff = 255**2 * 3 * W * H  # worst possible difference between the two images
    
    return 1.0 - (diff / max_diff)  # 1.0 = perfect match, 0.0 = worst, cannot give a number outside of 1-0
