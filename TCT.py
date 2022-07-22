import re
import sys

def Main():
    userInput = ""
    isActive = True
    welcomeMessage = """Starting TFT Script...

********************
* Text Format Tool *
******************** 

"""
    functionSelect = """Please select a function:
1) Format Workout Data
2) Formate Chord Chart and Lyrics
x) Exit

"""

    print(welcomeMessage)

    while isActive == True:
        print(functionSelect)
        userInput = input()

        if userInput == "1":
            FormatWorkoutData()
        elif userInput == "2":
            FormatChordChartAndLyrics()
        elif userInput == "x":
            isActive = False
        else:
            print("Sorry, not a valid entry, please try again.\n\n")

    print("Exiting Script....")

def GetText():
    
    print("Please paste your data below using Ctrl+Shift+V.\nWhen you are done, press Ctrl+D for Linux/Mac or Ctrl+Z for Windows.\n")
    lines = []
    try:
        lines = sys.stdin.readlines()
    except EOFError:
        pass
    return lines

def FormatWorkoutData():
    print("Starting Format Workout Data Subscript...\n")
    text = GetText()
    text = ProcessWorkoutData(text)
   
    print("\n\nYour formatted data is printed below:\n\n")
    print(f"|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n|---|---|---|---|---|{text}\n\n")

    return

def FormatChordChartAndLyrics():
    print("Starting Extract Chords and Lyrics Subscript...\n")
    text = GetText()

    print("********************************\n*Your chords are printed below:*\n********************************\n")
    print(ExtractChordChart(text) + "\n\n")

    print("********************************\n*Your lyrics are printed below:*\n********************************\n")
    print(ExtractLyrics(text))

def ExtractChordChart(text):
    output = ""

    for line in text:
        if line == "\n":
            continue
        else:
            output = output + line
            
    return output

def ExtractLyrics(text):
    output = ""

    for line in text:
        spaceCount = 0

        if line == "\n":
            continue

        if line.startswith(" "):
            line = line.replace(" ", "", 1)
        
        for character in line:
            if character == " ":
                spaceCount += 1
        if spaceCount > (len(line) / 3):
            continue

        if line == "[Intro]":
            continue

        if line.__contains__("[Chorus]"):
            line = line.replace("[Chorus]", "## Chorus")
        elif line.__contains__("[Verse]"):
            line = line.replace("[Verse]", "## Verse")
        elif line.__contains__("[Bridge]"):
            line = line.replace("[Bridge]", "## Bridge")
        elif line.__contains__("[Solo]"):
            line = line.replace("[Solo]", "## Solo")
        
        output += line
    
    print(output)
    return

def ProcessWorkoutData(data):

    isFirstExcercise = True
    output = ""

    for line in data:

        line = re.sub('\n', '', line)

        if (line == ''):
            continue
        elif (line.startswith("N:0")):
            line = 'xxN/A'
        elif (line.startswith("E:")):
            line = 'xx|' + line[2:]
            if (isFirstExcercise == True):
                isFirstExcercise = False
            else:
                line = 'xx\n' + line[2:]
        elif (line.startswith("N:")):
            line = re.sub('tt- ', '<br>- ', line)

        output += line[2:]

        if (output.endswith('|') == False):
            output += '|'
    return output

def PrintWorkoutData(data):
    print("\n\nYour formatted data is printed below:\n\n")
    print(f"|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n|---|---|---|---|---|{data}\n\n")

Main()
