#Average Until -1
sum = 0
count = 0
while True :
    number = float(input())
    if number == -1 :
        break
    sum += number 
    count += 1

if count ==0:
    print("NO data")
else:
    average = sum/count
    print(average)

#-------------------ลองใช้ if-----------------------------------
sum = 0
count = 0

for i in range(1000):
    number = float(input())
    if number == -1 :
        break
    sum += number 
    count += 1

if count ==0:
    print("NO data")
else:
    average = sum/count
    print(average)
    

