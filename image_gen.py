#Generating images after getting the text data from text_gen.py 

from PIL import Image, ImageDraw, ImageFont

def generate_image_template(width, height, background_color, border_color, border_thickness, top_space, logo_path, logo_width, logo_height, text, text_font, text_font_size):
    # Create a new image with the specified width and height
    image = Image.new("RGB", (width, height), background_color)
    
    # Create a draw object
    draw = ImageDraw.Draw(image)
    
    # Draw a border
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=border_color, width=border_thickness)
    
    # Draw a black line at the top, leaving some space
    draw.line([(0, top_space), (width - 1, top_space)], fill=(0, 0, 0), width=3)
    
    # Load the logo image
    logo = Image.open(logo_path)
    
    # Resize the logo image
    logo = logo.resize((logo_width, logo_height))
    
    # Paste the logo image at the top corners
    image.paste(logo, (0, 0))
    image.paste(logo, (width - logo_width, 0))
    
    # Calculate the text dimensions
    text_width, text_height = draw.textsize(text, font=text_font)
    
    # Calculate the position to center the text horizontally
    text_x = (width - text_width) // 2
    text_y = top_space // 3
    
    # Draw the text in the center of the top part
    draw.text((text_x, text_y), text, font=text_font, fill=(0, 0, 0))
    
    # Save the image
    image.save("image_template.png")
    print("Image template generated successfully!")

# Specify the parameters for the image template
template_width = 800
template_height = 600
template_background_color = (128, 128, 128)  # RGB values for #808080
template_border_color = (0, 0, 0)  # Black color (RGB values)
template_border_thickness = 5
template_top_space = 50  # Adjust this value to leave the desired space at the top
logo_file = "logo.png"  # Path to the logo image file
logo_width = 100  # Adjust the logo width as needed
logo_height = 100  # Adjust the logo height as needed
text = "STRANGE LEARNINGS"  # The text to be displayed
text_font = ImageFont.truetype("arial.ttf", 30)  # Font type and size
text_font_size = 30

# Generate the image template
generate_image_template(template_width, template_height, template_background_color, template_border_color, template_border_thickness, template_top_space, logo_file, logo_width, logo_height, text, text_font, text_font_size)
