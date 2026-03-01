from tkinter import *
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





enter_title = Label(window, text="Secret Note", fg="black", bg="gray")
enter_title_entry = Entry(width=25)
enter_title.pack()
enter_title_entry.pack()

user_mesage_label = Label(text="Enter your secret mesage", fg="black", bg="gray")
user_mesage_label.pack()
user_mesage_title = Text(height=20, width=40)
user_mesage_title.pack()

user_enter_key = Label(text="Enter your secret key", fg="black", bg="gray")
user_enter_key.pack()
user_enter_key_entry = Entry(width=25)
user_enter_key_entry.pack()

save_encrypt_button = Button(text="Save & Encrypted ", fg="black", bg="light gray",)
save_encrypt_button.config(padx=20)
save_encrypt_button.pack(pady=10)

decrypt_button = Button(text="Decrypt", fg="black", bg="light gray",)
decrypt_button.pack()



window.mainloop()