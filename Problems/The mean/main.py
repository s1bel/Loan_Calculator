numbers = []
while True:
    number = input()
    if number != '.':
        numbers.append(int(number))
    else:
        break
print(sum(numbers) / len(numbers))
