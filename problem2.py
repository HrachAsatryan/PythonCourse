s = "azcbobobegghakl"
numbob = 0
for i in range(len(s) - 2):
    if s[i:i+3] == 'bob':
        numbob += 1
print("Number of times bob occurs: " + str(numbob))