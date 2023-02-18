def sum(a, b):
    ans = a + b 
    print(f"\n {str(a)} + {str(b)} = {str(ans)} \n")

def rest(a, b):
    ans = a - b
    print(f"\n {str(a)} - {str(b)} = {str(ans)} \n")

def mult(a, b):
    ans = a * b
    print(f"\n {str(a)} × {str(b)} = {str(ans)} \n")

def div(a, b):
    ans = a / b
    print(f"\n {str(a)} ÷ {str(b)} = {str(ans)} \n")

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Please select number: ")

    if choice == "1":
        print("Addition")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        sum(a, b)
    elif choice == "2":
        print("Subtraction")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        rest(a, b)
    elif choice == "3":
        print("Multiplication")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        mult(a, b)
    elif choice == "4":
        print("Divition")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        div(a, b)
    else:
        print("Closing program...")
        quit()