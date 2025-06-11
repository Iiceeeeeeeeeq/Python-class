#Exercise2
M = input() #ใส่ตัวเลขกี่หนักก้อได้
N = int(input()) #กำหนดจำนวนหลัก
value = N-len(M) #หาจำนวนเลข 0 ที่ต้องใส่
print(type(len(M)), len(M))
print(value*'0'+ M)