# Super
# เมื่อต้องการเรียกใช้งานคุณสมบัติต่างๆ ในคลาสแม่
# เช่น Constructor, Method, Attribute

# super().__init__(name)

class Employee:
    # class variable
    minSalary = 12000
    maxSalary = 50000
    companyName = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print('ชื่อพนักงาน = '+self.__name)
        print('เงินเดือน = ', format(self.__salary))
        print('แผนก = '+self.__department)


class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()

class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self,name,salary):
        super().__init__(name, salary,self.__departmentName)
        super()._showData()

class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()
        

account = Accounting("ออย",35000)
programmer = Programmer("นัด",50000)
sale = Sale("คิว",40000)
