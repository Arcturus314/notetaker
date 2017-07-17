#Kaveh Pezeshki
#V0.01
#This script will output Anki-importable text notecard files generated via scanning a general notes file
#Keywords:
#   def| item:definition will generate a card with 'item' on one side and 'definition' on the other
#File Generation:
#At the terminal, call 'python parser.py <inputfile> <outputfile>', where <inputfile> is the input notes file, and <outputfile> is the output flashcard file. Providing only <inputfile> will write to default <outputfile> 'flashcards.txt'

import sys
card_filename = "flashcards.txt"

def parseFile(inputfile):
    notecards = ""
    lineNumber = 0
    try:
        with open(inputfile, 'r') as f:
            for line in f:
                #print("scanning line: " + line)
                lineNumber += 1
                #keyword 'def'
                if "def|" in line:
                    definition = line.split('|')[1].split(':')
                    definition[1].replace("\n", "")
                    print("item found: " + str(definition))
                    notecards += definition[0] + ';' + definition[1] + '\n'
            print("file successfully parsed")
            return notecards
    except:
        print("error found on line " + str(lineNumber))

def writeFile(outputfile, data):
    try:
        print("writing data: " + data)
        with open(outputfile, 'w') as f:
            f.write(data)
    except:
        print("Unable to write output file")

if len(sys.argv) == 2:
    print("reading from file: " + sys.argv[1])
    print("outputting to default file: " + card_filename)

    notecards = parseFile(sys.argv[1])
    writeFile(card_filename, notecards)

elif len(sys.argv) == 3:
    print("reading from file: " + sys.argv[1])
    print("outputting to file: " + sys.argv[2])
    card_filename = sys.argv[2]

    notecards = parseFile(sys.argv[1])
    writeFile(card_filename, notecards)


else:
    print("Please enter command-line parameters. Further information is given below.")
    print("At the terminal, call 'python parser.py <inputfile> <outputfile>', where <inputfile> is the input notes file, and <outputfile> is the output flashcard file. Providing only <inputfile> will write to default <outputfile> 'flashcards.txt'")

