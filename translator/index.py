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

    # selectors
    select1 = ttk.Combobox(root, values=language_vals, font=("Calibri", 14), state="r")
    select1.place(x=150, y=20)
    select1.set("English")

    select2 = ttk.Combobox(root, values=language_vals, font=("Calibri", 14), state="r")
    select2.place(x=700, y=20)
    select2.set("Select Language")

    # textareas

    # frame
    frame1 = Frame(root, bg=blue, bd=5)
    frame1.place(x=600, y=90, width=450, height=210)
    
    frame2 = Frame(root, bg=blue, bd=5)
    frame2.place(x=30, y=90, width=450, height=210)

    # text input
    text1 = Text(frame1, font=("Calibri", 16), bg=blue, relief=GROOVE, wrap=WORD, borderwidth=0)
    text1.place(x=2, y=2, width=450, height=220)
    
    text2 = Text(frame2, font=("Calibri", 16), bg=blue, relief=GROOVE, wrap=WORD, borderwidth=0)
    text2.place(x=2, y=2, width=450, height=220)

    # scroll bar
    scrollbar1 = Scrollbar(frame1)
    scrollbar1.pack(side="right", fill="y")
    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)

    scrollbar2 = Scrollbar(frame2)
    scrollbar2.pack(side="right", fill="y")
    scrollbar2.configure(command=text2.yview)
    text2.configure(yscrollcommand=scrollbar2.set)


    root.mainloop()


if __name__ == '__main__':
    main()