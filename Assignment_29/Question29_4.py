import sys

def CompareFile(File1, File2):

    f1 = open(File1, "r")
    f2 = open(File2, "r")

    if File1.read() == File2.read():
        print("Success")
    else:
        print("Failure")

    File1.close()
    File2.close()

def main():

    if len(sys.argv) != 3:
        print("Invalid arguments")
        print("Usage: python Any file which in current directory SourceFile and 2 input is DestinationFile")

    src = sys.argv[1]
    dest = sys.argv[2]

    CompareFile(src,dest)

if __name__ == "__main__":
    main()
