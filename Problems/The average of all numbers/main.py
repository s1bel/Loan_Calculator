a = int(input())
b = int(input()) + 1
mean = 0
divider = 0
for i in range(a, b):
    if i % 3 == 0:
        mean += i
        divider += 1
print(mean / divider)