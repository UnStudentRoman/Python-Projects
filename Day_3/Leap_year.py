#Leap year

print("Is it by any chance a leap year?")

year = int(input("What year would you like to test? :"))


if year % 400 == 0:
    print(year, "is a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")