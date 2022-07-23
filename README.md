# TFT (Text Format Tool)
TFT is a simple python script I use to format large bits of text. I use [Joplin](https://joplinapp.org/) to keep track of my workout data, as well as chrord charts and lyrics for any music I'm working on. It keep repetive tasks to a minimum and allows me to focus on getting the data into Joplin and not worrying about playing with markdown.

## Workout Data Formatting
Over the past year or so, I developed a short hand for keeping track of my workout while at the gym. Over time I've developed a bit of a short-hand format. This short hand makes it easy to quickly move on from recording so I can stay focused and get done in a timely manner. TFT simply takes this short hand and refactors it to a Joplin-friendly markdown table that I can then paste into the app.

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

### Shorthand Format Key

```
E:[Excercise Name/Goal Sets.]
S:[Sets that were completed.]
W:[Weight for each set. "2X_" indicates dumbbells.]
R:[Reserve reps after the last set.]
N:[Notes/additional info. Lines start with "-". "tt- " will start a new line in the note.]
```
## Chord Charts and Lyrics Extraction
I also use Jopling to keep track of my chord charts, lyrics, and any short notes about specific song I'm working on. I prefer it to other methods as having markdown avalible to me let's me format lyrics and chords into whatever format I'd like. TFT helps immensely with this. By simply copy/pasting the raw text from something like Ultimate Guitar Tabs, TFT can extract well formatted chord charts and lyrics from the text. This can then be simply pasted into Joplin.

### Text Before Formatting:
![Screenshot from 2022-07-22 17-02-57](https://user-images.githubusercontent.com/105478928/180582529-70c9c47d-dc87-445a-95df-f7aedb186372.png)

### Chord Chart
![Screenshot from 2022-07-22 17-03-24](https://user-images.githubusercontent.com/105478928/180582584-412fa388-e4b7-4bcb-a6cf-4d3fab6f4568.png)

### Lyrics
![Screenshot from 2022-07-22 17-03-54](https://user-images.githubusercontent.com/105478928/180582593-705cc0fc-d0b3-423f-86ef-41d2935d129d.png)
