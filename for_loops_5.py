number = int(input("How many rows you want: "))
for i in range(1,number + 1):
    print(" " * (number-1) + "*" * i + "*" * (i-1))
    number = number - 1
