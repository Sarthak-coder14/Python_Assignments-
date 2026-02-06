import hashlib
import os
import sys

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate


def DisplayResult(MyDict):
    fobj = open("Log.txt", "w")

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    if len(Result) == 0:
        fobj.write("No duplicate files found\n")
    else:
        for value in Result:
            fobj.write("Duplicate files are:\n")
            for subvalue in value:
                fobj.write(subvalue + "\n")
            fobj.write("\n")

    fobj.close()

def DeleteDuplicate(Path = "Marvellous"):
    fobj = open("Log.txt","w")

    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                fobj.write("Deleted file : " + subvalue + "\n")
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0
    fobj.write("Total deleted file : " + str(Cnt) + "\n")
    fobj.close()


def main():
    Border = "-" * 50
    print(Border)
    print("Marvellous Directory Automation")
    print(Border)

    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return

    Ret = FindDuplicate(sys.argv[1])
    DisplayResult(Ret)
    DeleteDuplicate(sys.argv[1])

    print("Log file created successfully")


if __name__ == "__main__":
    main()
