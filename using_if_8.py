num = int(input("How many numbers you want: "))
min_num = num
max_num = num
numbers = []
for i in range (0,num ):
    x = int(input("Enter next number: \n")) 
    numbers.insert(i , x)
    i = i + 1
print(numbers)
for i in range(len(numbers)):
    if int(numbers[i]) < min_num:
        min_num = int(numbers[i])
        i += i
print("Smallest number: " , min_num)
for i in range(len(numbers)):
    if int(numbers[i]) > max_num:
        max_num = int(numbers[i])
        i += i
print("Biggest number: " , max_num)
