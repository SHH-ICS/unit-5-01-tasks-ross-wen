# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import math

a = int(input("Input side a:\n"))
b = int(input("Input side b:\n"))
c = math.sqrt(a**2 + b**2)
print("The hypotenuse is:", c)
