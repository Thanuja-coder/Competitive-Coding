# Peak Value Problem 
# A number gretaer than the neighboring numbers
#{2,8,3,1,4,3,9,5}
#{8 4 9}


arr=[2,8,3,1,4,3,9,5]
arrlen=len(arr)

#Left corner value
if arr[0]>arr[1]:
    print(arr[0],end="")

#Right corner value
if arr[arrlen -1 ]> arr[arrlen -1]:
    print(arr[arrlen -1],end=" ")

#In between values
for i in range(1,arrlen-1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        print(arr[i],end=" ")

        