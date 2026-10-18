import os
from PIL import Image, ImageDraw, ImageFont

ASSET_DIR = "/home/developer/.gemini/antigravity-ide/scratch/apps-femininos/app-bebe-maternidade/store_assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def create_icon():
    img = Image.new("RGBA", (512, 512), color=(253, 242, 248, 255)) # Soft pink background
    draw = ImageDraw.Draw(img)
    # Background circular gradient / soft circle
    draw.ellipse([32, 32, 480, 480], fill=(244, 114, 182, 255))
    draw.ellipse([64, 64, 448, 448], fill=(219, 39, 119, 255))
    
    # Inner baby heart & silhouette shape
    draw.ellipse([140, 140, 372, 372], fill=(255, 255, 255, 255))
    draw.ellipse([196, 196, 316, 316], fill=(244, 114, 182, 255))
    
    # Save icon
    path = os.path.join(ASSET_DIR, "icon-512.png")
    img.save(path, "PNG")
    print("Icon generated:", path)

def create_feature():
    img = Image.new("RGB", (1024, 500), color=(253, 242, 248))
    draw = ImageDraw.Draw(img)
    
    # Decorative shapes
    draw.rectangle([0, 0, 1024, 500], fill=(255, 241, 242))
    draw.ellipse([-100, -100, 400, 400], fill=(254, 205, 211))
    draw.ellipse([700, 200, 1200, 700], fill=(251, 207, 232))
    
    # Card container in the middle
    draw.rounded_rectangle([150, 70, 874, 430], radius=24, fill=(255, 255, 255))
    draw.rounded_rectangle([180, 100, 320, 240], radius=16, fill=(244, 114, 182))
    
    # Text placeholder / lines
    draw.rectangle([360, 120, 780, 160], fill=(219, 39, 119))
    draw.rectangle([360, 180, 700, 210], fill=(156, 163, 175))
    draw.rectangle([180, 280, 840, 310], fill=(243, 244, 246))
    draw.rectangle([180, 330, 800, 360], fill=(243, 244, 246))
    draw.rectangle([180, 380, 720, 400], fill=(243, 244, 246))
    
    path = os.path.join(ASSET_DIR, "feature-graphic-1024x500.png")
    img.save(path, "PNG")
    print("Feature graphic generated:", path)

def create_screenshots():
    screens = [
        ("Amamentação & Extração", (244, 114, 182)),
        ("Sons para Acalmar & Sono", (168, 85, 247)),
        ("Fraldas & Alimentação", (236, 72, 153)),
        ("Evolução & Rotina Diária", (99, 102, 241))
    ]
    for idx, (title, color) in enumerate(screens, 1):
        img = Image.new("RGB", (1080, 1920), color=(253, 242, 248))
        draw = ImageDraw.Draw(img)
        
        # Header banner
        draw.rectangle([0, 0, 1080, 360], fill=color)
        
        # Phone mockup card
        draw.rounded_rectangle([90, 420, 990, 1800], radius=40, fill=(255, 255, 255))
        
        # Top pill inside phone
        draw.rounded_rectangle([150, 480, 930, 680], radius=24, fill=(249, 250, 251))
        draw.rounded_rectangle([190, 520, 450, 640], radius=16, fill=color)
        
        # Stat cards
        for y in range(740, 1650, 200):
            draw.rounded_rectangle([150, y, 930, y + 160], radius=20, fill=(243, 244, 246))
            draw.rounded_rectangle([170, y + 20, 290, y + 140], radius=14, fill=color)
            draw.rectangle([320, y + 40, 750, y + 70], fill=(75, 85, 99))
            draw.rectangle([320, y + 90, 600, y + 120], fill=(156, 163, 175))
            
        path = os.path.join(ASSET_DIR, f"phone-{idx}.png")
        img.save(path, "PNG")
        print(f"Screenshot {idx} generated:", path)

create_icon()
create_feature()
create_screenshots()
