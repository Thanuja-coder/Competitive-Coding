#[2,00,2,1,1,0]
#time complexity :O(n)
#Assurance: Numbers:0 1 2

a = [2, 0, 2, 1, 1, 0]

low = 0
mid = 0
high = len(a) - 1

while mid <= high:

    if a[mid] == 0:
        temp = a[mid]
        a[mid] = a[low]
        a[low] = temp

        low += 1
        mid += 1

    elif a[mid] == 1:
        mid += 1

    elif a[mid] == 2:
        temp = a[mid]
        a[mid] = a[high]
        a[high] = temp

        high -= 1

print("Sorted array:", a)