
arr1 = [1,3,4,5,2]
arr2 = [2,4,3,1,7,5,15]

# method 1
# O(M*N)

#meehtod
#Bianry Search

def binary(arr,start,end,tar):
    while start<=end:
        mid = (start + end) // 2
        if arr[mid]==tar:
            return True
        elif arr[mid]<tar:
            start=mid+1
        else:
            end=mid-1
    return False

arr2.sort()

def answer():
    for i in arr1:
        if not binary(arr2,0,len(arr2),i):
            print("Not a subset of aa Array")
            break
    else:
        print("Subset of a Array")


#method 3
#Hashmap

def check():
    ans={}
    for i in arr2:
        ans[i]=1

    for i in arr1:
        if i not in ans.keys():
            print("Not a Subset")
            break
    else:
        print("Subset")

check()