from re import T
import PySimpleGUI as sg
import os.path
from PIL import Image, ImageOps
from processing_list import *

# Kolom Area No 1: Area open folder, select image, information
file_list_column = [
    [
        sg.Text("Open Image Folder :"),
    ],
    [
        sg.In(size=(20, 1), enable_events=True, key="ImgFolder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Choose an image from list :"),
    ],
    [
        sg.Listbox(values=[], enable_events=True, size=(18, 10), key="ImgList")
    ],
    [
        sg.Text("Image Input 2:"),
    ],
    [
        sg.In(size=(20, 1), enable_events=True, key="inputImage2"),
        sg.FileBrowse(),
    ],
    [
        sg.Text("Image Information:"),
    ],
    [
        sg.Text(size=(20, 1), key="ImgSize"),
    ],
    [
        sg.Text(size=(20, 1), key="ImgColorDepth"),
    ],

]

# membuat kolom area 2 : area viewer image input

image_viewer_column = [
    # ukuran citra perlu akses sehingga butuh key
    [sg.Text(size=(20, 1), key="ImgSize")],

    # color depth berapa jumlah bit yang digunakan untuk menyimpan citra
    [sg.Text(size=(20, 1), key="ImgColorDepth")],
    # menampilkan text masukkan gambar
    [sg.Text("Image Input : ")],

    # mengakses path dimana citra itu berada,
    # akan berubah2 tergantung path yang dipilih oleh citranya
    [sg.Text(size=(40, 1), key="FilepathImgInput")],

    # menampung dan menampilkan citra
    [sg.Image(key="ImgInputViewer")],
]

# membuat kolom area 3 : Area image info dan tombol list of processing

list_processing = [

    [sg.Text("List Processing :")],
    [sg.Button("Negative", size=(20, 1), key="ImgNegative"), sg.Button("Logaritmic", size=(20, 1), key="ImgLogaritmic")],    
    
    [sg.Button("Power law", size=(20, 1), key="ImgPowerLaw"),sg.Button("Threshold", size=(20, 1), key="ImgThreshold")],
    
    [sg.HSeparator()],
    [sg.Text("Image Brightness Slider:"), ],
    [  # slider brightness
        sg.Slider(range=(-255, 255), size=(19, 20),
                    orientation='h',
                    key="SliderBrightness",
                    default_value=0), sg.Button("Image Brightness", size=(20, 1), key="ImgBrightness")],
    [sg.HSeparator()],
    [sg.Text("Image Rotate:"),sg.Button("90°", size=(9, 1), key="ImgRotate90"),
        sg.Button("180°", size=(9, 1), key="ImgRotate180"),sg.Button("270°", size=(9, 1), key="ImgRotate270") ],
    [sg.HSeparator()],
    [sg.Text("Image Flipping:"),sg.Button("Vertikal", size=(9, 1), key="ImgFlippingVertikal"),
        sg.Button("Horizontal", size=(9, 1), key="ImgFlippingHorizontal"),sg.Button("Vertikal Horizontal  ", size=(
        9, 2), key="ImgFlippingVerHor") ],
    [sg.HSeparator()],
    [sg.Text("Image Translation:"),sg.Button("X", size=(9, 1), key="ImgTranslasiX"),
        sg.Button("Y", size=(9, 1), key=("ImgTranslasiY"))],
    [sg.HSeparator()],
    [sg.Text("Image Scalling:"),sg.Button("Zoom", size=(9, 1), key="ImgZoom"), sg.Button(
        "Shrinking", size=(9, 1), key="ImgShrinking")],
    [sg.HSeparator()],
    [sg.Text("Percobaan :")],
    [sg.Button("ImgCircle", size=(20, 1), key="ImgCircle"),sg.Button("ImgRhombus", size=(20, 1), key="ImgRhombus")],
    [sg.Button("Half Gray", size=(20, 1), key="RGBtoGrayscale"),sg.Button("ImgCross", size=(20, 1), key="ImgCross")],
    [sg.Button("Blending Biasa", size=(20, 1), key="ImgBlending"),sg.Button("Blend Kecil Atas", size=(20, 1), key="ImgBlend")],
    [sg.Button("Blend Flip Ver", size=(20, 1), key="ImgBlendFlip"),sg.Button("Blend Flip Hor", size=(20, 1), key="ImgBlendFlip2")],
    [sg.Button("4 gambar", size=(20, 1), key="ImgFourImages"),  sg.Button("4 gambar 2", size=(20, 1), key="ImgFour2")],
    [sg.HSeparator()],
    [sg.Text("Neighborhood :")],
    [sg.Button("ImgMeanFiltering", size=(20, 1), key="ImgMeanFiltering"), sg.Button("ImgMedianFiltering", size=(20, 1), key="ImgMedianFiltering")],
    [sg.Button("ImgMaxFiltering", size=(20, 1), key="ImgMaxFiltering"), sg.Button("ImgMinFiltering", size=(20, 1), key="ImgMinFiltering")],
    [sg.Text("Ujian Tengah Semester :")],
    [sg.Button("ImgWajib", size=(20, 1), key="ImgWajib"), sg.Button("ImgBonus", size=(20, 1), key="ImgBonus")],
    [sg.HSeparator()],
    [
        sg.Button("Weight Filter", size=(20, 1), key="WeightMeanFilter"),
        sg.Button("Gradien1 Operator", size=(20, 1), key="Gradien1Filter"),
    ],
    [
        sg.Button("CenterDif Operator", size=(20, 1), key="CenterDifFilter"),
        sg.Button("Sobel Operator", size=(20, 1), key="SobelFilter"),
    ],
    [
        sg.Button("Prewitt Operator", size=(20, 1), key="PrewittFilter"),
        sg.Button("Robert Operator", size=(20, 1), key="RobertFilter"),
    ],
    [
        sg.Button("Laplacian Operator", size=(20, 1), key="LaplacianFilter"),
        # sg.Button("Kompas Operator", size=(20, 1), key="KompasFilter"),
    ]
]

