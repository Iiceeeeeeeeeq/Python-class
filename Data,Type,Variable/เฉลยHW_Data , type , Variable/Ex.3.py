#Exercise3
u = input("เวกเตอร์ u = ")[1:-1].split(',')
# print(u)
v = input("เวกเตอร์ v = ")[1:-1].split(',')
# print(v)
u = [float(u[0]),float(u[1]),float(u[2])]
v = [float(v[0]),float(v[1]),float(v[2])]
sum=[u[0]+v[0],u[1]+v[1],u[2]+v[2]]
print(u,"+",v,"=",sum)