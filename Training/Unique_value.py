#Print unique value in the array
#{2,3,4,3,2}
#Time complexity: O(n)
# Space Complexity : O(1)

# Same No XOR =0
# No XOR 0= Same Number

#Works on only even number of duplicates

arr=[2,3,4,3,2]
arrlen=len(arr)
unique =0 

for i in range(arrlen):
    unique^=arr[i]

print(f"Unique value : {unique}")
