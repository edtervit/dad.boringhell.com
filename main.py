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
    <link rel="apple-touch-icon" sizes="180x180" href="favi/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="favi/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favi/favicon-16x16.png">
    <link rel="manifest" href="favi/site.webmanifest">
    <link rel="mask-icon" href="favi/safari-pinned-tab.svg" color="#5bbad5">
    <link rel="shortcut icon" href="favi/favicon.ico">
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="msapplication-config" content="favi/browserconfig.xml">
    <meta name="theme-color" content="#ffffff">
    <title>Ned's Race Reminder</title>
</head>
<body>
    <h1>Ned's Race Reminder</h1>
    <p> Ticking a box should play a sound 3 minutes before the race starts</p>
    <button class="stop" onclick="alarmSound.pause()">STOP SOUND</BUTTON>
<div class="container">
    '''

main_html = '''
    
''' 
bot_html = '''
</div>
<audio id="alarm" src="sounds/crazy_frog.mp3" preload="auto" hidden></audio>
<script src="ringer.js"></script> 
</body>
</html> '''

for key, value in times_and_tracks.items():
    main_html += "<div class=a_track> \n"
    main_html += "<h2>" + key + "</h2>" + "\n" # for each key (track) make a h2 with its name
    main_html += "  <h3 class='going'>" + value[0] + "</h3>" + "\n" # write first item (going) in the value's list (going+times) 
    main_html += "  <ul class='the_times'>" + "\n"    #create a list opening
    for i in value[1:]: #for each i in list of times create a list item
        main_html += "      <li class ='time'>" + i + "<input type='checkbox' id='" + key + i + "' onclick='checkIfChecked(this)'>" +"<p></p>" +  "</li>" + "\n"
    main_html += "  </ul> \n</div> \n" # closes list
    

final_html = top_html + main_html + bot_html

wr = open('index.html', 'w')
wr.write(final_html)
wr.close()

time.sleep(3)
##Enbale to push final html file to live server
push_live.upload_index()