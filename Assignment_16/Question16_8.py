def printStars(n):
    stars = ""
    for i in range(n):
        stars = stars + "* "
    print(stars)

def main():
    print("Enter number: ")
    n = int(input())
    printStars(n)

if __name__ == "__main__":
    main()
