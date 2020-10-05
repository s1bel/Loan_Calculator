min_sleep = int(input())
max_sleep = int(input())
sleep = int(input())

if sleep < min_sleep:
    print('Deficiency')
elif sleep > max_sleep:
    print('Excess')
else:
    print('Normal')
