import time

# open and read the input file
inputFile = open("input.txt", "r")
index = 0

# create an interable of textfile lines
lines = []

# populate list
for line in inputFile:
    lines.append(line)


# print each line of the input file
for line in lines:
    
    print(line)
    time.sleep(0.1)

# close the file
inputFile.close()


# create/open output file
outputFile = open("output.txt", "w")

# print each line to the output file
for line in lines:
    outputFile.write(line)

# close the output file
outputFile.close()