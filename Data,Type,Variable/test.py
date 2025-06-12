#dot vector u= i+2j+3k
#           v= 2i+4j+5k
#           u.v= (1x2)+(2x4)+(3x5) = 2+8+15=25

import math
# u = input()
# parts = u.split()
# print(parts)
# ui = int(parts[0])
# uj = int(parts[1])
# uk = int(parts[2])
# print(type(ui)) 
v = int(input())
ui,uj,uk = [float(e) for e in input().split()]
vi,vj,vk = [float(e) for e in input().split()]
dot = (ui*vi)+(uj*vj)+(uk*vk)
print(dot)

