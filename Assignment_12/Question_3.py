def calculate(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

def main():
    print("Enter first number: ")
    num1 = int(input())
    print("Enter second number: ")
    num2 = int(input())
    
    calculate(num1, num2)

if __name__=="__main__":

    main()
