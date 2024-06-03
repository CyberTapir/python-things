# -*- coding: utf-8 -*-
# File              : randomNumbers.py
# Author            : Callum Bennett
# Date              : 03.06.2024
# Last Modified Date: 03.06.2024
# Last Modified By  : Callum Bennett

array = []

def randomNumbers():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num3 = input("Enter the third number: ")
    num4 = input("Enter the fourth number: ")
    num5 = input("Enter the fifth number: ")
    num6 = input("Enter the sixth number: ")

    if num1.isnumeric == True:
        if num2.isnumeric == True:
            if num3.isnumeric == True:
                if num4.isnumeric == True:
                    if num5.isnumeric == True:
                        if num6.isnumeric == True:
                            print("All numbers are numeric")
                            array = generateRandomNumbers(makeArray(num1, num2, num3, num4, num5, num6))


def makeArray(num1, num2, num3, num4, num5, num6):
    inputNumbers = []
    inputNumbers.append(num1)
    inputNumbers.append(num2)
    inputNumbers.append(num3)
    inputNumbers.append(num4)
    inputNumbers.append(num5)
    inputNumbers.append(num6)
    return inputNumbers

def generateRandomNumbers(inputNums):
    import random
    randomNumbers = []
    currentNum = 0
    for i in range (0, 99):
        for i in range(0, 5):
            currentNum = currentNum & inputNums(random.randint(0, 5))
        randomNumbers.append(currentNum)
    return randomNumbers

def howManyColumns():
    columns = input("How many columns would you like to display the numbers in? ")
    return columns

def displayNumbers(randomNumbers, columns):
    for i in range(0, 99):
        if i % columns == 0:
            print("\n")
        print(randomNumbers(i) + " ")
    print("\n")

randomNumbers()
displayNumbers(array, howManyColumns())
