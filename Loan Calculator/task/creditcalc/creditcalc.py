print('Enter the loan principal:')
loan_principal = int(input())
print('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')
user_choice = input()
if user_choice == 'm':
    print('Enter the monthly payment:')
    monthly_payment = int(input())
    months = loan_principal / monthly_payment
    if months % 1 == 0:
        months = int(months)
    else:
        months = int(months) + 1
    print('It will take ' + str(months) + (' month' if months == 1 else ' months') + ' to repay the loan')
elif user_choice == 'p':
    print('Enter the number of months:')
    months = int(input())
    payment = loan_principal / months
    if payment % 1 == 0:
        print('Your monthly payment = ' + str(int(payment)))
    else:
        payment = int(payment) + 1
        last_payment = loan_principal - (months - 1) * payment
        print('Your monthly payment = ' + str(payment) + ' and the last payment = ' + str(last_payment) + '.')

