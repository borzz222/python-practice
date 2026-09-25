number = int(input())
if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")
if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")
if number in range(10, 51):
    print("Число лежит в диапазоне [10, 50]")
else:
    print("Число не лежит в диапазоне [10, 50]")