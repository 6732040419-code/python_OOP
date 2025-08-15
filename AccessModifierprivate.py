class Employee:
    def __init__(self, name, salary, department):
        # protected attribute
        self._name = name
        self.__salary = salary
        self.__department = department

    # protected method
    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน = {} '.format(self.__salary))
        print('แผนก = {} '.format(self.__department))

emp1 = Employee('วงศกร', 50000, 'ออกแบบ')
emp1.__salary = 70000
emp1._showData()
