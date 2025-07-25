# ให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้นคำนวณค่าที่จอดรถที่ต้องจ่ายโดยหลักเกณฑ์การคำนวณมีดังนี้
# 1. จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
# 2. จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของ 
#     ชั่วโมงคิดเป็นหนึ่งชั่วโมง
# 3. จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท   
#      เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
# 4. จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท

# ► ข้อมูลนำเข้า
# มี 4 บรรทัด แต่ละบรรทัดมีจำนวนเต็มหนึ่งจำนวน
# โดยบรรทัดที่ 1-2 เป็นชั่วโมงและนาทีของเวลาเข้า และบรรทัดที่ 3-4 เป็นชั่วโมงและนาทีของเวลาออก

# ► ข้อมูลส่งออก
# มีบรรทัดเดียว เป็นค่าที่จอดรถที่ต้องจ่าย ให้แสดงผลลัพธ์เป็นจำนวนเต็ม

import math
start_hour = int(input("เวลาเข้า(Hr):"))
start_min = int(input("เวลาเข้า(min):"))

end_hour = int(input("เวลาออก(Hr):"))
end_min = int(input("เวลาออก(min):"))

#แปลงเวลาเข้าเเละออกให้เป็นนาทีทั้งหมด
start_total_min = start_hour*60 + start_min
end_total_min = end_hour*60 + end_min

#คำนวณระยะเวลาที่จอดรถ(นาที)
duration_min = end_total_min - start_total_min

#ตรวจสอบเงื่อนไข
if duration_min <= 15:
    fee = 0
else:
    duration_hour = math.ceil(duration_min/60) #ceil ปัดเศษขึ้น

    if duration_hour <= 3:
        fee = duration_hour*10
    
    elif duration_hour <= 6:
        fee = 3*10 + (duration_hour-3)*20
    
    else:
        fee = 200

print ("ค่าที่จอดรถ: ", fee)



    
    
