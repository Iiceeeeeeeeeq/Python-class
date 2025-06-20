num1,num2,num3,num4,num5 = map(int,input("โปรดใส่จำนวนเต็ม 5 จำนวน เรียงจากน้อยไปมาก : ").split())

if num1 <= num2 <= num3 <= num4 <= num5:
    print("True")
else:
    print("False")