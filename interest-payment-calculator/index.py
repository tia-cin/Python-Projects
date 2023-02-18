def main():
    print("Welcome to Payment Loan Calculator! \n")

    principal = float(input("Loan amount: "))
    apr = float(input("Annual Interest Rate: "))
    years = int(input("Amount of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print(f"\n The monthly payment for this loan is: ${monthly_payment}")

main()