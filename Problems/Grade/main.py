score = int(input())
maximum = int(input())

score_percents = score / maximum * 100

if score_percents >= 90:
    print('A')
elif score_percents >= 80:
    print('B')
elif score_percents >= 70:
    print('C')
elif score_percents >= 60:
    print('D')
else:
    print('F')
