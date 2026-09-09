from PIL import Image, ImageDraw, ImageFont

# Create a blank white image
width = 600
height = 250
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Colors
blue_header = (26, 115, 232)
text_black = (32, 33, 36)
text_gray = (95, 99, 104)

# Draw header background
draw.rectangle([0, 0, width, 40], fill=blue_header)

# Draw Header text
draw.text((15, 12), "Google Calendar - Event Details", fill="white")

# Draw Event Title
draw.text((20, 60), "Portfolio Audit & Next Case Sync", fill=text_black)

# Draw details
draw.text((20, 100), "Time: Every 6 weeks", fill=text_gray)
draw.text((20, 130), "Notification: Email 1 day before", fill=text_gray)
draw.text((20, 160), "Description:", fill=text_black)
draw.text((20, 185), "1. Open 'FlyRank ML Portfolio' Claude Project.", fill=text_gray)
draw.text((20, 205), "2. Run the 3-beat prompt (Problem, Action, Result) for the Drift Monitor project.", fill=text_gray)

# Save image
image.save("work/figures/calendar_reminder.png")
print("Calendar reminder image generated successfully.")
