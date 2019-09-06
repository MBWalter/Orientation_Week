num = int(input("How many numbers you want: "))
num_even = 0
num_odd = 0
num_count = 0
numbers = [num]
for i in range (1,num + 1):
    x = int(input("Enter next number: \n")) 
    numbers.insert(i , x)
    i = i + 1
print(numbers)
for i in range(len(numbers)):
    if int(numbers[i]) % 2 == 0:
        num_even = num_even + 1
    else: 
        num_odd =  num_odd + 1
        num_count = num_count + int(numbers[i])
print("Even: " , num_even)
print("Odd: " , num_odd)
print("Odd total: " , num_count)
