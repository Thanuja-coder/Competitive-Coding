# Palindromic Number

n=int(input("Enter a number: "))
reverse=0
original=n

while n>0:
    rem= n % 10
    reverse=(reverse*10)+rem
    n=n//10

if reverse == original:
    print("It is a Palidrome No.")

else:
    print("It is not a Palindrome No.")
