total_tax = 0
balance_tax = 0
tax1 = 0
tax2 = 0
tax3 = 0
tax4 = 0
tax5 = 0
tax6 = 0
tax7 = 0
tax8 = 0

def calculate_tax(balance,total_tax):
    if balance > 0 :
        tax1 = (min(balance , 150000)- 0) * 0
        total_tax += tax1

    if balance > 150000  :
        tax2 = (min(balance , 300000)- 150000) * 0.05 
        total_tax += tax2

    if balance > 300000 :
        tax3 = (min(balance , 500000)- 300000) * 0.10
        total_tax += tax3

    if balance > 500000  :
        tax4 = (min(balance , 750000)- 500000) * 0.15
        total_tax += tax4
  
    if balance > 750000 :
        tax5 = (min(balance , 1000000)- 750000)* 0.20
        total_tax += tax5

    if balance > 1000000  :
        tax6 = (min(balance , 2000000)- 1000000) * 0.25 
        total_tax += tax6

    if balance > 2000000 :
        tax7 = (min(balance , 5000000)- 2000000) * 0.30
        total_tax += tax7

    if balance > 5000000 :
        tax8 = (balance - 5000000) * 0.35
        total_tax += tax8

    return total_tax

balance = int(input("How much of your salary: "))

total_tax = calculate_tax(balance,total_tax)

print("You Income: ",balance)
print("ภาษีขั้นที่ 1: ",tax1)
print("ภาษีขั้นที่ 2: ",tax2)
print("ภาษีขั้นที่ 3: ",tax3)
print("ภาษีขั้นที่ 4: ",tax4)
print("ภาษีขั้นที่ 5: ",tax5)
print("ภาษีขั้นที่ 6: ",tax6)
print("ภาษีขั้นที่ 7: ",tax7)
print("ภาษีขั้นที่ 8: ",tax8)
print("Total Tax: ",total_tax)
effective_tax_rate = total_tax / balance * 100
print(f"Your Effective: {effective_tax_rate:.2f}%")
after_tax = balance - total_tax
print(f"Your Income After pay a Tax: {after_tax}")
