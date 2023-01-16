# Use
`workout_data_cleanup` is a simple python script I use to format my workout data I generate while I'm in the gym. I use [Joplin](https://joplinapp.org/) to keep track of reps/excercises. While markdown tables look nice, they're not something I want to create while I'm excercising.

Over the past year or so, I developed a short hand for keeping track of my workout while at the gym. This short hand makes it easy to quickly move on from recording so I can stay focused and get done in a timely manner. this script simply takes this short hand and reformats it to a Joplin-friendly markdown table that I can then paste into the app.

# Before/After
```
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

# Shorthand Format Key

```
E:[Excercise Name/Goal Sets.]
S:[Sets that were completed.]
W:[Weight for each set. "2X_" indicates dumbbells.]
R:[Reserve reps after the last set.]
N:[Notes/additional info. Lines start with "-". "tt- " will start a new line in the note.]
```