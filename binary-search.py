# Creating a list of 10 random integers. 
import random
import qs

min = 9
max = 99
count = 10

l = [random.randint(min, max) for iter in range(count)]

# Sort the list (May be call quickSort here)
qs.quickSort(l, 0, 10)
print(l)

# Code for binary search here
def binSearch(se, lb, ub):
    while lb <= ub:
        mid = int((lb + ub)/2)
        if se < l[mid]:
            ub = mid-1
        elif se > l[mid]:
            lb = mid+1
        else:
            print('Found at ' + str(mid+1))
            break
    print('Not found')

# by recursion
def rbinSearch(se, lb, ub):
    mid = int((lb + ub)/2)
    if lb >= ub:
        print('Not found')
    elif se < l[mid]:
        rbinSearch(se, lb, mid-1)
    elif se > l[mid]:
        rbinSearch(se, mid+1, ub)
    elif se == l[mid]:
        print('Found at ' + str(mid+1))

t = rbinSearch(int(input('Enter the number - ')), 0, 10)
