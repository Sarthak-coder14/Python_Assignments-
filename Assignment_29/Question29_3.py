import sys
import os

def CopyContent(copyFile, Pastfile):

    if(os.path.exists(copyFile) == False):
        print("Source file does not exist")
    else:     
        cobj = open(copyFile, "r")

        pobj = open(Pastfile, "w")

        pobj.write(cobj.read())

        print("File copied successfully")

        cobj.close()
        pobj.close()

def main():

    if len(sys.argv) != 3:
        print("Invalid arguments")
        print("Usage: python Any file which in current directory SourceFile and 2 input is DestinationFile")

    src = sys.argv[1]
    dest = sys.argv[2]

    CopyContent(src,dest)

if __name__ == "__main__":
    main()
