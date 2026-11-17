# Buy Sell Problem 
# To find the maximum profit 
# Using 2 pointers
#Pointer 1- Buy point- Keeps moving to the minimum value only 
#Pointer 2 - Sell point- Keeps moving to the next value.(i)
#{15,3,2,1,6,11,5}- here profit is 10- buy at 1 and sell at 11


arr=[15,3,2,1,6,11,5]

buy=arr[0]
max_profit=0 

for i in arr:   # i is the sell point
    if i<buy:
        buy=i
    profit=i-buy
    if profit>max_profit:
        max_profit=profit
print("Maximum Profit:", max_profit)