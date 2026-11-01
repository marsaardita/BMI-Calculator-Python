from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title('Tkinter.com - BMI Calculator')
root.geometry("600x600")

#Define Our Image
meter = ImageTk.PhotoImage(Image.open("c:/Users/Hp/Documents/KULIAH/PROJECT OPREC ASLAB LEPKOM/BMI/bmi_categories.png"))
meter_img = Label(root, image=meter, bd=0)
meter_img.pack(pady=40)

def clear_screen():
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.config(text="")

def get_bmi():
    # Menghitung BMI
    # Rumus BMI = our_weight (kg) / ((our_height_cm (cm) / 100) (m^2) ** 2)
    our_height_cm = int(h_entry.get())
    our_height = our_height_cm / 100
    our_weight = int(w_entry.get())
    bmi = (our_weight / (our_height ** 2))
    bmi_rounded = round(bmi, 1)
    
    results.configure(text=f"{str(bmi_rounded)}")

    # Menambahkan warna menyesuaikan kategori
    if bmi_rounded < 18.5:
        results.configure(text=f"{str(bmi_rounded)}\nUnderweight", text_color="#7ED957")
    elif bmi_rounded >= 18.5 and bmi_rounded <= 24.9:
        results.configure(text=f"{str(bmi_rounded)}\nNormal", text_color="#20C056")
    elif bmi_rounded >= 25.0 and bmi_rounded <= 29.9:
        results.configure(text=f"{str(bmi_rounded)}\nOverweight", text_color="#FFDE59")
    elif bmi_rounded >= 30.0 and bmi_rounded <= 34.9:
        results.configure(text=f"{str(bmi_rounded)}\nObese", text_color="#FF6E4F")
    elif bmi_rounded >= 35:
        results.configure(text=f"{str(bmi_rounded)}\nExtreme Obese", text_color="#F90303")    

#Define Entry Boxes
h_entry = customtkinter.CTkEntry(master=root,
    placeholder_text="Height In Centimeters",
    width=200,
    height=30, 
    border_width=2)
h_entry.pack(pady=20)

w_entry = customtkinter.CTkEntry(master=root,
    placeholder_text="Weight In Kilograms",
    width=200,
    height=30, 
    border_width=2)
w_entry.pack(pady=5)

#Buttons
button_1 = customtkinter.CTkButton(master=root,
    text="Calculate BMI",
    width=190,
    height=40,
    corner_radius=20,
    compound="top",
    command=get_bmi)
button_1.pack(pady=5)


button_2 = customtkinter.CTkButton(master=root,
    text="Clear",
    width=190,
    height=40,
    corner_radius=20,
    fg_color="#D35B58",
    hover_color="#C77C78",
    command=clear_screen)
button_2.pack(pady=5)

#Result
results = customtkinter.CTkLabel(master=root, text="",
    width=250,
    height=40,
    font=("Arial", 24))
results.pack(pady=20)

root.mainloop()
