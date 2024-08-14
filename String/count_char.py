
name="takeuforward"

ans=dict()

for i in name:
    if i not in ans.keys():
        ans[i]=1
    else:
        ans[i]+=1

# print(max(ans.values()))
ch=""
maxy=0

for k,v in ans.items():
    if v>maxy:
        maxy=v
        ch=k
print(ch)