def Display(Filename, letter):

    fd = open(Filename, "r")

    for line in fd:
        words = line.split()  

        for i in words:
            if i == letter:     
                return True
            else:
                return False
    fd.close()
    
def main():
    Ret = False
    
    print("Enter file name:")
    fname = input()

    print("Enter word to search:")
    word = input()

    Ret = Display(fname, word)

    if (Ret == True):
        print("Word found")
    else:
        print("Word not found")


if __name__ == "__main__":
    main()

    
