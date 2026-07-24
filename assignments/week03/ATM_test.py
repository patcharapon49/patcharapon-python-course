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
        
        choice = input("Choose option 1-4: ")
        
        
        if choice == "1" :
            print("Your Balance is ",balance)
        elif choice == "2":
            withdraw = int(input("How many you want to withdraw: "))
            balance -= withdraw
            print("Your Balance is ",balance)
        elif choice == "3" :
            deposit = int (input("How many you want to deposit: "))
            balance += deposit
            print("Your Balance is ",balance)
        elif choice == "4" :
            break
else:
    print("Invalid PIN")