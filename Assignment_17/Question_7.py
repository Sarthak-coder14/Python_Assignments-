def display(n):
    for i in range(n):
        row = ""
        for j in range(1, n + 1):
            row = row + str(j) + " "
        print(row)

def main():
    num = int(input("Enter number: "))
    display(num)

if __name__ == "__main__":
    main()
