import math

weight_apple = input("How much apple do you want to buy? ")
cost_apple = input("How much does 1 kg apple cost? ")
price = int(weight_apple) * int(cost_apple)
print( "It will cost you" , abs(price) , "korona.")
