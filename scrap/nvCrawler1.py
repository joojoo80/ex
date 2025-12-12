import os
import sys
import urllib.request
import datetime
import time
import json
client_id = "TUbB6ZX5S1b0i3LO_P0k"
client_secret = "BD5U9UbTAG"

# [code 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response =urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Reqest Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(),url))
        return None
    
# [code 2]

def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters ="?query=%s&start=%s&display=%s"  %(urllib.parse.quote(srcText),start,display)

    url = base + node + parameters

    responseDecode = getRequestUrl(url) #[code 1]

    if(responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)
    
#  [code 3]

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pData =datetime.datetime.strptime(post['pubDate'],'%a, %d %b %Y %H:%M:%S +0900')
    pData =pData.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description ,'org_link':org_link,'link':org_link, 'pData':pData})
    return

# [code 0 ]
def main():
    node ='news' # 크롤링 대상 노드 : 네이버 '뉴스'
    srcText = input('검색어를 입력하세요 : ')
    cnt = 0
    jsonResult =[]

    jsonResponse = getNaverSearch(node, srcText, 1, 100) # [code2]

    total = jsonResponse['total']

    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt) # [code3]

        start = jsonResponse['start'] + jsonResponse['display']
        if start == 1001 : break # 네이버 뉴스는 1000개까지 무료 제공됨
        jsonResponse = getNaverSearch(node, srcText, start, 100) # [code2]
    
    print('전체검색 : %d 건' %total)

    with open('%s_naver_%s.json' % (srcText, node),'w', encoding='utf8') as outfile:
        jsonfile = json.dumps(jsonResult, indent = 4, sort_keys =True, ensure_ascii = False)

        outfile.write(jsonfile)

    print("가져온 데이터 : %d 건" %(cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == '__main__':
    main()
    
