word = input()
for n in word:
    if not n.isalpha():
        break
    else:
        if n in 'aeiou':
            print('vowel')
        else:
            print('consonant')
