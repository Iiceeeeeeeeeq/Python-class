import math
m = (input("Enter number : "))
n = int(input("How lenth : "))
mlen = len(m)
# if mlen < n:
while len(m) < n: 
    m = "0" + m   
print (m)   

#สงสัยว่าทำไมถึงใช้mlen ไม่ได้ 
#มีคำสั่งไหนที่ตอบโจทย์กว่าอันนี้มั้ยคะ ถ้ามีจัดมาเลยค่า ตอนนี้มีไฟเรียนสุดๆ