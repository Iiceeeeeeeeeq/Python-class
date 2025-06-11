#แสดงข้อมูลที่เป็นจริง (True) เท็จ (False)
# 1. and (&) = True ก็ต่อเมื่อ A&B = True
# 2. or (|) = True ก็ต่อเมื่อ A|B ไม่ A ก้อ B เป็นจริง
# 3. not() = นิเสธ

# ex.1
a= 5<4
b= 10>20
print(a)
print(b)
print(a and b)
print(a or b)
print(not a)
print(not b)

#ex.2 เปลี่ยนคำสั่งจากอุปกรณ์เดิม ให้เป็นคำสั่งใหม่ของเราเอง
#หลอดไฟทำงานมันขึ้น 0 
#หลอดไฟไม่ทำงานมันขึ้น 1 

ON = 0
OFF = 1

ON_Led = not ON
print (ON_Led, "ไฟเปิดอยู่")
OFF_Led = not OFF
print (OFF_Led, "ไฟดับจ้า")

