import re
import sys

def GetData():
    print("\n\nPlease paste your data below using Ctrl+Shift+V.\nWhen you are done, press Ctrl+D for Linux/Mac or Ctrl+Z for Windows.\n\n")
    lines = []
    try:
        lines = sys.stdin.readlines()
    except EOFError:
        pass
    return lines

def ProcessData(data):

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

def PrintData(data):
    # Many print() calls are much easier to look at in the code
    # and I'm not too worried about the speed of a 50 line text formatting script.
    print("\n\nYour formatted data is printed below:\n*************************************\n")
    print("|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n|---|---|---|---|---|")
    print(data)
    print("\n*************************************\n")

data = GetData()
data = ProcessData(data)
PrintData(data)