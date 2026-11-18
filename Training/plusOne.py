# Plus One program 
#[1,9,9] -> [2,0,0]
#[1,2,3] ->[1,2,4]
#[1,8,9] -> [1,9,0]
#[9,9,9] ->[1,0,0,0]

def plusOne(arr):
    arrlen =len(arr)
    for i in range(arrlen -1,-1,-1):
        if arr[i] <0:
            arr[i]+=1
            return arr
        arr[i]=0
    return[1] + arr

test_arr =[9,9,9]
resultArr=plusOne(test_arr)
print(f"[9,9,9] -> {resultArr}")

