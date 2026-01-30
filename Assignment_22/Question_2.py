class Circle:
    
    PI = 3.14

    def __init__(self):
        self.Radiusadius = 0.0
        self.Area = 0.0
        self.circumference = 0.0

    def Accept(self):
        print("Enter the radius")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = self.Radius * self.Radius * Circle.PI

    def CalculateCircumference(self):
        self.circumference = 2 * self.Radius * Circle.PI

    def Display(self):
        print("Radius is : ",self.Radius)
        print("Area is : ",self.Area)
        print("Circumference is : ",self.circumference)

def main():
    obj1 = Circle()
    obj2 = Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()


if __name__ == "__main__":
    main()