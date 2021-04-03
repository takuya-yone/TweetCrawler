import tweepy
import json


def main():
    json_open = open('secret.json','r')
    secrets = json.load(json_open)
    # print(secrets.keys())
    print(secrets['APIkey'])
    print(secrets['APIkeysecret'])
    print(secrets['Bearertoken'])

    auth = tweepy.OAuthHandler(secrets['APIkey'],secrets['APIkeysecret'])
    auth.set_access_token(secrets['AccessToken'], secrets['AccessTokenSecret'])
    api= tweepy.API(auth)
    print(api, auth)
    api.update_status("投稿テスト")


if __name__ == '__main__':
    main()

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
#     print('-----------------')
#     print(tweet.text)