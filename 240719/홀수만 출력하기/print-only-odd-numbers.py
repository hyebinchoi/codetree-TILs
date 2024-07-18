N = int(input())


for _ in range(N):
    number = int(input())
    if number % 2 != 0 and number % 3 == 0:
        print(number)