import tkinter as tk
from PIL import Image
from tkinter import *
from tkinter import filedialog

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Converter")

        # create widgets
        self.file_path_label = tk.Label(master, text="No file selected")
        self.select_button = tk.Button(master, text="Select Image", command=self.select_file)
        self.mode_label = tk.Label(master, text="Select conversion mode:")
        self.mode_var = tk.StringVar(value="7")
        self.mode_entry = tk.Entry(master, textvariable=self.mode_var)
        self.convert_button = tk.Button(master, text="Convert", command=self.convert_image)

        # grid layout
        self.file_path_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.select_button.grid(row=1, column=0, padx=10, pady=10)
        self.mode_label.grid(row=2, column=0, padx=10, pady=10)
        self.mode_entry.grid(row=2, column=1, padx=10, pady=10)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.file_path_label.configure(text=file_path)
            self.file_path = file_path

    def convert_image(self):
        try:
            mode = self.mode_var.get()
            img = Image.open(self.file_path)
            converted_img = img.convert(mode)
            converted_img.show()
            
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                converted_img.save(r"C:\Users\TK\Desktop\image stegno\converted_image.png")
        except AttributeError:
            # no image selected
            pass

root = tk.Tk()
app = ImageConverterApp(root)
root.mainloop()
