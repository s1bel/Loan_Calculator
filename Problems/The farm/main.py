money = int(input())
price = ['chicken', 23, 'goat', 678, 'pig', 1296, 'cow', 3848, 'sheep', 6769]
price_index = -1
animals = 0
animal_type = ''

if money < price[1]:
    print('None')
else:
    while abs(price_index) < len(price):
        if money >= price[price_index]:
            animals = money // price[price_index]
            animal_type = price[price_index - 1]
            print(animals, animal_type + 's' if animals > 1 and animal_type != 'sheep' else animal_type)
            price_index = len(price)
        else:
            price_index -= 2  # check every odd element in list
