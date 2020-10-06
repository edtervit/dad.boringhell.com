import requests
from bs4 import BeautifulSoup

def get_data():
    #gets the webpage containting race info
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    data = requests.get('https://www.timeform.com/horse-racing/racecards', headers=headers)

    #parses page into html
    soup = BeautifulSoup(data.text, 'html.parser')

    #finds all the meetings from html
    meetings = soup.find_all(class_="w-racecard-grid-meeting")

    #create dictionaries to store data
    times_and_tracks = {}



    #for each meeting, look for it's name, going and all the times that match with the name. For each meeting, add it's name as the dictionary key and a list first list item being going and the rest are times as its values. 

    for a_meeting in meetings:

        track = a_meeting.find("h2").text #track name as string

        times_list = a_meeting.find_all("b") #this works but includes the going sometimes

        all_times = [] # creates list to add times into
        for a_time in times_list:
            
            time = a_time.text #time as string

            all_times.append(time)


        times_and_tracks[track] = all_times       


    return times_and_tracks





