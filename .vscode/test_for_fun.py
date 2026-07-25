balance = int(input("How much of your salary: "))
tax = 0
total_tax = 0

if balance =< 150000 :
    balance -= 150000
else: print("You don't have any tax")

if balance =< 300000  :
    tax -= balance 
    balance -= tax
    