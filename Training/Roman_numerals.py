# Int to Roman
# For a given positive integer value print the corresponding roman numeral for it.
#values={ 1000,900,500,400,100,90,50,40,10,9,5,4,1}
#symbols ={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"}

#45 --> XLV
#13 --> XIII
#3000 --> MMM

values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbols =["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
n=int(input("Enter the number: "))

final_roman_symbol=''

for i in range(len(values)):
    while n>= values[i]:
        final_roman_symbol+=symbols[i]
        n=n-values[i]

print(f"Int: {n} ---> Roman: {final_roman_symbol}")
