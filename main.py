from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


BACKGROUND_COLOR = "#B1DDC6"
BASE_WIDTH = 350
new_img = []


def mark_image():
    txt = []
    path = upload_file()


    def take_text():

        txt.append(txt_field.get("1.0", "end-1c"))
        print(txt[0])


    def put_watermark():
        print(path)
        img_pil_wat = Image.open(path)
        draw = ImageDraw.Draw(img_pil_wat)
        font = ImageFont.truetype('ariblk.ttf', size=250)
        draw.text((0, 0), txt[0], (255, 255, 255), font=font)
        print('watermarking with: ', txt[0])
        img_water = read_image(img_pil_wat)
        image_label.config(image=img_water)
        image_label.grid(row=0, column=0, columnspan=3)
        img_pil_wat.save('sample-out.jpg')



    window_marker = Toplevel()
    window_marker.title('Image watermarker')
    window_marker.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    img_pil = Image.open(path)

    img = read_image(img_pil)

    image_label = Label(window_marker, image=img)
    image_label.grid(row=0, column=0, columnspan=3)

    txt_field = Text(window_marker, height=5, width=50)
    txt_field.grid(row=1, column=1)

    get_txt = Button(window_marker, text='Take text', command=lambda: take_text())
    get_txt.grid(row=1, column=2)

    txt_btn = Button(window_marker, text='Put watermark', command=lambda: put_watermark())
    txt_btn.grid(row=2, column=1)


    window_marker.mainloop()





def upload_file():
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
    return filedialog.askopenfilename(filetypes=f_types)


def read_image(img):
    # resize the image so that it is not so big. from now on use this variable
    img = img.resize((BASE_WIDTH, int(BASE_WIDTH * img.size[1] / img.size[0])))
    # put_watermark('K.T.')

    img = ImageTk.PhotoImage(img)
    return img


# ---------------------- UI SETUP --------------------#
window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = PhotoImage(file='card_back.png')
card_image = canvas.create_image(400, 263, image=image)
word_text = canvas.create_text(400, 263, text="Welcome to Image Auto-Watermarker", font=('Arial', 30, 'bold'))

canvas.grid(row=0, column=0, columnspan=1)
load_image_but = Button(text='Click here to upload image', command=mark_image)
load_image_but.grid(row=1, column=0)

window.mainloop()

# show_image('me.jpg')