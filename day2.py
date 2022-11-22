#Tip calculator

print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")

total_bill_as_int = int(total_bill)
tip_percent_as_int = int(tip_percent)
number_of_people_as_int = int(number_of_people)

tip = total_bill_as_int * tip_percent_as_int / 100
bill_person = round((tip + total_bill_as_int) / number_of_people_as_int, 2)

print(f"Each person should pay: ${bill_person}")



