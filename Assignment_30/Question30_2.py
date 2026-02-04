def Word(FileName):
    
    fd = open(FileName, "r")

    data = fd.read()

    words = data.split()

    print("Total number of words:", len(words))

    fd.close()

def main():
    print("Enter file name:")
    fname = input()

    Word(fname)

if __name__ == "__main__":
    main()
