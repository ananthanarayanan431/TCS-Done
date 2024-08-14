
#Problem Statement: You are given an array. The task is to reverse the array and print it.
arr = [5,4,3,2,1]

print("Before Reversing!")
for i in arr:
    print(i,end=" ")

print("After Reversing")
n=len(arr)

for i in range(n//2):
    temp=arr[i]
    arr[i]=arr[n-i-1]
    arr[n-i-1]=temp

for i in range(n):
    print(arr[i],end=" ")