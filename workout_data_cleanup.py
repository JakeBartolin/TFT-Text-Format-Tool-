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

readfile = open("paste_workout_data_here.txt", "r")

Input = []
Output = ""
isFirstExcercise = True

Input = readfile.readlines()

for line in Input:

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

    Output += line[2:]                  # Add line minus the first two characters to Output

    if (Output.endswith('|') == False):
        Output += '|'                   # If no pipe at end of Output, add pipe

# Write the Output to the File
writefile = open("cleaned_data.txt", "w")
writefile.write("|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n|---|---|---|---|---|\n")
writefile.write(Output)
writefile.close()