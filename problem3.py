s = 'abcdefghijklmnopqrstuvwxyz'
count = 1
maxcount = 1
maxind = 0
ind = 0
for i in range(len(s) - 1):
    if ord(s[i]) <= ord(s[i + 1]):
        if count == 1:
            ind = i
        count += 1
        if count > maxcount:
            maxcount = count
            maxind = ind
    else:
        count = 1
print(s[maxind:maxind + maxcount])