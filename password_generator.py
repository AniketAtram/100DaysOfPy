#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_string = ""
numbers_string = ""
symbols_string = ""

for letter in range(nr_letters):
    letters_string += random.choice(letters)

for symbol in range(nr_symbols):
    symbols_string += random.choice(symbols)

for number in range(nr_numbers):
    numbers_string += random.choice(numbers)

password_string_easy = letters_string+symbols_string+numbers_string
print(f"Easy Level - {password_string_easy}")
letter_array = list(letters_string)
symbols_array = list(symbols_string)
numbers_array = list(numbers_string)
random.shuffle(letter_array)
random.shuffle(symbols_array)
random.shuffle(numbers_array)
password_string_hard = "".join(letter_array) + "".join(symbols_array) + "".join(numbers_array)
print(f"Hard Level - {password_string_hard}")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P