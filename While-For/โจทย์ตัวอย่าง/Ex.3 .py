#Triangle 90 degree

import math
n = int(input())  # รับค่ารอบรูปสูงสุด
max_c = 0         # ตัวแปรเก็บด้านตรงข้ามมุมฉากที่มากที่สุด

# ลองค่าทุกคู่ของ a และ b ที่เป็นไปได้
for a in range(1, n):
    for b in range(a, n):  # b เริ่มจาก a เพื่อไม่ให้ซ้ำ
        c = math.sqrt(a**2 + b**2)
        # c2 = a**2 + b**2
        # c = c2**0.5
        if c.is_integer():  # ตรวจสอบว่า c เป็นจำนวนเต็ม
            c = int(c)
            if a + b + c <= n:
                if c > max_c:
                    max_c = c

print(max_c)



