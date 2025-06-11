# ไลบรารี itertools เพื่อใช้สร้างชุด combination ทุกแบบที่เป็นไปได้ของจำนวนแพลน
from itertools import product

# รับค่าจากInput
devices = int(input("Device :"))
download = int(input("Downloads :"))
tv = input("Yes or No :")
resolution = input("SD/HD/FHD/UHD:")
# ---------------------------------------------------------------------------------------------------------

# แปลง resolution ให้อยู่ในรูปแบบที่ตรงกับข้อมูลของแพลนในตาราง
#Full HD, Ultra HD ขอย่อนะ ขก.เขียน 55555555
res_map = {
    "FHD": "Full HD",
    "UHD": "Ultra HD"
}
resolution = res_map.get(resolution, resolution) 
# print(resolution) ^^ บรรทัดบนแค่เอาคำย่อมาเก็บเป็นคำเต็มเฉยๆ จะได้จับคู่กับเเพลนได้

# ลำดับความละเอียด เพื่อให้สามารถเปรียบเทียบได้ว่าแพลนใดมีความละเอียดเท่ากับหรือสูงกว่าที่ผู้ใช้กรอกไว้ก่อนหน้านี้
resolution_order = {"SD": 1, "HD": 2, "Full HD": 3, "Ultra HD": 4}
# ---------------------------------------------------------------------------------------------------------

# ตั้งค่าข้อมูลแต่ละแพลนที่โจทย์ให้มา เขียนแบบเซ็ตไว้ จะได้ดึงไปใช้ทีหลังได้
plans = [
    {"name": "Mobile", "price": 99, "devices": 1, "download": 1, "tv": "No",  "resolution": "SD"},
    {"name": "Basic", "price": 169, "devices": 1, "download": 1, "tv": "Yes", "resolution": "HD"},
    {"name": "Standard", "price": 349, "devices": 2, "download": 2, "tv": "Yes", "resolution": "Full HD"},
    {"name": "Premium", "price": 419, "devices": 4, "download": 6, "tv": "Yes", "resolution": "Ultra HD"},
]
# ---------------------------------------------------------------------------------------------------------

# คัดกรองแพลนที่เหมาะกับ Input
# คือแบบถ้า tv = "Yes" ต้องเลือกเฉพาะแพลนที่รองรับ TV
# และความละเอียดของแพลนต้องเท่ากับหรือสูงกว่าที่ต้องการ
filtered_plans = [
    p for p in plans
    if (tv == "No" or p["tv"] == "Yes") and resolution_order[p["resolution"]] >= resolution_order[resolution]
]
# ---------------------------------------------------------------------------------------------------------

# ปรับจำนวน combination ตั้งค่าจำนวนสูงสุดของแพลนแต่ละชนิดที่จะนำมาทดลอง 
# (ขึ้นอยู่กับจำนวนอุปกรณ์หรือดาวน์โหลดที่ต้องการ)
# เตรียมตัวแปร ราคาที่ถูกที่สุด (min_total) และ รูปแบบการรวมแพลน (best_combo) ที่ดีที่สุด
MAX_COUNT = max(devices, download)  
min_total = float('inf') 
# min_total = float('inf') : inf = infinity
# ให้ min_total เริ่มที่ ∞ ไปก่อน เพราะแบบเปรียบเทียบครั้งแรก "อะไรก็ได้ราคาถูกกว่า ∞ หมด"
best_combo = None
# ---------------------------------------------------------------------------------------------------------

# ลองทุก combination ของจำนวนแพลน (0 ถึง 5 ชุดต่อแพลน)
# ลองทุกความเป็นไปได้ของจำนวนแพลนแต่ละชนิด
for counts in product(range(MAX_COUNT + 1), repeat=len(filtered_plans)):
    # คำนวณ
    total_devices = sum(filtered_plans[i]["devices"] * counts[i] for i in range(len(counts)))
    total_download = sum(filtered_plans[i]["download"] * counts[i] for i in range(len(counts)))
    total_price = sum(filtered_plans[i]["price"] * counts[i] for i in range(len(counts)))
    
    # ถ้า combination นี้ ตอบโจทย์ความต้องการของผู้ใช้ (อุปกรณ์และดาวน์โหลดเพียงพอ) และ ถูกกว่าที่เคยเจอมา ก็เก็บไว้เป็นคำตอบที่ดีที่สุด
    if total_devices >= devices and total_download >= download and total_price < min_total and sum(counts) > 0:
        min_total = total_price
        best_combo = counts

# ---------------------------------------------------------------------------------------------------------    
#แสดงผลลัพธ์
# ถ้ามีแพลนที่ตอบโจทย์: แสดงจำนวนแต่ละแพลนและราคารวม
# ถ้าไม่มี: แสดง 0

if best_combo:
    for i in range(len(best_combo)):
        if best_combo[i] > 0:
            print(f"{filtered_plans[i]['name']} x {best_combo[i]}")
    print(f"Total = {min_total}")
else:
    print("0")
