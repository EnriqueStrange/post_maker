from PIL import Image, ImageDraw, ImageFont

def generate_image_template(width, height, background_color, border_color, border_thickness, top_space, logo_path, logo_width, logo_height ,header_text , text, text_font, text_font_size):
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
    text_y = top_space + 10  # Adjust the value as needed to leave space below the top part
    
    # Split the text into lines to fit within the image width
    lines = []
    current_line = ""
    words = text.split()
    for word in words:
        test_line = current_line + word + " "
        test_width, _ = draw.textsize(test_line, font=text_font)
        if test_width <= width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)

    # Calculate the position to center the text horizontally
    header_text_x = (width - text_width) // 3
    header_text_y = top_space // 4

    #Draw the STRANGE LEARNINGS text
    draw.text((header_text_x, header_text_y
                      ), header_text, font=text_font, fill=(0, 0, 0))
    
    # Draw the text below the top space, adjusting for line breaks
    for line in lines:
        line_width, line_height = draw.textsize(line, font=text_font)
        line_x = (width - line_width) // 2
        draw.text((line_x, text_y), line, font=text_font, fill=(0, 0, 0))
        text_y += line_height + 10  # Adjust the value as needed to leave space between lines
    
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
logo_width = 50  # Adjust the logo width as needed
logo_height = 50  # Adjust the logo height as needed
header_text = "STRANGE LEARNINGS"
text = input("Enter the text: ")  # User-provided text
text_font = ImageFont.truetype("arial.ttf", 30)  # Font type and size
text_font_size = 30

## Generate the image template
generate_image_template(
    template_width,
    template_height,
    template_background_color,
    template_border_color,
    template_border_thickness,
    template_top_space,
    logo_file,
    logo_width,
    logo_height,
    header_text,
    text,
    text_font,
    text_font_size,
)
