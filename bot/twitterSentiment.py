import tweepy
from textblob import TextBlob

List = []
consumer_key = 'tR4VzkusECZYtw3f2anQQjG51'
consumer_secret = 'mFSYaOCkj8Xqn6YV0Zj9NkcDyiCF5nzsvIEHFxzxA854w7baOt'
access_token = '332069819-xFQOlZSM2VS9DttghL8WIJKfz1e5JNJy96VWOR5H'
access_token_secret = 'WuELR3tHldTj3M4WITl5TPy2UlVHre2zwPgdYwt3XfTrH'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


class TweetModel(object):

    def getFilterTweets(self,hashtag):
        public_tweets = api.search(hashtag)
        i=0
        for tweet in public_tweets:
            a =  tweet.text.encode('utf-8')
            analysis = TextBlob(tweet.text)
            b = analysis.sentiment.polarity
            c = analysis.sentiment.subjectivity

            List.append([a,b,c])
            if( i > 4 ):
                return List
            i+=1
            return List

def main():
    obj = TweetModel()
    print (obj.getFilterTweets("India")[0][0])
    print (obj.getFilterTweets("India")[0][1])
    print (obj.getFilterTweets("India")[0][2])

if __name__ == '__main__':
    main()
