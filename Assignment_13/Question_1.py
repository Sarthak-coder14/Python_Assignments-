def area_rectangle(l, w):
    return l * w

def main():
    print("Enter length: ")
    length = float(input())
    print("Enter width: ")
    width = float(input())
    print("Area of Rectangle:", area_rectangle(length, width))

if __name__ == "__main__":
    main()
