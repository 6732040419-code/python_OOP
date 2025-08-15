# เขียนโปรแกรมสร้าง class ชื่อ Human โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อของบุคคล
# age เป็นอายุของบุคคล
# method
# aging(year) รับ parameter 1 ตัว คือ year
# - แสดงอายุปัจจุบัน
# - เพิ่มอายุขึ้นเท่ากับ year
# - แสดงอายุหลังเพิ่มแล้ว

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self, year):
        print(f"อายุปัจจุบัน = {self.age}")
        self.age = self.age + year
        print(f"อายุที่ต้องเพิ่ม = {year}")
        print(f"อายุหลังเพิ่มแล้ว = {self.age}")

vip = Human('วงศกร', 21)
vip.aging(3)


