string = "aaabbcc"

hashtable = [0 for i in range(256)]

# Log frequency of characters inside a hash table
for x in range(len(string)):
    hashtable[ord(string[x])] += 1

compressed = ''

for y in range(len(string)):
    freq = hashtable[ord(string[y])]

    if freq != 0:
        compressed += string[y] + str(freq)
        hashtable[ord(string[y])] = 0

print("Original string:", string)
print("Compressed string:", compressed)