# greet user
print("Welcome to tip calculator")
print("*" * 60)

# Ask user to enter the total bill amount
bill_amount = float(input("Please enter the total bill amount: "))

# Ask the user for the split
split = int(input("How many ways do you wish to split?: "))

# Ask the user for tip
tip_amount = float(input("Enter tip(%): "))

# Calculate total bill
total_bill_amount = bill_amount + (bill_amount * (tip_amount / 100))

# Calculate how much each individual should pay
each_individual_pays = total_bill_amount / split

# Print the output
print("*" * 60)
print(f"Your total bill is: ${total_bill_amount}")
print(f"you chose to pay {tip_amount}% tip")
print(f"You've chosen to split the bill amongst {split} members")
print(f"Each individual should pay ${round(each_individual_pays)}")