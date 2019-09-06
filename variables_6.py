total = input("How much money you want to cover to coins: ")
money = int(total)
ten_coins = money // 10
five_coins = (money - (ten_coins * 10)) // 5
two_coins = (money -( ten_coins * 10 + five_coins * 5)) // 2
one_coins = (money -( ten_coins * 10 + five_coins * 5)) % 2
print("Least ammount of coins you can pay with: ")
print("10 korona coin: ")
print("")
print(ten_coins)
print("")
print("5 korona coin: ")
print("")
print(five_coins)
print("")
print("2 korona coin: ")
print("")
print(two_coins)
print("")
print("1 korona coin: ")
print("")
print(one_coins)
