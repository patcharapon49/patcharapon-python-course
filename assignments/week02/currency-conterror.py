"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
print("What you want to convert 1.THB to USD or 2.USD to THB")
choose = str(input("Choose 1-2: "))
if choose == "1":
        bath = float(input("How many You want to convert?: "))
        bath *= 0.033
        print(f"This this your money after convert: {bath} USD")
elif choose == "2":
        bath = float(input("How many You want to convert?: "))
        bath *= 33.7
        print(f"This this your money after convert: {bath} THB")
else :
    print("Invaid input")




