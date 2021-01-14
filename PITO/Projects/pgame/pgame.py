from PIL import Image
###################################################################################
R,G,B = 0,0,0
new_color = (R,G,B)

picture = Image.open("Projects/pgame/Resources/d2.png")

width, height = picture.size

for x in range(width):
    for y in range(height):
        current_color = picture.getpixel( (x,y) )
        R,G,B = current_color
        if G == 255:
            G,R = 0,255
        elif R == 255:
            R,B = 0,255
        elif B == 255:
            B,G = 0,255
        new_color = (R,G,B)
        picture.putpixel( (x,y), new_color)