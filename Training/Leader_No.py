# Leader No Problem 
#{4,9,3,2,7,1}
# if a number is greater than the noss behind it
#1- because it doesn't have any behind nos
#7-because it is greater than 1
#9-because it is greater than 3,2,7,1
#OUTPUT: 1,7,9


array=[4,9,3,2,7,1]
leader_no=array[-1]
print(leader_no)
for i in range(len(array)-2, -1, -1):
    if array[i] > leader_no:
        leader_no = array[i]
        print(leader_no)