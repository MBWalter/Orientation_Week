import math

hour = input("Hours first: ")
minute = input("Minutes first: ")
second = input("Seconds first: ")
hour2 = input("Hours second: ")
minute2 = input("Minutes second: ")
second2 = input("Seconds second: ")
hours = abs((int(hour) - int(hour2))) * 60 ** 2
minutes = abs((int(minute)-int(minute2))) * 60
seconds = abs(int(second) - int(second2))
print("The difference:" , hours + minutes + seconds , "seconds. ")
