arr =[100,1,10,3,2,101,4,102]

for i in range(len(arr)):
    minIndex=i
    for j in range(i,len(arr)):
        if arr[j]<arr[minIndex]:
            minIndex=j


    #swap Logic
    temp=arr[minIndex]
    arr[minIndex]=arr[i]
    arr[i]=temp

print(arr)


# Part 2: Longest Consecutive Count
count=1
maxCount=0
for x in range(len(arr)-1):
    if(arr[x]+1)==arr[x+1]:
        count+=1
    else:
        if count > maxCount:
            maxCount=count
        count=1

print(f" Max Consecutive Count: {maxCount}")
