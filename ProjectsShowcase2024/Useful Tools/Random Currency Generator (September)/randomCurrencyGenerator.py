import random
import pyperclip
import time

minNum = int(input("Enter starting number: "))
maxNum = int(input("Enter ending number: "))
nums = int(input("How many numbers do you want to generate? "))
for num in range(nums):
    integerPart = random.randint(minNum, maxNum)
    decimalPart = random.random()
    finalNumber = integerPart + round(decimalPart,2)
    print("The random number is:",finalNumber)
    pyperclip.copy(finalNumber)
    time.sleep(2)
