

arr1 = [2,5,1,3,0]
arr2 = [8,10,5,7,9]
#Problem Statement: Given an array, we have to find the smallest element in the array.

print("Method 1")
arr1.sort()
arr2.sort()
print(arr1[0])
print(arr2[0])

print("Method 2")
minn = arr1[0]
for i in range(1,len(arr1)):
    if minn>arr1[i]:
        minn=arr1[i]
print(minn)

minn=arr2[0]
for i in range(1,len(arr2)):
    if minn>arr2[i]:
        minn=arr2[i]
print(minn)