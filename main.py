from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image


window = Tk()
window.title("Secret Note")
window.config(background="gray")
window.minsize(width=400, height=300)


my_image = Image.open("output.png",)
my_image_tk = ImageTk.PhotoImage(my_image)
image_label = Label(window, image=my_image_tk)
image_label.pack()
image_label.config(bg="gray")





enter_title = Label(window, text="Enter your title", fg="black", bg="gray")
enter_title_entry = Entry(width=25)
enter_title.pack()
enter_title_entry.pack()

user_mesage_label = Label(text="Enter Your Secret Mesage", fg="black", bg="gray")
user_mesage_label.pack()
user_mesage_title = Text(height=20, width=40)
user_mesage_title.pack()

user_enter_key = Label(text="Enter Your Secret Key", fg="black", bg="gray")
user_enter_key.pack()
user_enter_key_entry = Entry(width=25)
user_enter_key_entry.pack()


def new_create_file():
    with open("secret.txt", "w") as file:
        file.write(f"{enter_title_entry.get()}:")
        file.write("\n",)
        file.write("\t")
        file.write(user_mesage_title.get("1.0",END))





save_encrypt_button = Button(text="Save & Encrypted ", fg="black", bg="light gray",command=new_create_file)
save_encrypt_button.config(padx=20)
save_encrypt_button.pack(pady=10)



decrypt_button = Button(text="Decrypt", fg="black", bg="light gray",)
decrypt_button.pack()



window.mainloop()