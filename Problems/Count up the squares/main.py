numbers = []
simple_sum = 0
square_sum = 0
while True:
    numbers.append(int(input()))
    simple_sum += numbers[-1]
    square_sum = square_sum + numbers[-1] ** 2
    if simple_sum == 0:
        break

print(square_sum if numbers[0] != 0 else 0)
