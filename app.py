from PIL import Image, ImageDraw, ImageFont

template = Image.open('certificate_template.png')
dpi = 300
y_position = int(6.2 * dpi / 2.54)
font = ImageFont.truetype('arial.ttf', 80)
with open('participants_list.txt', 'r') as file:
    names = file.readlines()
for name in names:
    name = ''.join(word.capitalize() for word in name.strip().split()) 
    cert = template.copy()
    draw = ImageDraw.Draw(cert)
    bbox = font.getbbox(name)
    text_width = bbox[2] - bbox[0] 
    template_width = cert.width
    x_position = (template_width - text_width) // 2
    draw.text((x_position, y_position), name, font=font, fill='black')
    cert.save(f'certificates/{name}.png')

print("Certificates generated successfully!")