f = open('24-239.txt')
s = f.readline()
s = 'ZZXZXZZXYYZYZZYYY'
count, a = 0, 1
for i in range(1, len(s)):
    print(i, s[i-1], s[i], a, count)
    if (s[i] == 'Y' and s[i-1] == 'X') or (s[i] == 'Z' and s[i-1] == 'Y') or \
       (s[i] == 'Z' and s[i-1] == 'Z' and s[i-2] == 'Y' and i > 1):
        a += 1
        print(a)
        
    else:
        count = max(a, count)
        a = 1
#print(a)
