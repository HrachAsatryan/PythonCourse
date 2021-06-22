s = "azcbobobegghakl"
numvow = 0
for letter in s:
    if letter == 'a' or letter == 'o' or letter == 'i' or letter == 'u' or letter == 'e':
        numvow += 1
print("Number of vowels: " + str(numvow))