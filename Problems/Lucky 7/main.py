n = int(input())

squares = []
for _ in range(n):
    number = int(input())
    if number % 7 == 0:
        squares.append(number * number)

for numbers in squares:
    print(numbers)
