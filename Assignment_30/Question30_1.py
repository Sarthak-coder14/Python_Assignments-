def Count(Filename):
    count = 0

    fd = open(Filename, "r")

    for i in fd:
        count = count + 1
    return count

    fd.close()

def main():
    Ret = 0

    print("Enter file name:")
    fname = input()

    Ret = Count(fname)

    print("Total number of lines:", Ret)

if __name__ == "__main__":
    main()
