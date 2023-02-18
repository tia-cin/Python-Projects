def main():
    print("Welcome! \n")

    email = input("Please provide your email address: ")

    username, domain = email.split("@")
    domain, extention = domain.split(".")

    print(f"Username: {username} \n Domain: {domain} \n Extention: {extention}")

while True:
    main()