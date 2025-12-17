from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a white background
image = Image.new('RGB', (400, 200), color='white')
draw = ImageDraw.Draw(image)

# Try to load a font
try:
    # Try Arial on Windows
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    try:
        # Try Arial on Windows (with bold)
        font = ImageFont.truetype("arialbd.ttf", 20)
    except IOError:
        # Try DejaVu on Linux
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        except IOError:
            # Try Arial on macOS
            try:
                font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 20)
            except IOError:
                # Fallback to default
                font = ImageFont.load_default()

# Draw item details
draw.text((10, 10), "Item: Stainless Steel Valve", fill='black', font=font)
draw.text((10, 40), "ID: INV-45782", fill='black', font=font)
draw.text((10, 70), "Location: Aisle 4, Row B, Shelf 3", fill='black', font=font)
draw.text((10, 100), "Qty: 48", fill='black', font=font)

# Draw a simple barcode (just an example pattern)
barcode_start_x = 10
barcode_start_y = 130
barcode_height = 40
barcode_widths = [2, 1, 2, 3, 1, 2]  # pattern of line widths
for i, width in enumerate(barcode_widths):
    x0 = barcode_start_x + sum(barcode_widths[:i])
    draw.rectangle([x0, barcode_start_y, x0 + width, barcode_start_y + barcode_height], fill='black')

# Save the image
image.save("test_inventory_image.png")

print("Test image created: test_inventory_image.png")