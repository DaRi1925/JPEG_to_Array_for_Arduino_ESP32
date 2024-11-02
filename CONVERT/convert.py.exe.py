from tkinter import Tk, Button, Label, filedialog
from PIL import Image

def convert_image_to_array(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize((240, 320))
    pixels = list(img.getdata())
    array = []

    for pixel in pixels:
        r, g, b = pixel
        rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
        array.append(rgb565)

    return array

def choose_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    if filename:
        array = convert_image_to_array(filename)
        with open('image_array.txt', 'w') as f:
            for i, val in enumerate(array):
                if i % 16 == 0:
                    f.write('\n')
                f.write(f'0x{val:04X}, ')

        status_label.config(text="Image converted successfully!")

# Создаем графический интерфейс с кнопкой "Выбрать изображение" и меткой для вывода статуса
root = Tk()
root.title("Image to Array Converter")
root.geometry("300x150")

choose_button = Button(root, text="Выбрать изображение", command=choose_image)
choose_button.pack(pady=20)

status_label = Label(root, text="")
status_label.pack()

root.mainloop()
