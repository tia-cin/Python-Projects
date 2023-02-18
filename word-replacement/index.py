def replace_word():
    str = "Bla bla bla"
    replace = input("Word to replace: ")
    replacement = input(f"Replace '{replace}' with: ")

    print(str.replace(replace, replacement))

replace_word()
