# เขียนโปรแกรมสร้าง class ชื่อ people โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อบุคคล
# age เป็นอายุของบุคคล
# method
# Introduce() เมื่อเรียกใช้จะพิมพ์ข้อความ
# My name is <name>. I'm <agn> year old

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
            print(f"My name is {self.name} . I'm {self.age} year old")


peo = people('วงศกร', 21)
peo.introduce()