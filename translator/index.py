from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

# color palette
black = "#0D2137"
white = "#E0EAF5"
blue = "#2E77AE"
orange = "#FF8E2B"

def main():
    # create program
    root = Tk()
    root.title("Translator")
    root.geometry("1080x500")
    root.configure(background=black)
    img = PhotoImage(file="translator\icon.png")
    root.iconphoto(False, img)

    # languages
    language = googletrans.LANGUAGES
    language_vals = [l.capitalize() for l in list(language.values())]
    lang1 = language.keys()

    select1 = ttk.Combobox(root, values=language_vals, font=("Calibri", 14), state="r")
    select1.place(x=100, y=20)
    select1.set("English")

    select2 = ttk.Combobox(root, values=language_vals, font=("Calibri", 14), state="r")
    select2.place(x=700, y=20)
    select2.set("Select Language")

    root.mainloop()


if __name__ == '__main__':
    main()