# merge 2 sorted arrya or lists without using function extend() or append()

arr1=[1,3,5,7]
arr2=[2,4,6,8]

result_len=len(arr1)+len(arr2)
result=[0 for i in range(result_len)]

i=0
j=0
k=0

while i<len(arr1) and j<len(arr2):
    if arr1[i] <= arr2[j]:
        result[k]=arr1[i]
        i+=1
        k+=1
    else:
        result[k]=arr2[j]
        j+=1
        k+=1


#Handling missing values
    while i < len(arr1):
        result[k]= arr1[i]
        i+=1
        k+=1

    while j< len(arr2):
        result[k]=arr2[j]
        j+=1
        k+=1


#Result Array
print(f"Result Array:{result}")

