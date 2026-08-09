item_price = []
budget = 0
bought_items = []
total_spent = 0

# This code use to input price of 6 items.
print("Enter price of 6 items:")
for number in range(0,6):
    item_price.append(int(input(f"Item {number + 1}: ")))

# This code use to enter budget.
budget = int(input("\nEnter total budget: "))

# This code use to check what items user can buy.
for number in range(0,6):
    if item_price[number] > budget:
        print(f"\nItem {number + 1} = {item_price[number]} -> cannot buy")
        print(f"Current total = {total_spent}")
    else:
        print(f"\nItem {number + 1} = {item_price[number]} -> buy")
        bought_items.append(item_price[number])
        total_spent += item_price[number]
        budget -= item_price[number]
        print(f"Current total = {total_spent}")

# This code use to print bought items .Total spent and Remaining budget.
print(f"\nBought items: {bought_items}")
print(f"Total spent: {total_spent}")
print(f"Remaining budget: {budget}")