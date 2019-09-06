year = int(input("In which year you loking for easter : "))
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
dateofeaster = 22 + d + e
if (e == 6 ) and (d == 28 ):
    dateofeaster = 50
    if (e == 6) and (d == 29) and (a > 10):
        dateofeaster = 49
    else:
        dateofeaster = 22 + d + e
if dateofeaster > 31:
    print("April " , (dateofeaster - 31))
else:
    print("March" , dateofeaster)
