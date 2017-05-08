# import requests
# r = requests.get('https://places.demo.api.here.com/places/v1/discover/explore?at=52.5159%2C13.3777&cat=sights-museums&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg')
# print(r.text)


# import requests
# r = requests.get('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=hinduism')
# print(r.json()["query"]["pages"])

import requests
key = "AIzaSyAbkultYtC9Q4ebcvVv0qGvGNKIUSEX7mE"
place = 'mumbai'
r2 = requests.post("https://maps.googleapis.com/maps/api/geocode/json?address=" + place + ",+CA&key=" + key)
placeres = r2.json()
lat = str(placeres['results'][0]['geometry']['location']['lat'])
lng = str(placeres['results'][0]['geometry']['location']['lng'])

r3 = requests.get('https://places.demo.api.here.com/places/v1/discover/explore?at='+lat+','+lng+'&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg')

regionRes = r3.json()

regionsList = []
for i in range(5):
    regionsList.append([regionRes['results']['items'][i]['title'], regionRes['results']['items'][i]['position']])
print(regionsList)
