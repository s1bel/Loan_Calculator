column = int(input())
row = int(input())
moves = 0

if column in (1, 8):
    if row in (1, 8):
        moves += 3
    else:
        moves += 5
elif 1 < column < 8:
    if row in (1, 8):
        moves += 5
    else:
        moves += 8

print(moves)
