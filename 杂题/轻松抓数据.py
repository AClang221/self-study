import requests
# import用于引入工具包,requests 库是一个常用的用于 http 请求的模块，它使用 python 语言编写，可以方便的对网页进行爬取
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'}
#headers用于伪装，将python对服务器的访问伪装成，浏览器对服务器的访问
import json
resp = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=8240108&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',headers=headers)
content = resp.text
rest = content.replace('fetchJSON_comment98(', '').replace(');', '')
json_data = json.loads(rest)
# json.loads用于将网页代码转换成python可以翻译的东西
comments = json_data['comments']
# json_data指的是将网页的内容给json这个工具包
for item in comments:
  color = item['productColor']
  size = item['productSize']
  print(color)
  print(size)