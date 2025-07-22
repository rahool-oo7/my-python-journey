import numpy as np

'''
Array Indexing
1D => arr[index]
2D => arr[row,col]
'''

arr1 = np.array([10,20,30,40,50])

#indexing 
print(arr1[0])
print(arr1[-1])
# print(arr1[10]) #index out of range 


arr = np.array([[10,20],[30,40],[50,60]])

print(arr[1])

# fancy indexing => access multiple non - sequence elements 
# but it creates a copy not the original is effected => deep copy
print (arr1[[0,2,4]]) # fancy indexing => pass list of index to access


#BOOLEAN MASKING => filtering value of array based on condition
print(arr1[arr1 > 25])

# REshaping and manipulating