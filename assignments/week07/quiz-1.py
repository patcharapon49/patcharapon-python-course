"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        self.area = self.width * self.length
        return self.area

    # Method to get the perimeter
    def get_perimeter(self):
        self.perimeter = self.length * 4
        return self.perimeter


rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

"""
เขียนclasscircle ที่ทำงานคล้ายคลึงกับ classrectangle

"""
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        self.area = self.radius * (3.14 ** 2)
        return f"Your Area of Circle is {self.area:.2f}"

    def get_perimeter(self):
        self.perimeter = 2 * 3.14 * self.radius
        return f"Your Perimeter of Circle is {self.perimeter:.2f}"

myCircle = Circle(10)
print(myCircle.get_area())
print(myCircle.get_perimeter())