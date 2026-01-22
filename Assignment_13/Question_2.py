def area_circle(r):
    return 3.14 * r * r

def main():
    print("Enter radius: ")
    radius = float(input())
    print("Area of Circle:")
    print(area_circle(radius))

if __name__ == "__main__":
    main()
