from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from cryptography.fernet import Fernet


window = Tk()
window.title("Secret Note")
window.config(background="gray")
window.minsize(width=400, height=300)


my_image = Image.open("output.png",)
my_image_tk = ImageTk.PhotoImage(my_image)
image_label = Label(window, image=my_image_tk)
image_label.pack()
image_label.config(bg="gray")





enter_title = Label(window, text="Enter Your Title", fg="black", bg="gray")
enter_title_entry = Entry(width=25)
enter_title.pack()
enter_title_entry.pack()

user_mesage_label = Label(text="Enter Your Message", fg="black", bg="gray")
user_mesage_label.pack()
user_mesage_title = Text(height=20, width=40)
user_mesage_title.pack()

user_enter_key = Label(text="Enter Your Key", fg="black", bg="gray")
user_enter_key.pack()
user_enter_key_entry = Entry(width=25)
user_enter_key_entry.pack()

myKey = Fernet.generate_key()
my_cryp_fernet = Fernet(myKey)


def new_create_file():

    user_iput1 = enter_title_entry.get().strip()
    user_input2 = user_mesage_title.get("1.0",END).strip()
    user_input3 = user_enter_key_entry.get().strip()

    encrypted_message = my_cryp_fernet.encrypt(user_input2.encode())


    if not user_iput1 or not user_input2:
        messagebox.showerror("Error", "Please Enter Title and Message")
        return
    if not user_input3:
        messagebox.showerror("Error", "Please Enter Key")
        return

    try:
        with open("secret.txt","ab") as s_file:
            s_file.write(user_iput1.encode() + b"\n")
            s_file.write(encrypted_message + b"\n")

        user_mesage_title.delete("1.0",END)
        enter_title_entry.delete(first=0,last=END)
        user_enter_key_entry.delete(first=0,last=END)

        messagebox.showinfo("Success", "Secret Message Saved")

    except:
        messagebox.showerror("Error", "Please Enter Title and Message")








save_encrypt_button = Button(text="Save & Encrypted ", fg="black", bg="light gray",command=new_create_file)
save_encrypt_button.config(padx=20)
save_encrypt_button.pack(pady=10)



decrypt_button = Button(text="Decrypt", fg="black", bg="light gray",)
decrypt_button.pack()



window.mainloop()