from PIL import Image, ImageDraw, ImageFont

# Load the certificate template
template = Image.open('certificate_template.png')

# Define font and size
font = ImageFont.truetype('arial.ttf', 60)  # Adjust the font and size as needed

# Open the text file and read the names
with open('participants_list.txt', 'r') as file:
    names = file.readlines()

# Create certificates for each name
for name in names:
    name = name.strip()  # Remove any extra spaces or newline characters

    # Create a copy of the template
    cert = template.copy()

    # Draw the name on the certificate
    draw = ImageDraw.Draw(cert)
    draw.text((400, 300), name, font=font, fill='black')  # Adjust position (x, y)

    # Save the certificate
    cert.save(f'certificates/{name}.png')

print("Certificates generated successfully!")
