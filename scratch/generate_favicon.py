from PIL import Image, ImageDraw, ImageFont

# Create a blank near-white image
size = 256
image = Image.new("RGB", (size, size), "#FAFAFA")
draw = ImageDraw.Draw(image)

# Draw a dark circle (near-black)
circle_bbox = [16, 16, size-16, size-16]
draw.ellipse(circle_bbox, fill="#1E1E1E")

# Try to load a font, fallback to default
try:
    font = ImageFont.truetype("arialbd.ttf", 100)
except IOError:
    font = ImageFont.load_default()

# Add text "RE"
text = "RE"
# Since ImageFont.load_default() gives very small text, we will scale it up if needed, 
# or just draw some simple geometric lines for a monogram if the font is default.
# We'll assume the font loaded, or we'll just draw the letters manually to be safe.

# Draw "RE" manually using rectangles if arial isn't available to ensure it looks bold and clean
# We'll just draw it with rectangles
# Letter R
draw.rectangle([70, 70, 90, 180], fill="#FAFAFA") # left stem
draw.rectangle([70, 70, 130, 90], fill="#FAFAFA") # top bar
draw.rectangle([110, 70, 130, 120], fill="#FAFAFA") # right loop edge
draw.rectangle([70, 110, 130, 130], fill="#FAFAFA") # middle bar
# R leg
draw.polygon([(90, 130), (110, 130), (140, 180), (120, 180)], fill="#FAFAFA")

# Letter E
draw.rectangle([150, 70, 170, 180], fill="#FAFAFA") # left stem
draw.rectangle([150, 70, 200, 90], fill="#FAFAFA") # top bar
draw.rectangle([150, 115, 190, 135], fill="#FAFAFA") # middle bar
draw.rectangle([150, 160, 200, 180], fill="#FAFAFA") # bottom bar

image.save("work/figures/favicon.png")
print("Favicon generated successfully.")
