xy = input("โปรดระบุตำแหน่ง (x,y) : ").split()
x,y = map(float,xy)

if x == 0 and y == 0 :
    print("อยู่ที่จุดกำเนิด")

elif x == 0 :
    print("อยู่บนแกน y")

elif y == 0 :
    print("อยู่บนแกน x")

elif x > 0 and y > 0 :
    print("อยู่จตุภาคที่ 1")

elif x < 0 and y > 0 :
    print("อยู่จตุภาคที่ 2")

elif x < 0 and y < 0 :
    print("อยู่จตุภาคที่ 3")

elif x > 0 and y < 0 :
    print("อยู่จตุภาคที่ 4")
