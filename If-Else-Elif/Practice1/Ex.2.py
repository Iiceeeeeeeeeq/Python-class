from math import sqrt
circle1 = input("กรุณาใส่ x y r ของวงกลมที่ 1 และโปรดเว้นช่องว่างแต่ละตัวเลข : ").split()
circle2 = input("กรุณาใส่ x y r ของวงกลมที่ 2 และโปรดเว้นช่องว่างแต่ละตัวเลข : ").split()

x1,y1,r1 = map(float,circle1)
x2,y2,r2 = map(float,circle2)

d = sqrt((x2 - x1)**2 + (y2 - y1)**2)

if d == r1 + r2:
    print("touch")

elif d < r1 + r2:
    print("overlap")

else:
<<<<<<< HEAD
    print("free")
=======
    print("free")
>>>>>>> 15661a26b27b32f87a1a822ad5977d622c6b2b0a
