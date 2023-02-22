import string
import random

all_characters = list(string.ascii_letters + string.digits + "!#$%&/@()*-+^")

def generate_password():
    password_len = int(input("How long would you like your password to be? "))
    random.shuffle(all_characters)

    new_password = []

    for x in range(password_len):
        new_password.append(random.choice(all_characters))

    random.shuffle(new_password)

    new_password = "".join(new_password)

    print(f"\n Here is your new password: \n\n {new_password} \n\n Please copy it!")


new_pass = input("Would you like a new password? ")

if new_pass == "Yes" or new_pass == "yes" or new_pass == "y" or new_pass == "Y":
    generate_password()
else:
    print("Closing program...")
    quit()
