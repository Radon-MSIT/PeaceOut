import time
import json
import requests
import urllib.parse
from twitterSentiment import TweetModel

TOKEN = "354935719:AAGx4axQnvqXllVACIbvjIwT_Tp2GaaMfy4"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


# def send_message(text, chat_id):
#     text = urllib.parse.quote_plus(text)
#     url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
#     get_url(url)

def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]

        # obj = TweetModel()

        # if obj.getFilterTweets("Trump")[0][1]
        # reply = obj.getFilterTweets("Trump")[0][0]
        send_message(text, chat)

def handle_updates(updates):
    state = 0
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        if text == "/done":
            # keyboard = build_keyboard(items)
            send_message("Hope To See You Again", chat)
        elif text == "/start":
            send_message("Welcome to PeaceOut. What are you intrested in?", chat)
        elif text.startswith("/"):
            continue
        else:

            if state == 1:
                key = "AIzaSyAbkultYtC9Q4ebcvVv0qGvGNKIUSEX7mE"
                place = text

                # # twitter
                obj = TweetModel()

                for tweet in obj.getFilterTweets("hinduism"):
                    send_message(tweet,chat)

                r2 = requests.post("https://maps.googleapis.com/maps/api/geocode/json?address=" + place + ",+CA&key=" + key)
                placeres = r2.json()

                lat = str(placeres['results'][0]['geometry']['location']['lat'])
                lng = str(placeres['results'][0]['geometry']['location']['lng'])

                r3 = requests.get('https://places.demo.api.here.com/places/v1/discover/explore?at='+lat+','+lng+'&cat=sights-museums &app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg')

                regionRes = r3.json()

                regionsList = []
                items= []
                for i in range(5):
                    regionsList.append([regionRes['results']['items'][i]['title'], regionRes['results']['items'][i]['position']])
                    items.append(regionRes['results']['items'][i]['title'])

                # send_message(regionsList[0][0], chat)
                keyboard = build_keyboard(items)
                send_message("Select an Place", chat, keyboard)

            if state == 0:
                # getting that religion information
                r1 = requests.get('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles='+text)
                # wiki = r1.json()["query"]["pages"]
                replywiki = r1.text[r1.text.find('"extract"')+11:100]
                send_message(replywiki + "\n\nTell me places you'r intrested in!", chat)
                state = 1


            # items = db.get_items(chat)  ##
            # keyboard = build_keyboard(items)
            # send_message("Select an item to delete", chat, keyboard)
        # else:
        #     db.add_item(text, chat)  ##
        #     items = db.get_items(chat)  ##
        #     message = "\n".join(items)
        #     send_message(message, chat)

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)



def main():
    last_update_id = None
    while True:
        print("getting updates")
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
