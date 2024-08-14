
#Problem Statement: Given a string s, reverse the words of the string.

name = "I am in the Mumbai "

temp = ""
ans = ""

for i in range(len(name)):
    if name[i]=='' or name[i]==" ":
        ans = temp + " " + ans
        # print(ans)
        temp=""
    else:
        # print(temp)
        temp+=name[i]

print(ans)