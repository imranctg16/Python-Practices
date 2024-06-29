class ParkingSystem:

    
    def __init__(self, big: int, medium: int, small: int):
        self.arr = [0, big, medium, small]
    def addCar(self, carType: int) -> bool:
        #if available use it and thjen return true
        #else return false
        if self.arr[carType] > 0:
            self.arr[carType] -= 1
            return True
        else:
            return False
        



obj = ParkingSystem(1,1,0)
param_1 = obj.addCar(1)
param_1 = obj.addCar(1)
param_1 = obj.addCar(1)