#Pizza Order

print("Pizza delivery!")
size = input("What pizza size do you want? (S/M/L)")
add_pepperoni = input("Do you want extra pepperoni? (Y or N)")
add_cheese = input("Do you want extra cheese? (Y or N)")

total = 0

#Size value
if size == "S":
    total +=15
elif size == "M":
    total +=20
else:
    total +=25

#Extra pepperoni
if add_pepperoni == "Y" and size == "S":
    total +=2
elif (add_pepperoni == "Y" and size == "M") or (add_pepperoni == "Y" and size == "L"):
    total +=3
else:
    total +=0

#Extra cheese
if add_cheese == "Y":
    total +=1
else:
    total +=0

print("The total is :",total)