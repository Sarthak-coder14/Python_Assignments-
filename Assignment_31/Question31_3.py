import os
import sys

def DirectoryFileSearch(DirName ,src, dest ):

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
            if(ext == src):
                old_path = os.path.join(FolderName, fname)
                new_path = os.path.join(FolderName, name + dest)
                os.rename(old_path, new_path)
                print("renamed")
                print(new_path)
                

def main():

    if(len(sys.argv) != 4):
        print("Invalid Number of arguments")
        print("Please specify the name of directory with extension")
        return
    src = sys.argv[2]
    dest = sys.argv[3]
    DirectoryFileSearch(sys.argv[1],src,dest)

if __name__ == "__main__":
    main()