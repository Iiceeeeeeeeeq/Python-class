#Exercise5
d,m,y = input().split('/')
m = int(m)
months = [
    'January',
    'February',
    'march',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
# print(months[m], d+',' ,y)
print(months[m-1], d+',' ,y)