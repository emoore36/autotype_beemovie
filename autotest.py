import pyautogui, time

#
# static variables
#

x = 564 - 436

gui = pyautogui
keys = gui.KEYBOARD_KEYS
narcoServerMousePos = {"x": 77, "y": 436}
dumbassNerdsMousePos = {"x": 77, "y": 564}
sedonaBoisMousePos = {"x": 77, "y": 564 + x}
chatBarMousePos = {"x": 781, "y": 1837}
notePadMousePos = {"x": 2264, "y":781}
wordList = []


#
# static functions
#

# Gets the current mouse position after 5 seconds and prints to the console
def findMousePos():
    time.sleep(5)
    callStr = "Mouse at position: {}"
    print(callStr.format(gui.position()))

# windows searches the string 'appName' and runs the result
def openApp(appName, secondsToWait):
    time.sleep(.1)
    gui.press("win")
    time.sleep(.2)
    for char in appName:
        gui.press(char)
    gui.press("enter")
    time.sleep(secondsToWait)

# types each character in string 'word' individually, separated by a return key
def typeWordByChar(word):
    for char in word:
     gui.press(char)
     gui.press("enter")
     time.sleep(0.5)

# types each word in string 'phrase' individually, separated by a return key
def typePhraseByWord(phrase):
    for word in phrase:
     gui.press(word)
     gui.press("enter")
     time.sleep(0.5)

# clicks at the coordinates given in dict 'mousePos'
def clickPosition(mousePos):
    gui.click(mousePos["x"], mousePos["y"])
    time.sleep(.05)

# Types an entire word or phrase immediately before hitting enter
def typeWholeThing(thing, secondsOfSpace):
    for char in thing:
        gui.press(char)
    gui.press("enter")
    time.sleep(secondsOfSpace)
    
def parseFile(fileName):
    # scrape input file
    lineList = []
    file = open(fileName)

    # compile list of lines
    for line in file:
        if str.isspace(line) != True:
            lineList.append(line)    

    tempStr = ""
    # compile list of words
    for line in lineList:
        tempStr = ""
        for char in line:
            if str.isalnum(char):
                tempStr += char
            else:
                if str.isspace(char):
                    wordList.append(tempStr)
                    tempStr = ""

    wordList.append(tempStr)

    file.close()

# execute process
parseFile("input.txt")

openApp("discord", 3)

clickPosition(dumbassNerdsMousePos)

# clickPosition(dumbassNerdsMousePos)
clickPosition(chatBarMousePos)



for word in wordList:
    testString = "@everyone {}"

    typeWholeThing(str.format(testString, word), 1)

exit()