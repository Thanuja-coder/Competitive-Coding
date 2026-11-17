#Encryption and decryption 
#Encryptrd text -SBIVM
#Key used for encryption is 1
#Decrypted text - RAHUL
# SEISER CIPHER Implementation

str=input("Enter the string to be decrypted: ")
key=int(input("Enter the key used for encryption: "))
decrypted_str=''

for i in str:
    decrypted_str += chr((ord(i) - ord('A') - key) % 26 + ord('A'))

print("Decrypted text:", decrypted_str)
