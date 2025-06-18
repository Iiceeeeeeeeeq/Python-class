# for loop ใช้เพื่อรันบล็อกของโค้ดโดยมีจำนวนรอบที่แน่นอน ใช้เพื่อวนซ้ำประเภทข้อมูล
# ที่เป็นแบบ sequence เช่น List, Tuple, Dictionary หรือ String เป็นต้น

#การใช้ for loop ร่วมกับ range()
emma = "Emma"
for e in emma:
    print(e)

#--------List------
blackpink = [
    "Jenny",
    "Lisa",
    "Jisoo",
    "Rose"
]
for b in blackpink:
    print(b)

#--------Dic------
pet = {
    'C_name' : "Uta",
    'D_name' : "MhooYoung"
}
for p in pet:
    print(pet[p])
    print("---------------")
# range(start(number), stop(position), step)
for i in range(3,10):
    print (i)