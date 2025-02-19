class Car:
    def __init__(self,licensePlate,model,parkingTime):
        self.licensePlate = licensePlate
        self.model = model
        self.parkingTime = parkingTime

    def getLicensePlate(self):
        return self.licensePlate
    def getModel(self):
        return self.model
        

class ParkingLot:
    def __init__(self) -> None:
        self.parkCars=[]

    def parkCar(self,car):
        self.parkCars.append(car)

    def removeCar(self,license):
        for car in self.parkCars:
            if car.licensePlate ==license:
                self.parkCars.remove(car)
                return True
        return False
    
    def displayCars(self):
        return self.parkCars
            
