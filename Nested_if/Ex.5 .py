# จงเขียนโปรแกรมระบบประเมินผลพนักงานประจำปี
# บริษัทต้องการประเมินผลพนักงานในแต่ละปี โดยใช้เกณฑ์ดังนี้

#     เงื่อนไข:
#     1. ตำแหน่ง (Position)
#         • Manager
#         • Staff
#         • Intern
#     2. คะแนนประเมินผลงาน (Performance Score) เต็ม 100
#     3. จำนวนวันขาดงาน (Absent Days)

#     กฎการประเมิน
#     • Manager:
#         • ถ้า Performance >= 85 และ Absent <= 3 –> “เลื่อนขั้น”
#         • ถ้า Performance >= 70 แต่ Absent <= 5 –> “รักษาระดับ”
#         • นอกเหนือจากนั้น –> “ต้องปรับปรุง”
#     • Staff:
#         • ถ้า Performance >= 80 และ Absent <= 5 –> “เลื่อนขั้น”
#         • ถ้า Performance >= 60 แต่ Absent <= 7 –> “รักษาระดับ”
#         • นอกเหนือจากนั้น –> “ต้องปรับปรุง”
#     • Intern:
#         • ถ้า Performance >= 90 และ Absent == 0 –> “รับเข้าเป็นพนักงาน”
#         • นอกเหนือจากนั้น –> “ไม่ผ่านทดลองงาน”

print("Q1.Position | Please fill in \"Manager\" , \"Staff\" , \"Intern\"")
POSITION = str(input("Position : "))

print("Q2.Performance Score")
SCORE = int(input("Performance Score : "))

print("Q3.Absent Days")
ABSENT = int(input("Absent Days : "))

if POSITION == "Manager":
    # ถ้า Performance >= 80 และ Absent <= 5 –> “เลื่อนขั้น”
    if SCORE >= 80 and ABSENT <= 5:
        print("get promoted")

    # ถ้า Performance >= 60 แต่ Absent <= 7 –> “รักษาระดับ”
    elif SCORE >= 60 and ABSENT <= 7:
        print("Hold the position")
    
    # นอกเหนือจากนั้น –> “ต้องปรับปรุง”
    else:
        print("Need to improve")

elif POSITION == "Staff":
    # ถ้า Performance >= 85 และ Absent <= 3 –> “เลื่อนขั้น”
    if SCORE >= 85 and ABSENT <= 3:
        print("get promoted")

    # ถ้า Performance >= 70 แต่ Absent <= 5 –> “รักษาระดับ”
    elif SCORE >= 70 and ABSENT <= 5:
        print("Hold the position")
    
    # นอกเหนือจากนั้น –> “ต้องปรับปรุง”
    else:
        print("Need to improve")

elif POSITION == "Intern":
    # ถ้า Performance >= 90 และ Absent == 0 –> “รับเข้าเป็นพนักงาน”
    if SCORE >= 90 and ABSENT == 0:
        print("Get employed")
    
    # นอกเหนือจากนั้น –> “ไม่ผ่านทดลองงาน”
    else:
        print("Failed probation")

else:
    print("Not eligible")