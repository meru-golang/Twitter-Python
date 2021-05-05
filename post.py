import json, config
from requests_oauthlib import OAuth1Session

#Twitterの認証
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

#Tweetのエンドポイント
url = "https://api.twitter.com/1.1/statuses/update.json"

#送信する内容の取得
print("Tweetする内容を入力！")
tweet = input('TypeHERE>> ')
print('ツイートを送信します！')

params = {"status" : tweet}

res = twitter.post(url, params = params) #送信

#正常にTweetできればSuccess.
if res.status_code == 200:
    print("Success.")
#正常にTweetできないのであればステータスコードを表示
else:
    print("Failed. : %d"% res.status_code)