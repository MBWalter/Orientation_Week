sorok = int(input("M number : ")) 
oszlopok = int(input("N number : ")) 
for i in range(oszlopok):
    for j in range(sorok):
        if(i == 0 or i == oszlopok - 1 or j == 0 or j == sorok - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
    print()
