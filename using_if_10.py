a = int(input("Enter 'a' : "))
b = int(input("Enter 'b' : "))
c = int(input("Enter 'c' : "))
if (c * c == a * a + b * b) or (a * a == b * b + c * c ) or (b * b == a * a + c * c):
    print("the 3 number can make a triangle :)")
else:
    print("the 3 number can't make a triangle :(")
