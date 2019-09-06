s = input("The sentence: ")
c = input("The char: ")
count = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == c:
        count = count + 1
print(count)
