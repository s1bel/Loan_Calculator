# import argparse
import math
import sys


# parser = argparse.ArgumentParser()
# parser.add_argument('--type', choices=['annuity', 'diff'], help='The type of payment: "annuity" or "diff" (differentiated)')
# parser.add_argument('--payment', help='The monthly payment amount. Use only with --type=annuity.')
# parser.add_argument('--principal', help='is used for calculations of both types of payment')
# parser.add_argument('--periods', help='denotes the number of months needed to repay the loan')
# parser.add_argument('--interest', help='is specified without a percent sign')
# args = parser.parse_args()
# print(args)
# exit(1)

args = sys.argv
formatted_args = []

if len(args) > 4:
    for i in args:
        formatted_args += i.split('=')
else:
    print('Incorrect parameters')
    exit(0)

if '--payment' in formatted_args and float(formatted_args[formatted_args.index('--payment') + 1]) < 0:
    print('Incorrect parameters')
    exit(0)
elif '--principal' in formatted_args and float(formatted_args[formatted_args.index('--principal') + 1]) < 0:
    print('Incorrect parameters')
    exit(0)
elif '--periods' in formatted_args and float(formatted_args[formatted_args.index('--periods') + 1]) < 0:
    print('Incorrect parameters')
    exit(0)
elif '--interest' in formatted_args and float(formatted_args[formatted_args.index('--interest') + 1]) < 0:
    print('Incorrect parameters')
    exit(0)

if '--type' in formatted_args and ('diff' in formatted_args or 'annuity' in formatted_args) and '--interest' in formatted_args:
    if 'diff' in formatted_args and not '--payment' in formatted_args:
        pass
    elif 'annuity' in formatted_args:
        pass
    else:
        print('Incorrect parameters')
        exit(0)
else:
    print('Incorrect parameters')
    exit(0)

exit(0)

print('''What do you want to calculate?
type "n" - for number of monthly payments,
type "a" - for annuity monthly payment amount,
type "p" - for the monthly payment:''')
user_choice = input()
if user_choice == 'n':
    print('Enter the loan principal:')
    loan_principal = float(input())
    print('Enter the monthly payment:')
    monthly_payment = float(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    nominal_interest_rate = loan_interest / (12 * 100)
    months = math.log(monthly_payment
                       / (monthly_payment - nominal_interest_rate * loan_principal), (1 + nominal_interest_rate))
    if months % 1 == 0:
        months = int(months)
    else:
        months = int(months) + 1
    years = months // 12
    months = months % 12
    if years == 0:
        print('It will take ' + str(months) + (' month' if months == 1 else ' months') + ' to repay the loan')
    else:
        print('It will take ' + str(years) + (' year' if months == 1 else ' years') + ' and ' + str(months) + (
            ' month' if months == 1 else ' months') + ' to repay the loan')
elif user_choice == 'a':
    print('Enter the loan principal:')
    loan_principal = float(input())
    print('Enter the number of periods:')
    months = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    nominal_interest_rate = loan_interest / (12 * 100)
    monthly_payment = loan_principal * ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, months))
                                        / (math.pow(1 + nominal_interest_rate, months) - 1))
    if monthly_payment % 1 == 0:
        print('Your monthly payment = ' + str(int(monthly_payment)))
    else:
        monthly_payment = int(monthly_payment) + 1
        print('Your monthly payment = ' + str(int(monthly_payment)))
#        last_payment = loan_principal - (months - 1) * payment
#        print('Your monthly payment = ' + str(payment) + ' and the last payment = ' + str(last_payment) + '.')
elif user_choice == 'p':
    print('Enter the annuity payment:')
    monthly_payment = float(input())
    print('Enter the number of periods:')
    months = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    nominal_interest_rate = loan_interest / (12 * 100)
    loan_principal = monthly_payment / ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, months))
                                        / (math.pow(1 + nominal_interest_rate, months) - 1))
    print(f'Your loan principal = {loan_principal:.0f}')
