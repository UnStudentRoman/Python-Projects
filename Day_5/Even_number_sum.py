#Sum of even numbers


even_sum = 0

n = int(input("Up to what number you want to calculate the sum of evens?\n"))

for i in range(2,n+1,2):
    even_sum += i
print("The sum of evens from 0 to", n,"is : ", even_sum)