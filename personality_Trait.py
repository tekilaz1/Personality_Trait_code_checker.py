import math
import random

print("WELCOME TO THE PERSONALITY CHECKER QUIZ ")
print("THIS IS YOUR  PERSONALITY CHECKER BASED ON YOUR CHOICES ")
print("THE ALGORITHM WORKS BY ANALYZING YOUR ANSWERS AND GIVE THEM MARKS ACCORDINGLY, SO THAT THEY WILL BE COMPARED")
print("NOTE! THE NUMBERS DO NOT REPRESENT THE ACTUAL VALUE, THEY ARE JUST SYMBOLS FOR CHOICES.")
print("\n")
print("SO LETS START THE QUIZ!")
print("\n")

print("1. I am an extrovert")
print("2. I am an introvert ")
print("3. I couldn't decide where I really belongs  ")
print("4. I don't even know what that means")
Q1 = int(input("A.what personality trait do you have?(please enter here your relevant choice by number from above)"))
print("\n")

print("1. I spent mostly with my friends and relatives")
print("2. I spent mostly alone or reading a book")
print("3. I do like being alone or with my dog eventhough its boring ")
print("4. I like being alone, but due to my social status I couldn't.")
Q2 = int(input("B.where do you spent your time after work?(please enter  your relevant choice by number from above)"))
print("\n")

print("1. I am very social person")
print("2. really I am not that social person")
print("3. I prefer being alone ")
print("4. even though I am a social person, but I love being alone")
Q3 = int(input("C. Do you consider yourself a social person?(please enter your relevant choice by number from above)"))
print("\n")

print("1. Practical intelligence ")
print("2. creative intelligence")
print("3. Analytical intelligence  ")
print("4. I don't even know these types of intelligence ")
Q4 = int(
    input("D.which intelligence doyou think you have most?(please enter your relevant choice by number from above)"))
print("\n")

print("1. Speaking ")
print("2. Reading")
print("3. Dancing ")
print("4. I donot have any talent")
Q5 = int(input("E.pick your relevant talent from the list?(please enter your relevant choice by number from above)"))
print("\n")

if Q1 == 4 or Q4 == 4:
    Q1 = 0
    Q4 = 0

if Q3 == 1 and Q5 == 1:
    Q3 = 10 + math.pow(2, 5)
    Q5 = 10 + math.pow(2, 5)

if Q2 == 2 or Q3 == 2:
    Q2 = -2 * math.pow(2, 3)
    Q3 = -2 * math.pow(2, 3)

numsum = Q1 + Q2 + Q3 + Q4 + Q5


def personality_1():
    if numsum < 0:
        print("RESULT=YOU HAVE AN INTROVERT PERSONALITY, LOVING LONLINESS")
    elif 0 <= numsum <= 20:
        print("RESULT =YOU ARE A MODERATE PERSON LEANING TO INTROVERT PERSONALITY WHILE LOVE ENJOY SOCIAL LIFE .")
    elif 20 < numsum <= 89:
        print("RESULT=YOU HAVE AN EXTROVERT PERSONALITY, ENJOYING SOCIAL LIFE ")
    else:
        print("RESULT= YOU ARE TRYING TO PLAY WITH THE QUIZ, PLEASE GIVE HONEST ANSWERS THAT DIDN'T CONTRADICT.")


print("YOUR SCORE RESULT IS ", numsum)
print("\n")

personality_1()
