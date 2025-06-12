#จงเขียนโปรแกรมระบบตรวจสอบสิทธิ์รับวัคซีนพิเศษ รัฐบาลเปิดโครงการวัคซีนพิเศษให้ประชาชน โดยมีเงื่อนไขดังนี้

# เงื่อนไข:
#     1. อายุ (Age)
#     2. กลุ่มเสี่ยง (Risk Group)
#         • ตั้งครรภ์
#         • ผู้สูงอายุ
#         • บุคลากรการแพทย์
#         • ไม่มี
#     3. โรคประจำตัว (Chronic Disease)
#         • มี
#         • ไม่มี

# กฎการอนุมัติวัคซีน
#  • ถ้าเป็นบุคลากรการแพทย์ –> “ได้รับสิทธิ์วัคซีนทันที”
#  • ถ้าอายุมากกว่า 60 และเป็นกลุ่มเสี่ยงใด ๆ –> “ได้รับสิทธิ์วัคซีน”
#  • ถ้าอายุมากกว่า 40 และมีโรคประจำตัว –> “ได้รับสิทธิ์วัคซีน”
#  • ถ้าอายุมากกว่า 18 และไม่มีความเสี่ยง –> “รอเรียกตามคิว”
#  • นอกเหนือจากนี้ –> “ยังไม่เข้าเกณฑ์”

print("This is a special vaccine eligibility checking system.\
 Please answer the following questions truthfully.")

#ข้อมูลเงื่อนไขที่ 1
print("Q.1 : AGE")
AGE = int(input("How old are you : "))

#ข้อมูลเงื่อนไขที่ 2
print("Q2 : Are you in any of the following risk groups? Please answer T(True) or F(False).")
RISK_G1 = str(input("Are you pregnant? : "))
RISK_G2 = str(input("Are you a healthcare worker? : "))
#ไม่ได้ใส่ผู้สูงอายุเพราะผู้สูงอายุหมายถึงบุคคลที่มีอายุ 60 ปีขึ้นไป เพราะงั้นจะประมวลผ่าน AGE

#ข้อมูลเงื่อนไขที่ 3
print("Q3 : Chronic Disease. Please answer T(True) or F(False).")
CHRONIC = str(input("Do you have any chronic diseases? : "))

if RISK_G2 == "T" and AGE >= 18:
    print("You are eligible for immediate vaccination.")

elif RISK_G2 == "F" and RISK_G1 == "T":

    if AGE >= 18:
        print("You are eligible for immediate vaccination.")

elif RISK_G2 == "F" and RISK_G1 == "F" and CHRONIC == "T":

    if AGE >= 60:
        print("You are eligible for immediate vaccination.")
    
    elif 18 <= AGE <= 59:
        print("You are eligible for immediate vaccination.")
    
    else:
        print("You are not eligible yet.")

elif RISK_G2 == "F" and RISK_G1 == "F" and CHRONIC == "F":
    if AGE >= 60:
        print("You are eligible for immediate vaccination.")
    
    elif 18 <= AGE <= 59:
        print("You are not eligible yet.")

else:
    print("You are not eligible yet.")