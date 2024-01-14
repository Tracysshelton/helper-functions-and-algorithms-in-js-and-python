# Convert Kilometers to miles
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")

#Convert Celsius to Fahrenhelt
celsius = float(input("Enter temperature in Celsius: "))
# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

# Solve quadratic equation
import math
# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
# Calculate the discriminant
discriminant = b**2 - 4*a*c
# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
 # Two real and distinct roots
 root1 = (-b + math.sqrt(discriminant)) / (2*a)
 root2 = (-b - math.sqrt(discriminant)) / (2*a)
 print(f"Root 1: {root1}")
 print(f"Root 2: {root2}")
elif discriminant == 0:
 # One real root (repeated)
 root = -b / (2*a)
 print(f"Root: {root}")
else:
 # Complex roots
 real_part = -b / (2*a)
 imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
 print(f"Root 1: {real_part} + {imaginary_part}i")
 print(f"Root 2: {real_part} - {imaginary_part}i")

# Check if leap year
year = int(input("Enter a year: "))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
 print("{0} is a leap year".format(year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
 print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
 print("{0} is not a leap year".format(year))

# check prime number
num = int(input("Enter a number: "))
# define a flag variable
flag = False
if num == 1:
 print(f"{num}, is not a prime number")
elif num > 1:
 # check for factors
 for i in range(2, num):
 if (num % i) == 0:
 flag = True # if factor is found, set flag to True
 # break out of loop
 break
 # check if flag is True
if flag:
 print(f"{num}, is not a prime number")
else:
 print(f"{num}, is a prime number")

# Primt the Fibonacci sequence
nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
 print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
 print("Fibonacci sequence upto",nterms,":")
 print(n1)
# generate fibonacci sequence
else:
 print("Fibonacci sequence:")
 while count < nterms:
 print(n1)
 nth = n1 + n2
 # update values
 n1 = n2
 n2 = nth
 count += 1

# Check for Armstrong Number
num = int(input("Enter a number: "))
# Calculate the number of digits in num
num_str = str(num)
num_digits = len(num_str)
# Initialize variables
sum_of_powers = 0
temp_num = num
# Calculate the sum of digits raised to the power of num_digits
while temp_num > 0:
 digit = temp_num % 10
 sum_of_powers += digit ** num_digits
 temp_num //= 10
# Check if it's an Armstrong number
if sum_of_powers == num:
 print(f"{num} is an Armstrong number.")
else:
 print(f"{num} is not an Armstrong number.")
