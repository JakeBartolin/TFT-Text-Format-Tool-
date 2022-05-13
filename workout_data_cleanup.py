import re
import sys

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

readfile = open("paste_workout_data_here.txt", "r")

Input = []
Output = ""

Input = readfile.readlines()
Output = ProcessData(Input)

print("|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n|---|---|---|---|---|")
print(Output)