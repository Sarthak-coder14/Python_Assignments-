import os

def Checkfile(Filename):

    if os.path.exists(Filename):
        return True
        
    else:
        return False


def main():
    Ret = False

    print("Enter file name:")
    fname = input()

    Ret = Checkfile(fname)

    if(Ret == True):
        print(fname," is exists in current directory")

    else:
        print(fname,"do not exists in current directory")

if __name__ == "__main__":
    main()
