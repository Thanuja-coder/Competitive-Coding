#Count the no.of carry values generated for 2 nos' addition
# 2 integer values
# No type conversion allowed

# MODULAR ARITHMETIC PATTERN( If we need to acces any digit without converting it into string)

n1=int(input("Enter the Number 1:"))
n2=int(input("Enter the Number 2:"))
carry=0
carry_count=0

while n1>0 or n2>0:
    last1=n1 %10
    last2=n2%10
    sum=last1+last2+carry
    if sum > 9:
        carry_count+=1
        carry=1
    else:
        carry=0
    
    n1=n1//10
    n2=n2//10

print("The carry count is :",carry_count)

        