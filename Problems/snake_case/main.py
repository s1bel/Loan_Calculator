word = input()
new_word = ''
for char in word:
    if char.islower():
        new_word += char
    else:
        new_word += '_' + char.lower()
print(new_word)
