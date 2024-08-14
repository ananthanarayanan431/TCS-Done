
name="JavazZ"

for i in range(len(name)):
    if name[i]=='z':
        print('a',end="")
    elif name[i]=='Z':
        print('A',end="")
    else:
        ch=ord(name[i])+1
        print(chr(ch),end="")