#Majority element/Voting Problem 
#{2,2,1,1,1,2,2}
#Majority Element is: 2
#Time Complexity: 0(n)

# arr=[2,2,1,1,1,2,2]
# count_1=0
# count_2=0

# for i in arr:
#     if i==2:
#         count_2 +=1
#     else:
#         count_1 +=1

# if count_2>count_1:
#     print("Majority element is : 2")
# else:
#     print("Majority element is : 1")


arr=[2,2,1,1,1,2,2]
party=0
count=0

#identify which party having highest frequency
for i in range(len(arr)):
    if count ==0:
        party = arr[i]
    if arr[i] == party:
        count+=1
    else:
        count-=1
print("The party with highest frequency: ",party)

# Check if single government can form a party
count=0

for j in range(len(arr)):
    if party == arr[j]:
        count+=1

if count>(len(arr)/2):
    print("Absolute Majority: ",party)
else:
    print("No majority found")