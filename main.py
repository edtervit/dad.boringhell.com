import push_live
import get_data

import time

#gets the tracks and their times/goings. Storing them in two dictionaries.
times_and_tracks = get_data.get_data()





top_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Ned's Race Reminder</title>
</head>
<body>
    <h1>Ned's Race Reminder</h1>
    <p> Ticking a box should play a sound 3 minutes before the race starts</p>
    <button class="stop" onclick="alarmSound.pause()">STOP SOUND</BUTTON>
    
    '''

main_html = '''
    
''' 
bot_html = '''

<audio id="alarm" src="sounds/crazy_frog.mp3" preload="auto" hidden></audio>
<script src="ringer.js"></script> 
</body>
</html> '''

for key, value in times_and_tracks.items():
    main_html += "<h2>" + key + "</h2>" + "\n" # for each key (track) make a h2 with its name
    main_html += "  <h3 class='going'>" + value[0] + "</h3>" + "\n" # write first item (going) in the value's list (going+times) 
    main_html += "  <ul class='the_times'>" + "\n"    #create a list opening
    for i in value[1:]: #for each i in list of times create a list item
        main_html += "      <li class ='time'>" + i + "<input type='checkbox' id='" + key + i + "' onclick='checkIfChecked(this)'>" + "</li>" + "\n"
    main_html += "  </ul>" # closes list
    

final_html = top_html + main_html + bot_html

wr = open('index.html', 'w')
wr.write(final_html)
wr.close()

time.sleep(3)
##Enbale to push final html file to live server
push_live.upload_index()