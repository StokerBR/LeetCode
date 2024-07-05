class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = {
            1: {
                'count': 0,
                'max': big
            },
            2: {
                'count': 0,
                'max': medium
            },
            3: {
                'count': 0,
                'max': small
            },
        }

    def addCar(self, carType: int) -> bool:
        parking = self.parking[carType]
        if parking['max'] > parking['count']:
            self.parking[carType]['count'] += 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)