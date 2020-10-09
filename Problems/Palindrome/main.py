word = input()

for i, n in enumerate(word):
    if n == word[- 1 - i]:
        continue
    else:
        print('Not palindrome')
        break
else:
    print('Palindrome')
