import os
import sys
import shutil
import time

def DirectoryCopyExt(SourceDir, DestDir, Ext):

    fobj = open("Log.txt", "w")
    Border = "-" * 50

    fobj.write(Border + "\n")
    fobj.write("Marvellous Directory Automation\n")
    fobj.write("Log created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n")

    if not os.path.exists(SourceDir):
        print("Source directory does not exist\n")
        return

    if not os.path.isdir(SourceDir):
        print("Source is not a directory\n")
        return

    if not os.path.exists(DestDir):
        os.makedirs(DestDir)
        fobj.write("Destination directory created\n")

    CopyCount = 0

    for FolderName, SubFolder, FileNames in os.walk(SourceDir):
        for fname in FileNames:
            if fname.endswith(Ext):
                src_path = os.path.join(FolderName, fname)
                dest_path = os.path.join(DestDir, fname)

                shutil.copy(src_path, dest_path)
                fobj.write(f"Copied file : {src_path} -> {dest_path}\n")
                CopyCount += 1

    fobj.write(Border + "\n")
    fobj.write(f"Total files copied : {CopyCount}\n")
    fobj.write("End of Application\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():

    if len(sys.argv) != 4:
        print("Usage : DirectoryCopyExt.py <SourceDir> <DestDir> <Extension>")
        return

    DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
