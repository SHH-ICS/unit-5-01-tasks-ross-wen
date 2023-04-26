# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
print("Answer the addition question:")
random1 = random.randint(1,100)
random2 = random.randint(1,100)
print("What is ", random1, "+", random2, "?")
answer = int(input())
real = random1 + random2
if answer == real:
  print("You got it right!")
else:
  print("Wrong!~~~")
