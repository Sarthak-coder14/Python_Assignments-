import os

def SearchString(FileName,string):
    count = 0

    fd = open(FileName, "r")

    for i in fd:
        words = i.split()

        for j in words:
            if j == string:
                count = count + 1
    return count

def main():
    Ret = 0
    print("Enter file name:")
    fname = input()

    print("Enter string to search:")
    s = input()

    Ret = SearchString(fname,s)
    

    print(f"{s} appers {Ret} times in file")

if __name__ == "__main__":
    main()
