import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

repo_dir = r"C:\Users\sri charan\.gemini\antigravity\scratch\2520090137_OSSP"

# Ensure directories exist
os.makedirs(os.path.join(repo_dir, "2520090137_Practical", "Practical-01", "screenshots"), exist_ok=True)
os.makedirs(os.path.join(repo_dir, "2520090137_Skill", "Skill-01", "screenshots"), exist_ok=True)

# Function to render code / terminal output as high-resolution PNG image
def render_text_to_image(text, output_path, title="Terminal Output"):
    lines = text.splitlines()
    if not lines:
        lines = [" "]
    
    font_size = 15
    try:
        font = ImageFont.truetype("consola.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Determine dimensions
    padding = 20
    header_height = 40
    
    max_line_len = max(len(line) for line in lines) if lines else 20
    char_width = 9.2
    line_height = 22
    
    img_width = max(700, int(max_line_len * char_width) + (padding * 2))
    img_height = header_height + (len(lines) * line_height) + (padding * 2)

    img = Image.new("RGB", (img_width, img_height), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)

    # Title bar (Dark header with terminal dots)
    draw.rectangle([(0, 0), (img_width, header_height)], fill=(45, 45, 45))
    draw.ellipse([(15, 14), (27, 26)], fill=(255, 95, 86)) # Close
    draw.ellipse([(35, 14), (47, 26)], fill=(255, 189, 46)) # Minimize
    draw.ellipse([(55, 14), (67, 26)], fill=(39, 201, 63)) # Expand

    draw.text((80, 10), title, font=font, fill=(200, 200, 200))

    # Text content
    y = header_height + padding
    for line in lines:
        draw.text((padding, y), line, font=font, fill=(240, 240, 240))
        y += line_height

    img.save(output_path)
    print(f"Saved screenshot: {output_path}")

print("Screenshot renderer setup ready.")
