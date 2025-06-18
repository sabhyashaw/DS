# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:44:08 2025

@author: Admin
"""
#Q1
l1=[1,2,3,4,5,2,4,9]
print('list 1 is' , l1)
#Q2
a=(int(input("\nEnter number of elements : ")))
l2=[]
for i in range(0,a):
    x=int(input("enter elements : "))
    l2.append(x)
print('list 2 is' , l2)
#Q3
l2[2]=34
print(l2)
#Q4
y=int(input('\nEnter the index : '))
z=int(input('\nEnter the element : '))
l1.insert(y,z)
print('list 1 after inserting is' , l1)
#Q5
l1.remove(6)
print('list 1 after removing element is ',  l1)
#Q6
l1.sort()
print('sorted list is ', l1)
#Q7
print('reverse of list 1 is ', l1[-1::])
#Q8
l3=[10,20,30,40,50]
l4=l1+l3
print('concatenated list is ', l4)
#Q9
print('last 3 elements are ', l1[-4:-1])
#Q10
s1=set(l1)
print('list before removing duplicates ',l1)
print('list after removing duplicates ',s1)
#Q11
l5=[1,2,3,4,5,2,14,23,12,4,5,67,12,8]
print('\nEvery 4th element of the list ', l5[3:14:4])
#Q12
arr = [5, 2, 9, 1, 7]
arr.sort()
print("Sorted array:", arr)

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

x1 = 7
result1 = binary_search(arr, x1)
if result1 != -1:
    print(f"{x1} found at index {result1}")
else:
    print(f"{x1} not found")

x2 = 8
result2 = binary_search(arr, x2)
if result2 != -1:
    print(f"{x2} found at index {result2}")
else:
    print(f"{x2} not found")

