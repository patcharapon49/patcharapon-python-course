""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"

อย่าลืมเขียนส่งโปรแกรมของส่วนในการทดลองใช้งานมาด้วย เอาซัก 3 ลูกค้า
"""

def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    user_premium = "Standard User"
    if premium == True:
        user_premium = "Premium User"

    print(f"Your username is {username}, Your Age is {age} - You are {user_premium}")

create_user_profile("Boss")
create_user_profile("John", 25,)
create_user_profile("Arm", 20, True)