import tweepy
import json
from icecream import ic
from datetime import datetime

def apiobj():
    json_open = open('secret.json','r')
    secrets = json.load(json_open)
    # ic(secrets.keys())
    # ic(secrets['APIkey'])
    # ic(secrets['APIkeysecret'])
    # ic(secrets['Bearertoken'])

    auth = tweepy.OAuthHandler(secrets['APIkey'],secrets['APIkeysecret'])
    auth.set_access_token(secrets['AccessToken'], secrets['AccessTokenSecret'])
    api= tweepy.API(auth)
    return api


def post_tweet(api:tweepy.API):
    ic(api)
    api.update_status('tweet from python ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def get_tweet(abi:tweepy.API):
    account = 'Satoru_191'
    tweets = api.user_timeline(account,count=10,page=1)
    for tweet in tweets:
        ic(tweet.id)
        ic(tweet.user.name)
        ic(tweet.created_at)
        ic(tweet.text)

if __name__ == '__main__':
    # main()
    api = apiobj()
    # post_tweet(api)
    get_tweet(api)

# # 認証に必要なキーとトークン
# API_KEY = 'your_api_key'
# API_SECRET = 'your_api_secret'
# ACCESS_TOKEN = 'your_access_token'
# ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# # APIの認証
# auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # キーワードからツイートを取得
# api = tweepy.API(auth)
# tweets = api.search(q=['Python'], count=10)

# for tweet in tweets:
#     ic('-----------------')
#     ic(tweet.text)