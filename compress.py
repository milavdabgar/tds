from PIL import Image

with Image.open('shapes.png') as img:
    # Convert to lossless WebP with maximum compression
    img.save('shapes_compressed.webp', 'WEBP', lossless=True, quality=100, method=6)
