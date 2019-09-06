s = input("The sentence: ")
c = input("The char: ")
for i in range(len(s)-1, -1, -1):
    if s[i] == c:
        s = s[:i] + s[i+1:]
print(s)
