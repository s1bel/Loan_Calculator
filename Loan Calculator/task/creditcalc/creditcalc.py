import math
import sys

args = sys.argv
formatted_args = []

if len(args) > 4:
    for i in args:
        formatted_args += i.split('=')
    if ('--payment' in formatted_args
        and float(formatted_args[formatted_args.index('--payment') + 1]) < 0) \
            or ('--principal' in formatted_args
                and float(formatted_args[formatted_args.index('--principal') + 1]) < 0) \
            or ('--periods' in formatted_args
                and float(formatted_args[formatted_args.index('--periods') + 1]) < 0) \
            or ('--interest' in formatted_args
                and float(formatted_args[formatted_args.index('--interest') + 1]) < 0):
        print('Incorrect parameters')
    elif '--type' in formatted_args and ('diff' in formatted_args or 'annuity' in formatted_args) \
            and '--interest' in formatted_args:
        interest = float(formatted_args[formatted_args.index('--interest') + 1])
        nom_interest_rate = interest / (12 * 100)

        if 'diff' in formatted_args and '--payment' not in formatted_args:
            principal = float(formatted_args[formatted_args.index('--principal') + 1])
            periods = int(formatted_args[formatted_args.index('--periods') + 1])
            payment_sum = 0
            for m in range(1, periods + 1):
                payment = float(principal / periods + nom_interest_rate * (principal - (principal * (m - 1)) / periods))
                if payment % 1:
                    payment = int(payment) + 1
                else:
                    payment = int(payment)
                payment_sum += payment
                print(f'Month {m}: payment is {payment}')
            overpayment = int(payment_sum - principal)
            print()
            print('Overpayment =', overpayment)
        elif 'annuity' in formatted_args and '--periods' not in formatted_args:
            principal = float(formatted_args[formatted_args.index('--principal') + 1])
            payment = float(formatted_args[formatted_args.index('--payment') + 1])
            overpayment = - principal
            periods = math.log(payment / (payment - nom_interest_rate * principal), (1 + nom_interest_rate))
            if periods % 1 == 0:
                periods = int(periods)
            else:
                periods = int(periods) + 1
            years = periods // 12
            months = periods % 12
            if years == 0:
                print(
                    'It will take ' + str(months) + (' month' if months == 1 else ' months') + ' to repay the loan!')
            elif months == 0:
                print('It will take ' + str(years) + (' year' if years == 1 else ' years') + ' to repay the loan!')
            else:
                print('It will take ' + str(years) + (' year' if years == 1 else ' years') + ' and '
                      + str(months) + (' month' if months == 1 else ' months') + ' to repay the loan!')
            overpayment = int(payment * periods - principal)
            print('Overpayment =', overpayment)
        elif 'annuity' in formatted_args and '--payment' not in formatted_args:
            principal = float(formatted_args[formatted_args.index('--principal') + 1])
            periods = int(formatted_args[formatted_args.index('--periods') + 1])
            payment = principal * (
                            (nom_interest_rate * math.pow(1 + nom_interest_rate, periods))
                            / (math.pow(1 + nom_interest_rate, periods) - 1))
            if payment % 1:
                payment = int(payment) + 1

            print(f'Your annuity payment = {payment}')
            #        last_payment = loan_principal - (months - 1) * payment
            #        print('Your monthly payment = ' + str(payment)
            #        + ' and the last payment = ' + str(last_payment) + '.')
            overpayment = int(payment * periods - principal)
            print('Overpayment =', overpayment)
        elif 'annuity' in formatted_args and '--principal' not in formatted_args:
            periods = int(formatted_args[formatted_args.index('--periods') + 1])
            payment = float(formatted_args[formatted_args.index('--payment') + 1])
            principal = int(payment / (
                            (nom_interest_rate * math.pow(1 + nom_interest_rate, periods))
                            / (math.pow(1 + nom_interest_rate, periods) - 1)))
            print(f'Your loan principal = {principal}!')
            overpayment = int(payment * periods - principal)
            print('Overpayment =', overpayment)
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
