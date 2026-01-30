class Demo:
    
    Value = 0

    def __init__(self,A,B):   
        self.Value1 = A
        self.Value2 = B
        

    def fun(self):
        print("Inside fun")
        print(self.Value1)
        print(self.Value2)

    def gun(self):
        print("Inside gun")
        print(self.Value1)
        print(self.Value2)

def main():
    obj1 = Demo(11,10)
    obj2 = Demo(51,101)

    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()


if __name__ == "__main__":
    main()