numbers = []
while True:
    number = input()
    if number == '.':
        break
    else:
        numbers.append(float(number))
numbers.sort()
print(numbers[0])
