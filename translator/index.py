from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

# color palette
black = "#0D2137"
white = "#E0EAF5"
blue = "#2E77AE"
orange = "#FF8E2B"

def translate():
    global languages
    try:
        # get text and language to translate
        text = text1.get(1.0, END)
        s1 = select1.get()
        s2 = select2.get()

        if text:
            words = textblob.TextBlob(text)

            # find both langs short name
            for i, j in languages.items():
                if j == s2.lower():
                    lan_ = i
                if j == s1.lower():
                    lan = i
            
            # translate it
            words = words.translate(from_lang=str(lan), to=str(lan_))
            text2.delete(1.0, END)
            text2.insert(END, words)
    
    except Exception as e:
        messagebox.showerror("Translation", "Please try again")
        print(e)

def main():
    global root

    global select1
    global select2

    global text1
    global text2

    global languages

    # create program
    root = Tk()
    root.title("Translator")
    root.geometry("1080x450")
    root.configure(background=black)
    img = PhotoImage(file="translator\icon.png")
    root.iconphoto(False, img)

    # languages
    languages = googletrans.LANGUAGES
    language_vals = [l.capitalize() for l in list(languages.values())]

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
    frame1.place(x=30, y=90, width=450, height=210)
    
    frame2 = Frame(root, bg=blue, bd=5)
    frame2.place(x=600, y=90, width=450, height=210)

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

    #translate button
    translate_btn = Button(root, text="Translate", font=("Calibri", 22), cursor="hand2", bd=0, bg=orange, fg=white, command=translate)
    translate_btn.place(x=475, y=340)

    
    root.mainloop()


if __name__ == '__main__':
    main()