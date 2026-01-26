def displayReverse():
    i = 10
    result = ""
    while i >= 1:
        result = result + str(i) + " "
        i -= 1
    print(result)

def main():
    displayReverse()

if __name__ == "__main__":
    main()
