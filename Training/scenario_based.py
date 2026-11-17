# You are given an array of people. where each element represents the weight of a person.
#You are also given an integer limit
#and the combined weight of those 2 people must not exceed the given limit. 
#Your task is to find the minimum number of boats to rescue all the people.
# Each boat can carry at most 2 people at the same time, provided the sum of the weight of those people is at most limit.


#peope=[1,2,2,3]
#Limit =3
#max people in one boat =2
#Minimum boats required ? 

people=[1,2,2,3]
limit=3
boats=0
people.sort()
i=0
j=len(people)-1
while i <= j:
    if people[i] + people[j] <= limit:
        i += 1
        j-=1
    else:
        j -= 1
    boats += 1

print("Minimum Boats Required:", boats)
