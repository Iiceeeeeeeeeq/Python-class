chest = int(input("ขนาดรอบอกของคุณ : "))

if chest >= 46:
    print("ขนาดเสื้อที่เหมาะกับคุณคือ XL")
elif 43 <= chest < 46 :
    print("ขนาดเสื้อที่เหมาะกับคุณคือ L")
elif 41 <= chest < 43 :
    print("ขนาดเสื้อที่เหมาะกับคุณคือ M")
elif 37 <= chest < 41 :
    print("ขนาดเสื้อที่เหมาะกับคุณคือ S")
else:
    print("ขนาดเสื้อที่เหมาะกับคุณคือ XS")