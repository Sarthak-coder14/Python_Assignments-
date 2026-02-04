import os

def Display(Filename):


    if(os.path.exists(Filename)):
        fobj = open(Filename,"r")
        print(fobj.read())

        fobj.close()
    else:
        print("This file do not exists in current directory")


def main():
    Ret = False

    print("Enter file name:")
    fname = input()
        
    print("The content of the file is : ")

    Display(fname)


if __name__ == "__main__":
    main()
