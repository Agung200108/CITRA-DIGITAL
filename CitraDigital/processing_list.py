from PIL import Image, ImageOps
from queue import Empty
from tkinter import Canvas
import math
from math import floor

# Main Feature
def ImgNegative(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


def clipping(intensity):
    if intensity < 0:
        return 0
    if intensity > 255:
        return 255
    return intensity


def ImgBrightness(img_input, coldepth, brightness):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (clipping(r+brightness),
                            clipping(g+brightness), clipping(b+brightness))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgBlending(img_input, imgInput2, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
        imgInput2 = imgInput2.convert('RGB')
        # print(img_input, imgInput2)
    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r1, g1, b1 = img_input.getpixel((i, j))
            r2, g2, b2 = imgInput2.getpixel((i, j))
            Rblend, Gblend, Bblend = r1+r2, g1+g2, b1+b2
            pixels[i, j] = (Rblend, Gblend, Bblend)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgLogaritmic(img_input, coldepth, c):
    # solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (int(c*math.log(1+r)),
                            int(c*math.log(1+g)), int(c*math.log(1+b)))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgPowerLaw(img_input, coldepth, gamma):
    # solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))

            pixels[i, j] = (int(255*(r/255)**gamma),
                            int(255*(g/255)**gamma), int(255*(b/255)**gamma))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgThreshold(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    PIXEL = img_input.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if PIXEL[i, j] < (128, 128, 128):
                pixels[i, j] = (0, 0, 0)
            elif PIXEL[i, j] >= (128, 128, 128):
                pixels[i, j] = (255, 255, 255)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgRotate90(img_input, coldepth, deg, direction):
    # solusi 1
    # img_output=img_input.rotate(deg)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction == "C":
                r, g, b = img_input.getpixel((j, img_output.size[0]-i-1))

            else:
                r, g, b = img_input.getpixel((img_input.size[1]-j-1, i))

            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgRotate180(img_input, coldepth, deg, direction):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction == "C":
                r, g, b = img_input.getpixel(
                    (img_output.size[1]-i-1, img_output.size[0]-j-1))
            else:
                r, g, b = img_input.getpixel((img_output.size[0]-j-1, i))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


def ImgRotate270(img_input, coldepth, deg, direction):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction == "C":
                r, g, b = img_input.getpixel((img_output.size[1]-j-1, i))
            else:
                r, g, b = img_input.getpixel((img_input.size[1]-j-1, i))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

def ImgFlippingVertikal(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    PIXEL = img_input.load()

    ukuran_horizontal = img_input.size[0]
    ukuran_vertikal = img_input.size[1]

    img_output = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = img_output.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[x, ukuran_vertikal - 1 - y]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgFlippingHorizontal(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    PIXEL = img_input.load()

    ukuran_horizontal = img_input.size[0]
    ukuran_vertikal = img_input.size[1]

    img_output = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = img_output.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[ukuran_horizontal - 1 - x, y]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgFlippingVerHor(img_input, coldepth):
    #img_output = img_input.transpose(Image.FLIP_LEFT_RIGHT)

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[0]):
            r, g, b = img_input.getpixel(
                ((img_output.size[0]-1)-i, (img_output.size[1]-1)-j))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTranslasi(img_input, coldepth, sumbuTransform):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixel = img_input.load()
    pixels = img_output.load()

    n = 50

    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):

            r, g, b = img_input.getpixel((i, j))
            r = 0
            g = 0
            b = 0

            if sumbuTransform == "x":
                if i <= n:
                    pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = pixel[i - n, j]
            elif sumbuTransform == "y":
                if j <= n:
                    pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = pixel[i, j - n]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


    
def ImgZoom(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    N = 2
    rowOut, colOut = int(img_input.size[0]*N), int(img_input.size[1]*N)

    img_output = Image.new('RGB', (rowOut, colOut))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((floor(i/N), floor(j/N)))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgShrinking(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    N = 2
    rowOut, colOut = int(img_input.size[0]/N), int(img_input.size[1]/N)

    img_output = Image.new('RGB', (rowOut, colOut))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((floor(i*N), floor(j*N)))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def RGBtoGrayscale(img_input, coldepth):
    
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    npixels = img_output.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = pixels[i,j]
            #if i > int(img_input.size[0])//2:
            if i < j:  #untuk miring
                Gray = (r + g + b)//3
                npixels[i,j] = (Gray, Gray, Gray)
            else:
                npixels[i,j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgCircle(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    npixels = img_output.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = pixels[i,j]
            if (i - img_input.size[0]//2)**2 + (j - img_input.size[1]//2)**2 < (img_input.size[0]//2)**2:
                Gray = (r + g + b)//3
                npixels[i, j] = (255-r, 255-g, 255-b)
            else:
                npixels[i,j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgRhombus(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    npixels = img_output.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = pixels[i,j]
            if abs(i - img_input.size[0]//2) + abs(j - img_input.size[1]//2) < img_input.size[0]//2:
                Gray = (r + g + b)//3
                npixels[i, j] = (255-r, 255-g, 255-b)
            else:
                npixels[i,j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgCross(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if i < img_output.size[0]/2 and j < img_output.size[1]/2:
                if i <= j:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)
            if i >= img_output.size[0]/2 and j < img_output.size[1]/2:
                if i-img_output.size[0]/2+j < img_output.size[1]/2:
                    pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = (255-r, 255-g, 255-b)
            if i < img_output.size[0]/2 and j >= img_output.size[1]/2:
                if i+(j-img_output.size[1]/2) < img_output.size[0]/2:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)
            if i >= img_output.size[0]/2 and j >= img_output.size[1]/2:
                if i >= j:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgFlip(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    npixels = img_output.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = pixels[i,j]
            if i < img_input.size[0]//2 and j < img_input.size[1]//2:
                npixels[i,j] = pixels[img_input.size[0] - 1 - i, img_input.size[1] - 1 - j]
            elif i < img_input.size[0]//2 and j > img_input.size[1]//2:
                npixels[i,j] = pixels[img_input.size[0] - 1 - i, j]
            elif i > img_input.size[0]//2 and j < img_input.size[1]//2:
                npixels[i,j] = pixels[i, img_input.size[1] - 1 - j]
            else:
                npixels[i,j] = pixels[i, j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgBlend(img_input, img_input2, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    npixels = img_output.load()
    img_input2 = img_input2.resize((img_input.size[0]//2, img_input.size[1]//2))
    pixels2 = img_input2.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = pixels[i,j]
            if i < img_input.size[0]//2 and j < img_input.size[1]//2:
                r2, g2, b2 = pixels2[i,j]
                npixels[i,j] = (r//2 + r2//2, g//2 + g2//2, b//2 + b2//2)
            else:
                npixels[i,j] = pixels[i,j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgBlendFlip(img_input, img_input2, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    npixels = img_output.load()
    img_input2 = img_input2.resize((img_input.size[0]//2, img_input.size[1]//2))
    pixels2 = img_input2.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = pixels[i,j]
            if i < img_input.size[0]//2 and j < img_input.size[1]//2:
                r2, g2, b2 = pixels2[i,j]
                npixels[i,j] = (r//2 + r2//2, g//2 + g2//2, b//2 + b2//2)
            else:
                npixels[i,j] = pixels[img_input.size[0] - 1 - i, j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgBlendFlip2(img_input, img_input2, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    npixels = img_output.load()
    img_input2 = img_input2.resize((img_input.size[0]//2, img_input.size[1]//2))
    pixels2 = img_input2.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = pixels[i,j]
            if i < img_input.size[0]//2 and j < img_input.size[1]//2:
                r2, g2, b2 = pixels2[i,j]
                npixels[i,j] = (r//2 + r2//2, g//2 + g2//2, b//2 + b2//2)
            else:
                npixels[i,j] = pixels[img_input.size[0] - 1 - i, img_input.size[1] - 1 - j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def ImgFourImages(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new("RGB", (img_input.size[0]*2, img_input.size[1]*2))
    npixels = img_output.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = img_input.getpixel((i, j))
            npixels[i, j] = (r, g, b)
            npixels[i, img_input.size[1]*2-1-j] = (r, g, b)
            npixels[img_input.size[0]*2-1-i, j] = (r, g, b)
            npixels[img_input.size[0]*2-1-i, img_input.size[1]*2-1-j] = (r, g, b)

    if coldepth==1:
        img_output = img_output.convert("1")
    elif coldepth==8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output



def ImgFour2(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (int(img_input.size[1]/2), int(img_input.size[0]/2)))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i*2, j*2))
            pixels[i, j] = (r, g, b)

    canvas = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    canvas_pixels = canvas.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_output.getpixel((i, j))
            canvas_pixels[i, j] = (r, g, b)
            canvas_pixels[img_output.size[0]*2-1-i, j] = (r, g, b)
            canvas_pixels[i, img_output.size[1]*2-1-j] = (r, g, b)
            r, g, b = img_output.getpixel((j, img_output.size[0]-i-1))
            canvas_pixels[i+img_output.size[0],
                            j+img_output.size[1]] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return canvas


def ImgWajib(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if (i - img_output.size[0]/2)**2 + (j - img_output.size[1]/2)**2 < (img_output.size[0]/2)**2:
                r, g, b = img_input.getpixel((i, j)) # The pixel coordinate, given as (i, j)
                pixels[i, j] = (255 - r, 255 - g, 255 - b)
                if abs(i - img_output.size[0]/2) + abs(j - img_output.size[1]/2) < img_output.size[0]/2:
                    r, g, b = img_input.getpixel((i, j)) # The pixel coordinate, given as (i, j)
                    pixels[i, j] = (r, g, b)
            else:
                r, g, b = img_input.getpixel((i, j)) # The pixel coordinate, given as (i, j)
                pixels[i,j]=(r,g,b)
                
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


def ImgBonus(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    pixelss = img_input.load()

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    radius_x = img_input.size[0]//2
    radius_y = img_input.size[1]//2

    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = pixelss[i, j]

            if i+j <= img_input.size[1]:
                if i < j:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                    if (i-img_input.size[0]//2)**2/radius_x**2 + (j-img_input.size[1]//2)**2/radius_y**2 <= 1:
                        r, g, b = img_input.getpixel((i, j))
                        pixels[i, j] = (r, g, b)
                        if abs(i - img_input.size[0]//2) + abs(j - img_input.size[1]//2) < img_input.size[0]//2:
                            pixels[i, j] = (255-r, 255-g, 255-b)
                    else:
                        pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)
                    if (i-img_input.size[0]//2)**2/radius_x**2 + (j-img_input.size[1]//2)**2/radius_y**2 <= 1:
                        r, g, b = img_input.getpixel((i, j))
                        pixels[i, j] = (255-r, 255-g, 255-b)
                        if abs(i - img_input.size[0]//2) + abs(j - img_input.size[1]//2) < img_input.size[0]//2:
                            pixels[i, j] = (r, g, b)
                    else:
                        pixels[i, j] = (r, g, b)

            elif i > j:
                pixels[i, j] = (255-r, 255-g, 255-b)
                if (i-img_input.size[0]//2)**2/radius_x**2 + (j-img_input.size[1]//2)**2/radius_y**2 <= 1:
                    r, g, b = img_input.getpixel((i, j))
                    pixels[i, j] = (r, g, b)
                    if abs(i - img_input.size[0]//2) + abs(j - img_input.size[1]//2) < img_input.size[0]//2:
                        pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (255-r, 255-g, 255-b)

            else:
                pixels[i, j] = (r, g, b)
                if (i-img_input.size[0]//2)**2/radius_x**2 + (j-img_input.size[1]//2)**2/radius_y**2 <= 1:
                    r, g, b = img_input.getpixel((i, j))
                    pixels[i, j] = (255-r, 255-g, 255-b)
                    if abs(i - img_input.size[0]//2) + abs(j - img_input.size[1]//2) < img_input.size[0]//2:
                        pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = (r, g, b)
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

def ImgMeanFiltering(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r1, g1, b1 = img_input.getpixel((i-1, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))
            r3, g3, b3 = img_input.getpixel((i, j-1))
            r4, g4, b4 = img_input.getpixel((i, j+1))
            r5, g5, b5 = img_input.getpixel((i-1, j-1))
            r6, g6, b6 = img_input.getpixel((i+1, j+1))
            r7, g7, b7 = img_input.getpixel((i-1, j+1))
            r8, g8, b8 = img_input.getpixel((i+1, j-1))
            r = (r+r1+r2+r3+r4+r5+r6+r7+r8)//9
            g = (g+g1+g2+g3+g4+g5+g6+g7+g8)//9
            b = (b+b1+b2+b3+b4+b5+b6+b7+b8)//9
            pixels[i, j] = (r, g, b)
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

def ImgMedianFiltering(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r1, g1, b1 = img_input.getpixel((i-1, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))
            r3, g3, b3 = img_input.getpixel((i, j-1))
            r4, g4, b4 = img_input.getpixel((i, j+1))
            r5, g5, b5 = img_input.getpixel((i-1, j-1))
            r6, g6, b6 = img_input.getpixel((i+1, j+1))
            r7, g7, b7 = img_input.getpixel((i-1, j+1))
            r8, g8, b8 = img_input.getpixel((i+1, j-1))
            r = sorted([r, r1, r2, r3, r4, r5, r6, r7, r8])[4]
            g = sorted([g, g1, g2, g3, g4, g5, g6, g7, g8])[4]
            b = sorted([b, b1, b2, b3, b4, b5, b6, b7, b8])[4]
            pixels[i, j] = (r, g, b)
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

def ImgMaxFiltering(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r1, g1, b1 = img_input.getpixel((i-1, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))
            r3, g3, b3 = img_input.getpixel((i, j-1))
            r4, g4, b4 = img_input.getpixel((i, j+1))
            r5, g5, b5 = img_input.getpixel((i-1, j-1))
            r6, g6, b6 = img_input.getpixel((i+1, j+1))
            r7, g7, b7 = img_input.getpixel((i-1, j+1))
            r8, g8, b8 = img_input.getpixel((i+1, j-1))
            r = max([r, r1, r2, r3, r4, r5, r6, r7, r8])
            g = max([g, g1, g2, g3, g4, g5, g6, g7, g8])
            b = max([b, b1, b2, b3, b4, b5, b6, b7, b8])
            pixels[i, j] = (r, g, b)
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output

def ImgMinFiltering(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r1, g1, b1 = img_input.getpixel((i-1, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))
            r3, g3, b3 = img_input.getpixel((i, j-1))
            r4, g4, b4 = img_input.getpixel((i, j+1))
            r5, g5, b5 = img_input.getpixel((i-1, j-1))
            r6, g6, b6 = img_input.getpixel((i+1, j+1))
            r7, g7, b7 = img_input.getpixel((i-1, j+1))
            r8, g8, b8 = img_input.getpixel((i+1, j-1))
            r = min([r, r1, r2, r3, r4, r5, r6, r7, r8])
            g = min([g, g1, g2, g3, g4, g5, g6, g7, g8])
            b = min([b, b1, b2, b3, b4, b5, b6, b7, b8])
            pixels[i, j] = (r, g, b)
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


def WeightMeanFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    koef1 = 2
    koef2 = 4

    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))  # tengah
            r2, g2, b2 = img_input.getpixel((i-1, j-1))  # kiri atas
            r3, g3, b3 = img_input.getpixel((i-1, j))  # kiri
            r4, g4, b4 = img_input.getpixel((i-1, j+1))  # kiri bawah
            r5, g5, b5 = img_input.getpixel((i, j-1))  # tengah atas
            r6, g6, b6 = img_input.getpixel((i, j+1))  # tengah bawah
            r7, g7, b7 = img_input.getpixel((i+1, j-1))  # kanan atas
            r8, g8, b8 = img_input.getpixel((i+1, j))  # kanan
            r9, g9, b9 = img_input.getpixel((i+1, j+1))  # kanan bawah
            r_list = [r*koef2, r2, r3*koef1, r4,
                      r5*koef1, r6*koef1, r7, r8*koef1, r9]
            g_list = [g*koef2, g2, g3*koef1, g4,
                      g5*koef1, g6*koef1, g7, g8*koef1, g9]
            b_list = [b*koef2, b2, b3*koef1, b4,
                      b5*koef1, b6*koef1, b7, b8*koef1, b9]
            r_mean = sum(r_list)//16
            g_mean = sum(g_list)//16  # karena 16 adalah jumlah koefisien
            b_mean = sum(b_list)//16
            pixels[i, j] = (r_mean, g_mean, b_mean)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def WeightMeanFilter2(img_input, coldepth):
    if coldepth != 25:
        img_input = img_input.convert("RGB")
        input_pixels = img_input.load()

        output_image = Image.new(
            'RGB', (img_input.size[0], img_input.size[1]))
        output_pixels = output_image.load()

    box_kernel = [
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9]]

    kernel = box_kernel
    offset = len(kernel)//2

    for x in range(offset, img_input.size[0] - offset):
        for y in range(offset, img_input.size[1] - offset):
            acc = [0, 0, 0]
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    acc[0] += pixel[0] * kernel[a][b]
                    acc[1] += pixel[1] * kernel[a][b]
                    acc[2] += pixel[2] * kernel[a][b]
            output_pixels[x, y] = (int(acc[0]), int(acc[1]), int(acc[2]))
    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image


def Gradien1Filter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    pixels_x = img_output.load()
    pixels_y = img_output.load()

    mask = [-1, 1]
    # mask2 = [1, -1]

    for i in range(img_input.size[0]-1):
        for j in range(img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))  # kanan
            r3, g3, b3 = img_input.getpixel((i, j+1))  # bawah

            # print(r2)

            r_sum_x = (r*mask[0])+(r2*mask[1])
            g_sum_x = (g*mask[0])+(g2*mask[1])
            b_sum_x = (b*mask[0])+(b2*mask[1])
            pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

            r_sum_y = (r*mask[1])+(r3*mask[0])
            g_sum_y = (g*mask[1])+(g3*mask[0])
            b_sum_y = (b*mask[1])+(b3*mask[0])
            pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

            r_sum_xy = (abs(r_sum_x))+(abs(r_sum_y))
            g_sum_xy = (abs(g_sum_x))+(abs(g_sum_y))
            b_sum_xy = (abs(b_sum_x))+(abs(b_sum_y))
            pixels[i, j] = (r_sum_xy, g_sum_xy, b_sum_xy)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def CenterDifFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels_x = img_output.load()
    pixels_y = img_output.load()
    pixels = img_output.load()

    mask = [-1, 0, 1]
    # mask2 = [1, 0, -1]

    for i in range(img_input.size[0]-2):
        for j in range(img_input.size[1]-2):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))  # kanan
            r3, g3, b3 = img_input.getpixel((i+2, j))  # kanan2
            r4, g4, b4 = img_input.getpixel((i, j+1))  # bawah
            r5, g5, b5 = img_input.getpixel((i, j+2))  # bawah2

            # print(r2)
            r_sum_x = (r*mask[0])+(r2*mask[1])+r3*mask[2]
            g_sum_x = (g*mask[0])+(g2*mask[1])+g3*mask[2]
            b_sum_x = (b*mask[0])+(b2*mask[1])+b3*mask[2]
            pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

            r_sum_y = (r*mask[2])+(r4*mask[1])+r5*mask[0]
            g_sum_y = (g*mask[2])+(g4*mask[1])+g5*mask[0]
            b_sum_y = (b*mask[2])+(b4*mask[1])+b5*mask[0]
            pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

            r_sum_xy = (abs(r_sum_x))+(abs(r_sum_y))
            g_sum_xy = (abs(g_sum_x))+(abs(g_sum_y))
            b_sum_xy = (abs(b_sum_x))+(abs(b_sum_y))
            pixels[i, j] = (r_sum_xy, g_sum_xy, b_sum_xy)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def SobelFilter(img_input, coldepth):
    if coldepth != 25:
        img_input = img_input.convert("RGB")
        input_pixels = img_input.load()

        output_image = Image.new(
            'RGB', (img_input.size[0], img_input.size[1]))
        output_pixels = output_image.load()

    box_kernel_x = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]]

    box_kernel_y = [
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]]

    kernel_x = box_kernel_x
    kernel_y = box_kernel_y
    offset = len(kernel_x)//2

    for x in range(offset, img_input.size[0] - offset):
        for y in range(offset, img_input.size[1] - offset):
            pixel_sx = [0, 0, 0]
            pixel_sy = [0, 0, 0]

            for a in range(len(kernel_x)):
                for b in range(len(kernel_x)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    pixel_sx[0] += pixel[0] * kernel_x[a][b]
                    pixel_sx[1] += pixel[1] * kernel_x[a][b]
                    pixel_sx[2] += pixel[2] * kernel_x[a][b]

                    pixel_sy[0] += pixel[0] * kernel_y[a][b]
                    pixel_sy[1] += pixel[1] * kernel_y[a][b]
                    pixel_sy[2] += pixel[2] * kernel_y[a][b]

            r_sum = abs(pixel_sx[0])+abs(pixel_sy[0])
            g_sum = abs(pixel_sx[1])+abs(pixel_sy[1])
            b_sum = abs(pixel_sx[2])+abs(pixel_sy[2])

            output_pixels[x, y] = (r_sum, g_sum, b_sum)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image


def PrewittFilter(img_input, coldepth):
    if coldepth != 25:
        img_input = img_input.convert("RGB")
        input_pixels = img_input.load()

        output_image = Image.new(
            'RGB', (img_input.size[0], img_input.size[1]))
        output_pixels = output_image.load()

    box_kernel_x = [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]]

    box_kernel_y = [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]]

    kernel_x = box_kernel_x
    kernel_y = box_kernel_y
    offset = len(kernel_x)//2

    for x in range(offset, img_input.size[0] - offset):
        for y in range(offset, img_input.size[1] - offset):
            pixel_sx = [0, 0, 0]
            pixel_sy = [0, 0, 0]

            for a in range(len(kernel_x)):
                for b in range(len(kernel_x)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    pixel_sx[0] += pixel[0] * kernel_x[a][b]
                    pixel_sx[1] += pixel[1] * kernel_x[a][b]
                    pixel_sx[2] += pixel[2] * kernel_x[a][b]

                    pixel_sy[0] += pixel[0] * kernel_y[a][b]
                    pixel_sy[1] += pixel[1] * kernel_y[a][b]
                    pixel_sy[2] += pixel[2] * kernel_y[a][b]

            r_sum = abs(pixel_sx[0])+abs(pixel_sy[0])
            g_sum = abs(pixel_sx[1])+abs(pixel_sy[1])
            b_sum = abs(pixel_sx[2])+abs(pixel_sy[2])

            output_pixels[x, y] = (r_sum, g_sum, b_sum)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image


def RobertFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    pixels_x = img_output.load()
    pixels_y = img_output.load()

    mask = [1, -1]
    # mask2 = [-1, 1]

    for i in range(img_input.size[0]-1):
        for j in range(img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))  # kanan
            r3, g3, b3 = img_input.getpixel((i, j+1))  # bawah
            r4, g4, b4 = img_input.getpixel((i+1, j+1))  # kanan bawah

            # print(r2)

            r_sum_x = (r*mask[0])+(r4*mask[1])
            g_sum_x = (g*mask[0])+(g4*mask[1])
            b_sum_x = (b*mask[0])+(b4*mask[1])
            pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

            r_sum_y = (r2*mask[0])+(r3*mask[1])
            g_sum_y = (g2*mask[0])+(g3*mask[1])
            b_sum_y = (b2*mask[0])+(b3*mask[1])
            pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

            r_sum_xy = (abs(r_sum_x))+(abs(r_sum_y))
            g_sum_xy = (abs(g_sum_x))+(abs(g_sum_y))
            b_sum_xy = (abs(b_sum_x))+(abs(b_sum_y))
            pixels[i, j] = (r_sum_xy, g_sum_xy, b_sum_xy)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def LaplacianFilter(img_input, coldepth):
    if coldepth != 25:
        img_input = img_input.convert("RGB")
        input_pixels = img_input.load()

        output_image = Image.new(
            'RGB', (img_input.size[0], img_input.size[1]))
        output_pixels = output_image.load()

        # output_image_2 = Image.new(
        #     'RGB', (img_input.size[0], img_input.size[1]))
        # output_pixels_2 = output_image_2.load()

    # laplacian filter memiliki 4 box kernel
    # akan digunakan salah 1 dari box kernel tersebut
    box_kernel = [
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]]

    # box_kernel = [
    #     [-1, -1, -1],
    #     [-1, 8, -1],
    #     [-1, -1, -1]]

    # box_kernel = [
    #     [1, -2, 1],
    #     [-2, 4, -2],
    #     [1, -2, 1]]

    # box_kernel = [
    #     [1, 4, 1],
    #     [4, -20, 4],
    #     [1, 4, 1]]

    kernel = box_kernel
    offset = len(kernel)//2

    for x in range(offset, img_input.size[0] - offset):
        for y in range(offset, img_input.size[1] - offset):
            pixel_sx = [0, 0, 0]

            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    pixel_sx[0] += pixel[0] * kernel[a][b]
                    pixel_sx[1] += pixel[1] * kernel[a][b]
                    pixel_sx[2] += pixel[2] * kernel[a][b]

            output_pixels[x, y] = (pixel_sx[0], pixel_sx[1], pixel_sx[2])

    # # applying the filter
    # for i in range(offset, img_input.size[0] - offset):
    #     for j in range(offset, img_input.size[1] - offset):
    #         r, g, b = img_input.getpixel((i, j))
    #         r2, g2, b2 = output_image_2.getpixel((i, j))
    #         r_sum = r - r2
    #         g_sum = g - g2
    #         b_sum = b - b2
    #         output_pixels_2[i, j] = (r_sum, g_sum, b_sum)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image