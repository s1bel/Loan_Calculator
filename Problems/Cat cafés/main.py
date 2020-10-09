cafe = []
names = []
while True:
    input_data = input()
    if input_data == 'MEOW':
        break
    else:
        cafe.append(input_data.split()[0])
        names.append(int(input_data.split()[1]))

print(cafe[names.index(max(names))])
