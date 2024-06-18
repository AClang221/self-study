import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'}
import json
import openpyxl
wk=openpyxl.Workbook()
sheet=wk.create_sheet()
resp = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=8240108&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',headers=headers)
content=resp.text
rest=content.replace('fetchJSON_comment98(','').replace(');','')
json_data=json.loads(rest)
comments=json_data['comments']
for item in comments:
  color = item['productColor']
  size = item['productSize']
  sheet.append([color,size])
  wk.save('E:\python题\wk.xlsx')
