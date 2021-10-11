import sys
import os

OUTPUT = "./output"

def get_filename(origin, fileNumber):
    return "./output/" + str(origin.removesuffix(".txt")) + "_split_" +str(fileNumber)+ ".txt"

def start_splitting(fileName, rowsPerFile):
    if not os.path.isdir(OUTPUT):
        os.mkdir(OUTPUT)
    
    fileNumber= 1
    row_index = 1
    f = open(fileName, "r")

    if os.path.isfile(get_filename(fileName, fileNumber)):
     decision = input("Warning: Overwriting existing Files! Continue? (Y/N) ")
     if not decision in ["Y", "y"] :
         print("Aborting. Bye!")
         exit(1)

    lines = f.read().splitlines()
    print("Read " + str(len(lines)) + " lines from " + fileName)
    print("Splitting to files...")
    output_file = open(get_filename(fileName, fileNumber), "w")
    
    for row in lines:
        isLastLine = row_index % rowsPerFile == 0
        if not isLastLine:
            row_with_lb = row + '\n'
            output_file.write(row_with_lb)
        else:
            output_file.write(row)
            fileNumber += 1
            if row_index < len(lines):
                output_file = open(get_filename(fileName, fileNumber), "w")
        row_index += 1

    print("Successfully wrote " + str(fileNumber) + " files. Bye.")
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        fileName = sys.argv[1]
        rowsPerFile = int(sys.argv[2])
        print("Started FileSplitter...")
        start_splitting(fileName, rowsPerFile)
    else:
        print("Wrong arguments. Please specify filename and lines-per-file.")
        exit(1)
