#จงเขียนโปรแกรมระบบคัดเลือกพนักงานเข้าทำงานในบริษัท ABC โดยใช้เงื่อนไขดังนี้
    # 1. เพศ (Gender) - เฉพาะรับเฉพาะ ชาย (M) และ หญิง (F) เท่านั้น
    # 2. อายุ (Age) - ต้องอยู่ระหว่าง 22 ถึง 35 ปี
    # 3. วุฒิการศึกษา (Degree) - ต้องเป็นอย่างน้อยปริญญาตรี (Bachelor)
    # 4. ประสบการณ์ทำงาน (Experience)
    #     • ถ้ามีประสบการณ์ มากกว่าหรือเท่ากับ 3 ปี จะได้รับการพิจารณาพิเศษ
    #     • ถ้ามีประสบการณ์ น้อยกว่า 3 ปี จะต้องมีคะแนนสอบสัมภาษณ์ 
    #       (Interview Score) มากกว่าหรือเท่ากับ 80 ถึงจะผ่าน

    # 5. แสดงผลดังนี้:
    #     • “ผ่านการคัดเลือกแบบพิเศษ”
    #     • “ผ่านการคัดเลือก”
    #     • “ไม่ผ่านการคัดเลือก”
GENDER = str(input("What is your gender. Please fill in with 'M' (Male) or 'F' (Female): "))

# เพศ (Gender) - เฉพาะรับเฉพาะ ชาย (M) และ หญิง (F) เท่านั้น
if GENDER == "M" or GENDER == "F":
    AGE = int(input("How old are you : "))

    # อายุ (Age) - ต้องอยู่ระหว่าง 22 ถึง 35 ปี
    if 22 <= AGE <= 35:
        DEGREE = str(input("Your degree : "))

        # วุฒิการศึกษา (Degree) - ต้องเป็นอย่างน้อยปริญญาตรี (Bachelor)
        if DEGREE == "Bachelor" or DEGREE == "Master's degree" or DEGREE == "Doctoral degree":
            EXPERIENCE = float(input("Your work experience(year): "))

            # ประสบการณ์ทำงาน (Experience)
            if EXPERIENCE >= 3:
                # ถ้ามีประสบการณ์ มากกว่าหรือเท่ากับ 3 ปี จะได้รับการพิจารณาพิเศษ
                print("You have passed the special selection.")

            elif EXPERIENCE < 3:
                # ถ้ามีประสบการณ์ น้อยกว่า 3 ปี จะต้องมีคะแนนสอบสัมภาษณ์
                print("As you have under 3 years of experience, we’ll proceed with an interview.")
                INTERVIEW_SCORE = float(input("Your interview score is : "))

                if INTERVIEW_SCORE >= 80:
                    # (Interview Score) มากกว่าหรือเท่ากับ 80 ถึงจะผ่าน
                    print("You have been selected.")
    
                else:
                    print("You were not selected.")

        else:
            print("You were not selected.")
    else:
        print("You were not selected.")

else:
    print("You were not selected.")