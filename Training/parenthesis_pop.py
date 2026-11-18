#If top value is pairs of parenthesis
#Pop from the stack 

# stack=[] top = -1
#stack empty/top is back to -1
#then balanced parenthesis 

string=" [({})]"
stringLen= len(string)

stack=[0 for i in range(stringLen)]

top=-1
for ch in string:
    if ch=='{' or ch =="(" or ch == "[":
        top+=1

        stack[top]=ch

    if ch =="}" or ch ==")" or ch == "]":
        if stack[top]=="{" and ch =="}":
            top-=1
        if stack[top]=="(" and ch ==")":
            top-=1
        if stack[top]=="[" and ch =="]":
            top-=1

if top== -1:
    print("Balanced parenthesis")
else:
    print("Not Balanced parenthesis")

