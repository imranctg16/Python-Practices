class Test:
    def __init__(self):
        self.name = "John"
        self.age = 30
        self.address = "123 Main St"
        self.email = "8I2eA@example.com"

    def printDetails(self):
        print("name : ", self.name + " age : " + str(self.age) + " address : " + self.address + " email : " + self.email)


class Test2(Test):
    def info(self):
        self.printDetails()

test = Test2()
test.printDetails()