#surviving person : 4 
#the number on whuch the key (k) value goes, that value is removed. Joesphs algorithm. 

n=7
k=3

person=0
for i in range(1,n+1):
    person -( person +k)%i

print(f" Last survining person : {person +1 }")