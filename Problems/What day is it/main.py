offset = int(input())
day = 'Tuesday'
hours = 10

if hours + offset >= 24:
    day = 'Wednesday'
elif hours + offset < 0:
    day = 'Monday'

print(day)
