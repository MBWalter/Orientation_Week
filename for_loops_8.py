number = int(input("How many Fibonacci number you want to sum: "))
a = 1
b = 1
total = 2
for i in range(3,number + 1):
    c = a + b
    a = b
    b = c
    total = total + c
print(total)    