# membuat kolom area 4 : area viewer image output
image_viewer_column2 = [
    [sg.Text("Image Output:")],
    [sg.Text(size=(40, 1), key="ImgProcessingType")],
    [sg.Image(key="ImgOutputViewer")],
]

# menggabungkan keempat kolom area
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
        sg.VSeparator(),
        sg.Column(list_processing),
        sg.VSeparator(),
        sg.Column(image_viewer_column2),
    ]
]


# run windows atau tampilan ui
window = sg.Window("Mini Image Editor", layout)
# nama image file temporary setiap kali processing output
filename_out = "out.png"

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # folder name was filled in, make a list of files in the folder
    if event == "ImgFolder":
        folder = values["ImgFolder"]

        try:
            # get list of the files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif",))
        ]

        window["ImgList"].update(fnames)

    elif event == "ImgList":  # A file wa choosen from the  listbox
        try:
            filename = os.path.join(
                values["ImgFolder"], values["ImgList"][0]
            )
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename)
            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename)
            img_input = Image.open(filename)
            # img_input.show()

            # Size
            img_width, img_height = img_input.size
            window["ImgSize"].update(
                # "Image Size : "+str(img_width)+" x "+str(img_height))
                "Image Size : "+str(img_height)+" x "+str(img_width))

            # Color depth
            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB":
                                24, "HSV": 24, "I": 32, "F": 32}
            coldepth = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth"].update("Color Depth : "+str(coldepth))
        except:
            pass
    elif event == "ImgNegative":

        try:
            window["ImgProcessingType"].update("Image Negative")
            img_output = ImgNegative(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass
    
    elif event == "ImgRotate90":

        try:
            window["ImgProcessingType"].update("Image Rotate 90°")
            img_output = ImgRotate90(img_input, coldepth, 90, "C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "RGBtoGrayscale":
        
        try:
            window["ImgProcessingType"].update("RGB to Grayscale")
            img_output=RGBtoGrayscale (img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgRotate180":
        try:
            window["ImgProcessingType"].update("Image Rotate 180°")
            img_output = ImgRotate180(img_input, coldepth, 180, "C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "ImgRotate270":
        try:
            window["ImgProcessingType"].update("Image Rotate 270°")
            img_output = ImgRotate270(img_input, coldepth, 270, "C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "ImgBrightness":

        try:
            value = int(values["SliderBrightness"])
            window["ImgProcessingType"].update("Image Brightness")
            img_output = ImgBrightness(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgBlending":

        try:
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            window["ImgProcessingType"].update("Image  Blending")
            img_output = ImgBlending(img_input, input_image2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgLogaritmic":

        try:
            window["ImgProcessingType"].update("Image Logaritmic")
            img_output = ImgLogaritmic(img_input, coldepth, 30)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgPowerLaw":

        try:
            window["ImgProcessingType"].update("Image Power Law")
            img_output = ImgPowerLaw(img_input, coldepth, 4)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgThreshold":

        try:
            window["ImgProcessingType"].update("Image Threshold")
            img_output = ImgThreshold(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlippingVertikal":

        try:
            window["ImgProcessingType"].update("Image Flip Vertikal")
            img_output = ImgFlippingVertikal(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlippingHorizontal":

        try:
            window["ImgProcessingType"].update("Image Flip Horizontal")
            img_output = ImgFlippingHorizontal(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
        
    elif event == "ImgFlippingVerHor":

        try:
            window["ImgProcessingType"].update("Image Flip ")
            img_output = ImgFlippingVerHor(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgTranslasiX":

        try:
            window["ImgProcessingType"].update("Image Translasi")
            img_output = ImgTranslasi(img_input, coldepth, "x")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgTranslasiY":
        try:
            window["ImgProcessingType"].update("Image Translasi")
            img_output = ImgTranslasi(img_input, coldepth, "y")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgZoom":
        try:
            window["ImgProcessingType"].update("Zoom ")
            img_output = ImgZoom(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgShrinking":
        try:
            window["ImgProcessingType"].update("Shrinking")
            img_output = ImgShrinking(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgRhombus":

        try:
            window["ImgProcessingType"].update("Image Wajik Negative")
            img_output = ImgRhombus(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass
    elif event == "ImgCircle":

        try:
            window["ImgProcessingType"].update("Image Circle Negative")
            img_output = ImgCircle(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "ImgFourImages":

        try:
            window["ImgProcessingType"].update("ImgFourImages")
            img_output = ImgFourImages(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "ImgBlendFlip":

        try:
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            window["ImgProcessingType"].update("Image  Blending Flip Vertikal")
            img_output = ImgBlendFlip(img_input, input_image2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgBlendFlip2":

        try:
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            window["ImgProcessingType"].update("Image  Blending Flip Horizontal")
            img_output = ImgBlendFlip2(img_input, input_image2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgBlend":

        try:
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            window["ImgProcessingType"].update("Image  Blending2")
            img_output = ImgBlend(img_input, input_image2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgFour2":

        try:
            window["ImgFour2"].update("ImgFour2")
            img_output = ImgFour2(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgCross":

        try:
            window["ImgCross"].update("ImgCross")
            img_output = ImgCross(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
        
    elif event == "ImgWajib":

        try:
            window["ImgWajib"].update("ImgWajib")
            img_output = ImgWajib(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
        
    elif event == "ImgBonus":

        try:
            window["ImgBonus"].update("ImgBonus")
            img_output = ImgBonus(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    #make a function to output neighborhood operation Satistical filtering
    elif event == "ImgMeanFiltering":

        try:
            window["ImgProcessingType"].update("Mean Filtering")
            img_output = ImgMeanFiltering(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
        #make a function to output Img Median Filtering
    elif event == "ImgMedianFiltering":
            
        try:
            window["ImgProcessingType"].update("Median Filtering")
            img_output = ImgMedianFiltering(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
            #make a function to output Img Max Filtering
    elif event == "ImgMaxFiltering":
                
        try:
            window["ImgProcessingType"].update("Max Filtering")
            img_output = ImgMaxFiltering(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                #make a function to output Img Min Filtering
    elif event == "ImgMinFiltering":
                        
        try:
            window["ImgProcessingType"].update("Min Filtering")
            img_output = ImgMinFiltering(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                #make a function to output WeightMeanFilter
    elif event == "WeightMeanFilter":
                        
        try:
            window["ImgProcessingType"].update("WeightMeanFilter")
            img_output = WeightMeanFilter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                #make a function to output WeightMeanFilter2
    elif event == "WeightMeanFilter2":
                        
        try:
            window["ImgProcessingType"].update("WeightMeanFilter2")
            img_output = WeightMeanFilter2(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                #make a function to output Gradien1Filter
    elif event == "Gradien1Filter":
                        
        try:
            window["ImgProcessingType"].update("Gradien1Filter")
            img_output = Gradien1Filter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                #make a function to output CenterDifFilter
    elif event == "CenterDifFilter":
                        
        try:
            window["ImgProcessingType"].update("CenterDifFilter")
            img_output = CenterDifFilter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                #make a function to output SobelFilter
    elif event == "SobelFilter":
                        
        try:
            window["ImgProcessingType"].update("SobelFilter")
            img_output = SobelFilter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                    #make a function to output PrewittFilter
    elif event == "PrewittFilter":
                        
        try:
            window["ImgProcessingType"].update("PrewittFilter")
            img_output = PrewittFilter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                #make a function to output RobertFilter
    elif event == "RobertFilter":
                        
        try:
            window["ImgProcessingType"].update("RobertFilter")
            img_output = RobertFilter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
                #make a function to output LaplacianFilter
    elif event == "LaplacianFilter":
                        
        try:
            window["ImgProcessingType"].update("LaplacianFilter")
            img_output = LaplacianFilter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
window.close()