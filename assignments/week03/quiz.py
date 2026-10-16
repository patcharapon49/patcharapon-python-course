# Complete this program to classify people by age
<<<<<<< HEAD
age = int(input("Enter age:"))
=======
age = int(input("Enter age: "))

>>>>>>> upstream/main
# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
<<<<<<< HEAD
if age <= 12:
    print("You are Child")
elif age <= 19:
    print("You are Teenager")
elif age <= 59:
    print("You are Adult")
else :
    print("You are Senior")
=======

>>>>>>> upstream/main


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
<<<<<<< HEAD
        if choice = 1:
            print("Your Balance is ",balance)
        
        elif choice = 2:
            withdraw = int(input("How many you want to withdraw: "))
        balance -= withdraw
        print("Your Balance is ",balance)
        
        elif choice = 3 
            deposit = int(input("How many you want to deposit: "))
        balance += deposit
        print("Your Balance is ",balance)

        elif choice = 4:
            break:
=======
        
>>>>>>> upstream/main
else:
    print("Invalid PIN")
