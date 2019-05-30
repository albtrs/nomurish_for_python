import requests
import lxml.html
import json
url = 'https://racing-lagoon.info/nomu/translate.php'
xpathToekn = '//input[@name="token"]';
xpathAfter = '//textarea[@name="after1"]';

def translate(text, level):
  # 準備
  session = requests.session() # クッキーを許可しないとCSRFで弾かれる
  res = session.get(url)

  # POST処理
  html = lxml.html.fromstring(res.content)
  token = html.xpath(xpathToekn)[0].get("value")
  payload = setPayload(text, level, token)
  res = session.post(url, data=payload)

  # 翻訳結果
  html = lxml.html.fromstring(res.content)
  result = html.xpath(xpathAfter)[0].text
  
  return result

def setPayload(text, level, token):
  params = {
    "options": "nochk",
    "transbtn": "翻訳",
    "before": text,
    "level": getLevel(level),
    "token": token
  }
  return params

def getLevel(level):
  if (0 < level and 6 > level):
    return level
  else:
    return 2