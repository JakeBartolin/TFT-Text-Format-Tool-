# WorkoutDataCleanup
WorkoutDataCleanup.py is a simple python script I use to format my workout data. I use [Joplin](https://joplinapp.org/) to keep track of my reps/sets/etc. Over time I've developed a bit of a short-hand format to keep me moving while I'm in the gym. This short hand makes it easy to quickly move on from recording so I can stay focused and get done in a timely manner. WorkoutDataCleaner.py simply takes this short hand and refactors it to a Joplin-friendly markdown table that I can then paste into the app.

```
Example Short Hand Data:

E:Standing Dumbbell Overhead Press 3x10
S:3X10
W:2X20
R:3-5
N:- Definitely up a weight next week

E:Standing Dumbbell Rows 3x10
S:3X10
W:2X20
R:4+
N:- Calibration weighttt- Really felt some burn but could definitely go up again next week
```
![Screenshot from 2022-05-24 13-24-10](https://user-images.githubusercontent.com/105478928/170095591-e3554f53-bbb0-4328-b3c2-8fac6fe99aca.png)

# Short Hand Formatting
The formatting for the short-hand is quite simple.

```
E:[Excercise Name/Goal Sets.]
S:[Sets that were completed.]
W:[Weight for each set. "2X_" indicates dumbbells.]
R:[Reserve reps after the last set.]
N:[Notes/additional info. Lines start with "-". "tt- " will start a new line in the note.]
```
