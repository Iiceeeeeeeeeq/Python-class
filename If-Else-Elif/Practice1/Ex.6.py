a = int(input("โปรดใส่จำนวนเต็มหนึ่งจำนวน : "))
x = round(a**(1/3))

if x**3 == a:
    print(x)
else:
    print("not found")

