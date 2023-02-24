from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv
import base64
import os

load_dotenv()


PASSWORD = os.getenv("PASSWORD")

def decrypt():
    password = code.get()

    if password == PASSWORD:
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#100e34")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypted = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPTED", font="Arial", fg="#fff", bg="#100e34").place(x=10, y=10)
        text2 = Text(screen2, font="Robote 10", bg="#fff", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted)
    
    elif password == "":
        messagebox.showerror("Decryption", "Please provide a KEY")

    elif password != PASSWORD:
        messagebox.showerror("Decryption", "Wrong KEY, please try again")

def encrypt():
    password = code.get()

    if password == PASSWORD:
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#100e34")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED", font="Arial", fg="#fff", bg="#100e34").place(x=10, y=10)
        text2 = Text(screen1, font="Robote 10", bg="#fff", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted)
    
    elif password == "":
        messagebox.showerror("Encryption", "Please provide a KEY")

    elif password != PASSWORD:
        messagebox.showerror("Encryption", "Wrong KEY, please try again")

def main():
    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("530x400") # program size
    
    # program icon and name
    icon = PhotoImage(file="encryption-decryption\icon.png")
    screen.iconphoto(False, icon)
    screen.title("SafeCrypting")

    # reset function (clear all inputs)
    def reset():
        code.set("")
        text1.delete(1.0, END)
    
    # app content
    Label(text="Please provide text for encryption or decryption", fg="#100e34", font=("calibri", 18)).place(x=10, y=10)

    text1 = Text(font="Robote 14", bg="#fff", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=510, height=100)

    Label(text="Please enter KEY for encryption and decryption", fg="#100e34", font=("calibri", 12)).place(x=110, y=170)

    code = StringVar()
    Entry(textvariable=code, width=17, bd=0, font=("Arial", 25), show="*").place(x=110, y=200)

    Button(text="ENCRYPT", height="2", width=20, bg="#4f48ec", fg="#fff", bd=0, command=encrypt).place(x=80, y=250)
    Button(text="DECRYPT", height="2", width=20, bg="#ffbf18", fg="#fff", bd=0, command=decrypt).place(x=303, y=250)
    Button(text="RESET", height="2", width=52, bg="#100e34", fg="#fff", bd=0, command=reset).place(x=80, y=300)

    screen.mainloop()

if __name__ == "__main__":
    main()