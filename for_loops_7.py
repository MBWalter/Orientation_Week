number = int(input("How many Fibonacci-number you want to see: "))
a = 1
b = 1
print(a)
print(b)
for i in range(2,number + 1):
    c = a + b
    a = b
    b = c
    print(c)
