def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width 
    print(f"Rectangle with length {length} and width {width}") # print what number did we put it
    print(f"Area = {length} × {width} = {area}") # what the nuber of area use to calculate and show result
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_trangle_area(height, base):
    """Calculates and displays trangle area"""
    area = 0.5 * height * base
    print(f"Trangle with height {height} and base {base}") # print what number did we put it
    print(f"Area =  0.5 × {height} × {base} = {area}") # what the number of area use to calculate and show result
    print()

print("Calculating triangle areas:")
calculate_trangle_area(5, 3)
calculate_trangle_area(10, 7)

"""
เขียน function แปลงหน่วยเงิน ที่สามารถแปลงเงินจาก
THB <--> USD .. 1 USD = 32 THB
THB <--> JPY .. 100 JPY = 22 THB

โดยใช้ชื่อและการใช้งาน
function_convert_currency(100,"USD")

แสดงผลการทำงานหน้าจอ
100 THB = 3.3 USD

และทดสอยผลการทำงาน function ที่ตัวเองเรียกด้วย
"""

currency = 0.0
type = ""
def function_convert_currency(currency,type):
    if type == "USD":
        new_currency = currency / 32
        print(f"{currency} THB = {new_currency:.1f} USD")

    if type == "JPY":
        new_currency = currency / 22
        print(f"{currency} THB = {new_currency:.1f} JPY")

    if type != "USD" or "JPY":
        print("We have only USD/JPY")
        quit()
        
currency = float(input("How many you want to convert: "))
type = str(input("What type you want to covert USD/JPY: "))
function_convert_currency(currency,type)