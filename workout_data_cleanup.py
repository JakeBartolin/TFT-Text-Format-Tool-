###        Note about formating
### ----------------------------------
### This script assumes the uncleaned
### data is still formatted in the
### correct manner. See notes below

### E:Excercise Name/Goal Reps
### S:Sets and Reps (SetsXReps)
### W:Weight Used (in lbs)
### R:Reserve Reps
### N:Notes, seperate each note with two
###     't' characters immediatle followed
###     by a dasha and space
###     like so: 'tt- '

import re
import sys

def ProcessData(data):

    isFirstExcercise = True
    output = ""

    for line in data:

        line = re.sub('\n', '', line)       # Remove newline characters


        if (line == ''):                    # If line is empty, skip it
            continue
        elif (line.startswith("N:0")):      # If line is empty note, mark as "N/A"
            line = 'xxN/A'
        elif (line.startswith("E:")):       # If line is excercise, add first pipe
            line = 'xx|' + line[2:]
            if (isFirstExcercise == True):  # If not first excercise, add newline
                isFirstExcercise = False
            else:
                line = 'xx\n' + line[2:]
        elif (line.startswith("N:")):       # If line is note, replace line breaks with actual breaks
            line = re.sub('tt- ', '<br>- ', line)

        output += line[2:]                  # Add line minus the first two characters to Output

        if (output.endswith('|') == False):
            output += '|'                   # If no pipe at end of Output, add pipe
    return output

readfile = open("paste_workout_data_here.txt", "r")

Input = []
Output = ""

Input = readfile.readlines()
Output = ProcessData(Input)

print("|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n|---|---|---|---|---|")
print(Output)