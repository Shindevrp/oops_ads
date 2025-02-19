import math
class complexNumber:
    def __init__(self):
        self.real=0.0
        self.imaginary=0.0
    def initialize(self,real, imaginary):
        self.real=float(real)
        self.imaginary=float(imaginary)
        print(f"Initialized: {self}")
    def add(self,real, imaginary):
        
        self.real+=real
        self.imaginary+=imaginary
        print(f"After addition: {self}")
    def subtract(self,real, imaginary):
        self.real-=real
        self.imaginary-=imaginary
        print(f"After subtraction: {self}")
    def multiply(self,real,imaginary):
        a=(self.real*real)-(self.imaginary*imaginary)
        b=(self.real*imaginary)+(self.imaginary*real)
        self.real=a
        self.imaginary=b
        print(f"After multiplication: {self}")
    def divide(self,real,imaginary):
        dmt=math.pow(real,2)+math.pow(imaginary,2)
        if dmt==0:
            print("Error: Division by zero is not allowed.")
        else:
            a=(self.real*real+self.imaginary*imaginary)/dmt
            b=(self.imaginary*real-self.real*imaginary)/dmt
            self.real=a
            self.imaginary=b


            print(f"After division: {self}")
    def modulus(self):
        a=math.sqrt(math.pow(self.real,2)+math.pow(self.imaginary,2))
        print(f"Modulus: {a}")
    def conjugate(self):
        self.imaginary=-self.imaginary


        print(f"Conjugate: {self}")
    def __str__(self):
        if self.imaginary>=0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"
        
    def chechCondition(self):
        while True:
            nums=input().split()
            if nums[0]=="exit":
                break
            else:
                part_input=nums[1].split(",")
                
                if nums[0]=="initialize":
                    self.initialize(float(part_input[0]),float(part_input[1]))
                elif nums[0]=="add":
                    self.add(float(part_input[0]),float(part_input[1]))
                elif nums[0]=="subtract":
                    self.subtract(float(part_input[0]),float(part_input[1]))
                elif nums[0]=="multiply":
                    self.multiply(float(part_input[0]),float(part_input[1]))
                elif nums[0]=="divide":
                    self.divide(float(part_input[0]),float(part_input[1]))
                elif nums[0]=="modulus":
                    self.modulus()
                elif nums[0]=="conjugate":
                    self.conjugate()







if __name__ == "__main__":
    c = complexNumber()
    c.chechCondition()



