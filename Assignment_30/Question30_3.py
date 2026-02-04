def Read(FileName):
    
    fd = open(FileName, "r")

    Count = 1

    for i in fd:
        print(Count, "Line is :")
        print(i)
        Count = Count + 1

    fd.close()

def main():
    print("Enter file name:")
    fname = input()

    Read(fname)

if __name__ == "__main__":
    main()
