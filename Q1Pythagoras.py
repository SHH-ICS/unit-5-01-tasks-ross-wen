# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math

a = int(input("Input side a:\n"))
b = int(input("Input side b:\n"))
c = math.sqrt(a**2 + b**2)
print("The hypotenuse is:", c)
