def Content(source,Dest):

    fsrc = open(source, "r")
    fdest = open(Dest, "w")

    fdest.write(fsrc.read())

    fsrc.close()
    fdest.close()

def main():
    print("Enter source file:")
    src = input()

    print("Enter destination file:")
    dest = input()

    Content(src,dest)

    print("File copied successfully")

if __name__ == "__main__":
    main()
