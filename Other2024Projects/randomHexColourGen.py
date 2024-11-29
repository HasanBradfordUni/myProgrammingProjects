import random
import pyperclip
import time

denToHexDict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
                8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

nums = int(input("How many colours do you want to generate? "))
for num in range(nums):
    digits = ""
    for digit in range(6):
        digit = random.randint(0, 15)
        digits += denToHexDict[digit]
    print("The random colour is:",digits)
    pyperclip.copy(digits)
    time.sleep(3)
