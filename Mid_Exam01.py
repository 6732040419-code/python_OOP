class Driver :
    def __init__(self,HP,generated_money):
        self.HP = HP
        self.generated_money = generated_money

    def drive (self):
        self.HP = self.HP- 10
        self.generated_money = self.generated_money + 10

    def care (self):
        self.HP = self.HP + 10
        self.generated_money = self.generated_money - 10

    def report(self):
        print('HP = {}, Generated Money = {}'.format(self.HP, self.generated_money))

driver_A = Driver(100, 100)
driver_A.drive()
driver_A.report()
driver_A.care()
driver_A.report()