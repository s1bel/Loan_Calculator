num = int(input())
prime = True
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            prime = False
else:
    prime = False

print('This number is prime' if prime else 'This number is not prime')
