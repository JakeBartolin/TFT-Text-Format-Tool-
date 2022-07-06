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
2) Format Chord Charts
3) Extract Lyrics
x) Exit

"""

    print(welcomeMessage)

    while isActive == True:
        print(functionSelect)
        userInput = input()

        if userInput == "1":
            FormatWorkoutData()
        elif userInput == "2":
            FormatChordCharts()
        elif userInput == "3":
            ExtractLyrics()
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
    print("Starting Format Workout Data subscript...\n")
    text = GetText()
    text = ProcessWorkoutData(text)
    PrintWorkoutData(text)
    return

def FormatChordCharts():
    text = GetText()
    output = ""

    for line in text:
        if line == "\n":
            continue
        else:
            output = output + line

    print("Your chord chart is printed below:\n******************************\n\n\n")
    print(output)
    return

def ExtractLyrics():
    text = GetText()
    output = ""

    for line in text:
        if line == "\n":
            continue

        if line == "[Chorus]":
            line = "# Chorus"
        
        output += line
    
    print(text)
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
    # Many print() calls are much easier to look at in the code
    # and I'm not too worried about the speed of a 50 line text formatting script.
    print("\n\nYour formatted data is printed below:\n\n")
    print("|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n|---|---|---|---|---|")
    print(data)
    print("\n\n")

Main()
