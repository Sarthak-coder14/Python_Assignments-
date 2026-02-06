import os
import sys
import time

def DirectoryFileSearch(DirName ,extension ):

    fobj = open("Marvellous.log","w")

    Border = "-"*50

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directoey Cleaner Script\n")
    fobj.write(Border+"\n")


    Ret = os.path.exists(DirName)
    if (Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False ):
        print("It is not a directory")
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        
        for fname in FileName:
            name, ext = os.path.splitext(fname)
            if(ext == extension):
                fobj.write(fname)

def main():

    Border = "-"*50
    print(Border)
    print("-----------marvellous Directory Automation--------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid Number of arguments")
        print("Please specify the name of directory with extension")
        return
    
    DirectoryFileSearch(sys.argv[1],sys.argv[2])

    print(Border)
    print("-----------marvellous Directory Automation--------")
    print(Border)

if __name__ == "__main__":
    main()