#Tip calculator

print("Welcome to the tip calculator.")


bill_amount_string = input("What is the total bill? : $")
bill_amount_string_converted = bill_amount_string.replace(",",".")
bill_amount = float(bill_amount_string_converted)

bill_people = input("How many people split the bill? ")

tip_percentage = input("What percentage tip would you like to give? (Regular 12%) ")
tip_percentage_converted = tip_percentage.replace(",",".")

payment = bill_amount*(1+(float(tip_percentage_converted)/100))/float(bill_people)
print("Each person should pay : $", round(payment,2))