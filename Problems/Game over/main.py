scores = input().split()
score = 0
incorrect = 0
i = 0

while incorrect < 3 and i < len(scores):
    if scores[i] == 'I':
        incorrect += 1
    elif scores[i] == 'C':
        score += 1
    i += 1

print('Game over' if incorrect == 3 else 'You won')
print(score)
