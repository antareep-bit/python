# Creating a list of 10 random integers. 
import random

min = 9
max = 99
count = 10

a = [random.randint(min, max) for iter in range(count)]

print(a)

# Code for Quick Sort here 

def partition(low, high):
    pivot = a[low]
    i = low+1
    for j in range(low+1, high):
        if a[j] < pivot or a[j] == pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i-1], a[low] = a[low], a[i-1]
    return i-1

def quickSort(low, high):
    if low < high:
        pp = partition(low, high)
        quickSort(low, pp)
        quickSort(pp+1, high)

quickSort(0, 10)
print(a)
