first_num = float(input())
second_num = float(input())
operation = input()

if operation in ('/', 'mod', 'div') and second_num == 0.0:
    print("Division by 0!")
else:
    if operation == 'mod':
        print(first_num % second_num)
    elif operation == 'pow':
        print(first_num ** second_num)
    elif operation == 'div':
        print(first_num // second_num)
    elif operation == '/':
        print(first_num / second_num)
    elif operation == '*':
        print(first_num * second_num)
    elif operation == '+':
        print(first_num + second_num)
    elif operation == '-':
        print(first_num - second_num)
