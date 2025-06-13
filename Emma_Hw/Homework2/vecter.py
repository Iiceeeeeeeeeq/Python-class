import math
u1 = input("Enter u: ")[1:-1].split(',')
v1 = input("Enter v: ")[1:-1].split(',')
u1 = [float(u1[0]),float(u1[1]),float(u1[2])]
v1 = [float(v1[0]),float(v1[1]),float(v1[2])]
result = [(u1[0] + v1[0]) , (u1[1] + v1[1]) , (u1[2] + v1[2])]
print(u1," + ",v1," = ",result)
