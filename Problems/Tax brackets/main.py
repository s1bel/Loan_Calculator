income = int(input())
if income > 132406:
    percent = 28
elif income > 42707:
    percent = 25
elif income > 15527:
    percent = 15
else:
    percent = 0

calculated_tax = f'{income / 100 * percent:.0f}'

print("The tax for {} is {}%. That is {} dollars!".format(income, percent, calculated_tax))
