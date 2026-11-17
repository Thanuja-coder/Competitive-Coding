# [8,3,1,9,4,2]
# Size of the sub array:3
# Static Sliding Window Technique

#Window frame =main array
#window panel =sub array


#step 1 :
#[8,3,1] =12 (initial window state)

#step 2:
# 3,1,9 : In: 9 out : 8 |12+9-8 =13
#1,9,4 : In:4 Out: 3 | 13+4-3=14
#9,4,2 : In:2 Out:1 | 14+2-1=15

#step 3:
# Max Window Sum = 15

arr=[8,3,1,9,4,2]
k=3
window_sum=0
for i in range(k):
    window_sum += arr[i]
max_sum=window_sum

for j in range (k, len(arr)):
    window_sum += arr[j] - arr[j-k]
    if window_sum > max_sum:
        max_sum=window_sum

print("Max Window Sum:", max_sum)
