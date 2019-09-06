num = int(input("How many numbers you want: "))
min_num = num
numbers = []
for i in range (0,num):
    x = int(input("Enter next number: \n")) 
    numbers.insert(i , x)
    i = i + 1
print(numbers)
for i in range(len(numbers)):
    if int(numbers[i]) < min_num:
        min_num = numbers[i]
print("Smallest number: " , min_num)
