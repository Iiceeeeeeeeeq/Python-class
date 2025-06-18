#Multiple of 3 0r 5
n = int(input())
sum = 0

for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

#----------------------------------------------

n = int(input())
sum = 0
i = 0
while i<n:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1
print(sum)          










