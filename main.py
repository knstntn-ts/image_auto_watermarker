##### IMPORT STATEMENTS
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

##### CONSTATNS AND VARIABLES FOR HOLDING DATA
BACKGROUND_COLOR = "#B1DDC6"
BASE_WIDTH = 350

##### FUNCTIONS

#### Main function to load, mark and output the image
def mark_image():
    txt = []
    path = upload_file()

    ### Function to grab the text from the text field
    def take_text():
        txt.append(txt_field.get("1.0", "end-1c"))

    ### Function to put the watermark to the input image
    def put_watermark():

        take_text()

        # write text on the image
        img_pil_wat = Image.open(path)
        draw = ImageDraw.Draw(img_pil_wat)

        # Custom font for the text
        font = ImageFont.truetype('ariblk.ttf', size=50)
        draw.text((0, 0), txt[0], (0, 0, 0), font=font)

        # Save the image with watermark
        img_pil_wat.save('sample-out.jpg')

        # Show the watermarked image
        # Note that this will probably open the image with your default program for viewing the image.
        # Code will continue to run after you close your image viewer.
        img_pil_wat.show()

        # Close the window for watermarking
        window_marker.destroy()

        # Update the text on the main screen
        canvas.itemconfig(word_text, text='Your watermarked image is ready.\n Check local directory.')

    # --- Open new window for adding the watermark --- #
    # Note: This allows to run the program continuously after finishing with one file
    window_marker = Toplevel()
    window_marker.title('Image watermarker')
    window_marker.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    img_pil = Image.open(path)

    # Display image
    img = read_image(img_pil)

    image_label = Label(window_marker, image=img)
    image_label.grid(row=0, column=0, columnspan=3)

    # Field for getting text for watermark
    txt_field = Text(window_marker, height=5, width=50)
    txt_field.grid(row=1, column=1)

    # Button for putting the watermark
    txt_btn = Button(window_marker, text='Put watermark', command=lambda: put_watermark())
    txt_btn.grid(row=2, column=1)

    window_marker.mainloop()


### Function for taking the input image
def upload_file():
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]

    return filedialog.askopenfilename(filetypes=f_types)


### Function for reading image in an appropriate format
def read_image(img):
    # Resize the image so that it is not so big. From now on use this variable
    img = img.resize((BASE_WIDTH, int(BASE_WIDTH * img.size[1] / img.size[0])))

    # Return in the format for tkinter
    img = ImageTk.PhotoImage(img)

    return img


# ---------------------- UI SETUP --------------------#
window = Tk()
window.title('Watermarker')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# --- Some nice background setup --- #
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = PhotoImage(file='card_back.png')
card_image = canvas.create_image(400, 263, image=image)
word_text = canvas.create_text(400, 263, text="Welcome to Image Auto-Watermarker", font=('Arial', 30, 'bold'))

canvas.grid(row=0, column=0, columnspan=1)
load_image_but = Button(text='Click here to upload image', command=mark_image)
load_image_but.grid(row=1, column=0)

window.mainloop()
