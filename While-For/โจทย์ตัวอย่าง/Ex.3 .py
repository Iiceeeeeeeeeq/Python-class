#Triangle 90 degree
import math
length = int(input())
max_c = 0
                    
for a in range(1, length) :
                       
    for b in range (a, length):
        c = math.sqrt(a**2+b**2)

        if c.is_integer():
            c = int(c)
            # ใช้ได้ทั้ง <= , ==
            if a + b + c == length: 
                if c > max_c:
                   max_c = c
print(max_c)

#----------HomeWork (While loop) -------#





