# Creating a list of 10 random integers. 
import random

min = 9
max = 99
count = 10

RandomListOfIntegers = [random.randint(min, max) for iter in range(count)]

print(RandomListOfIntegers)

# Code for Bubble Sort here 

for i in range(9):
    for j in range(9-i):
        if RandomListOfIntegers[j] > RandomListOfIntegers[j+1]:
            RandomListOfIntegers[j], RandomListOfIntegers[j+1] = RandomListOfIntegers[j+1], RandomListOfIntegers[j]
print(RandomListOfIntegers)