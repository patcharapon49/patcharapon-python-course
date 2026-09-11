def calculate_electricity_cost(units):
    cost_1 = min(units, 50) * 2.50
    cost_2 = min(max(units - 50, 0), 50) * 3.00
    cost_3 = min(max(units - 100, 0), 100) * 3.50
    cost_4 = max(units - 200, 0) * 4.00
    service_charge = 25.00

    total = cost_1 + cost_2 + cost_3 + cost_4 + service_charge

    return cost_1, cost_2, cost_3, cost_4, service_charge, total


while True:
    print("===== โปรแกรมคำนวณค่าไฟฟ้า =====")
    print("1. คำนวณค่าไฟ")
    print("2. ออกจากโปรแกรม")

    choice = input("เลือกเมนู: ")

    if choice == "1":
        try:
            units = float(input("\nกรอกจำนวนหน่วยไฟฟ้า: "))

            if units < 0:
                print("จำนวนหน่วยไฟฟ้าไม่ถูกต้อง")
                continue

            cost_1, cost_2, cost_3, cost_4, service_charge, total = calculate_electricity_cost(units)

            print()
            print("รายละเอียดค่าไฟ:")

            if units > 0:
                print(f"1-50 หน่วย: {cost_1:.2f} บาท")

            if units > 50:
                print(f"51-100 หน่วย: {cost_2:.2f} บาท")

            if units > 100:
                print(f"101-{min(units, 200):g} หน่วย: {cost_3:.2f} บาท")

            if units > 200:
                print(f"มากกว่า 200 หน่วย: {cost_4:.2f} บาท")

            print(f"ค่าบริการ: {service_charge:.2f} บาท")
            print(f"รวมค่าไฟทั้งสิ้น: {total:.2f} บาท")
            print()

        except ValueError:
            print("จำนวนหน่วยไฟฟ้าไม่ถูกต้อง")

    elif choice == "2":
        print("ออกจากโปรแกรม")
        break

    else:
        print("กรุณาเลือกเมนู 1 หรือ 2")