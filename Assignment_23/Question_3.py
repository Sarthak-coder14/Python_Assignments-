class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


def main():
    obj1 = Numbers(6)
    print("Prime:", obj1.ChkPrime())
    obj1.Factors()
    print("Sum of Factors:", obj1.SumFactors())
    print("Perfect:", obj1.ChkPerfect())

    print()

    obj2 = Numbers(17)
    print("Prime:", obj2.ChkPrime())
    obj2.Factors()
    print("Sum of Factors:", obj2.SumFactors())
    print("Perfect:", obj2.ChkPerfect())


if __name__ == "__main__":
    main()