#Ayub Ali
from PIL import Image
from PIL import Image, ImageDraw

def frame_picture():
    picture = draw_picture()
    picture = fix_fram(picture)

    picture.save("final_project.png")
    picture.show()

def fix_fram(file_name):
    picture = Image.open("broken_600.png")
    section1 = picture.crop((1,1,150,300))#blue
    section2 = picture.crop((150,150,300,300))#green
    section3 = picture.crop((450,300,600,450))#red
    section4 = picture.crop((300,450,450,600))#yellow
    
    x = 300 #600/2 = 300 so each section should be (300,300) or i could've done width//2
    y = 300
    section1 = section1.resize((x,y))
    section2 = section2.resize((x,y))
    section3 = section3.resize((x,y))
    section4 = section4.resize((x,y))

    section1 = section1.transpose(Image.ROTATE_180)
    section2 = section2.transpose(Image.ROTATE_180)
    section4 = section4.transpose(Image.ROTATE_270)

    picture.paste(section1, (300, 1))  # Blue Top right
    picture.paste(section2, (300, 300))  # Green bottom right
    picture.paste(section3, (1, 1))  # Red top left
    picture.paste(section4, (1, 300))  # Yellow bottom left
    
    return picture

def draw_picture(): #island
    image = Image.new("RGB",(100,100), (200,200,220))
    draw = ImageDraw.Draw(image)
    draw.ellipse([(0,20),(100,40)],"white",None)
    draw.rectangle([(-5,80),(100,100)],"blue", width=0.5)
    draw.polygon([(-10,80),(50,80),(30,200)],"green")
    draw.line([(50,80),(50,100)],"yellow",10)
    draw.text((30,25),"Island","black")
    image.show()

frame_picture()


