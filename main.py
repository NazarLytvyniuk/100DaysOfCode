import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#create lists with letters, symbols and numbers

ps_letters = []
ps_symbols = []
ps_numbers = []

for i in range(0, nr_letters):
  ps_letters.append(letters[random.randint(0, len(letters) - 1)])

for i in range(0, nr_symbols):
  ps_symbols.append(symbols[random.randint(0, len(symbols) - 1)])

for i in range(0, nr_numbers):
  ps_numbers.append(numbers[random.randint(0, len(numbers) -1 )])

#randomize order of characters

characters = []
characters.extend(ps_letters)
characters.extend(ps_symbols)
characters.extend(ps_numbers)

password = ""
for i in range(0, len(characters)):
  index = random.randint(0, len(characters) - 1)
  password += characters[index]
  characters.remove(characters[index])

print("Here is your password: " + password)