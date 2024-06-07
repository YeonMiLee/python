import os
import sys
import urllib.request
import datetime
import time
import json

client_id = "wRe2UJkwpGyQwMdpG86L"
client_secret = "bLKnFKSFI4"

# [CODE 1] : url 접속을 요청하고 응답을 받아서 반환하는 부분
def getRequestUrl(url):    
    req = urllib.request.Request(url)   # url 요청하기 위해 request 객체로 만들어줌
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)    # API를 사용하기 위한 id/secret 코드를 요청 객체 헤드에 추가
    
    try: 
        response = urllib.request.urlopen(req)      # 요청 객체를 보내고 그에 대한 응답을 받아 response 객체에 저장
        if response.getcode() == 200:                                     # getcode()로 response 객체에 저장된 코드 확인
            print ("[%s] Url Request Success" % datetime.datetime.now())  # 200이면 정상처리 - 성공 메세지 마이썬 셸창에 출력 
            return response.read().decode('utf-8')                        # 응답을 utf-8로 디코딩하여 반환
    except Exception as e:                                                  # ~22까지 - 예외 사항 발생하면 에러메세지 피이썬 셸 창에 출력
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
    
# [CODE 2] : 네이버 뉴스 검색 url을 만들고 [CODE 1]의 
# getRequestUrl(url)을 호출하여 반환받은 응답 데이터를 파이썬 jsom형식으로 반환하는 부분
def getNaverSearch(node, srcText, start, display):    
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)
    
    url = base + node + parameters            # 1~ : 네이버 검색 API 정보에 따라 요청 URL을 구성
    responseDecode = getRequestUrl(url)       # [CODE 1] / 완성한 url을 이용하여 getRequestUrl()함수를 호출하여 받은 utf-8 디코드 응답을 responseDecode에 저장
    
    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)     # 서버에서 받은 json 형태의 응 답 객체를 파이썬 객체로 로드하여 반환


#[CODE 3] : json 형식의 응답 데이터를 필요한 항목만 정리하여 딕셔너리 리스트인 jsonResult를 구성하고 반환하도록
def getPostData(post, jsonResult, cnt):    
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']     # 1~ : 검색 결과가 들어있는 post 객체에서 필요한 데이터 항목을 추출하여 변수에 저장
    
    pDate = datetime.datetime.strptime(post['pubDate'],  
                                       '%a, %d %b %Y %H:%M:%S +0900') # 네이버에서 제공하는 시간인 pubDate는 문자열 형태이므로 날짜 객체로 변환
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')   # 수정된 날짜를 '연-월-일 시:분:초' 형식으로 나타냄
    
    jsonResult.append({'cnt':cnt, 'title':title, 'description': description, 
                        'org_link':org_link,   'link': org_link,   'pDate':pDate})
    # 2~5행에서 저장한 데이터를 딕셔너리 형태인 {'키':값}으로 구성하여 리스트 객체인 jsonResult에 추가
    return    

#[CODE 0]
def main():
    node = 'news'   # 크롤링 할 대상
    srcText = input('검색어를 입력하세요: ')    # 파이썬 셸 창에서 검색어 입력받아 srcText에 저장
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)  #[CODE 2] / 
    # getNaverSearch() 함수 호출하여 start=1, display=100에 대한 검색결과를 반환받아 jsonResponse에 저장
    total = jsonResponse['total']
 
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):         
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)  #[CODE 3]       
        
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)  #[CODE 2]
   # while~ : 검색결과(jsonResponse)에 데이터가 있는 동안 for문으로 검색 결과를 한개씩 처리하는 작업(getPostData())을 반복
   # 반복 작업이 끝나면 다음 검색 결과 100개를 가져오기 위해 start 위치를 변경하고, getNaverSearch()함수를 호출하여 새로운 검색 결과를
   # jsonResponse에 저장하고 for문을 다시 반복

    print('전체 검색 : %d 건' %total)
    
    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult,  indent=4, sort_keys=True,  ensure_ascii=False)
                        
        outfile.write(jsonFile)
  # with~ : 파일 객체를 생성하여 정리된 데이터를 json파일에 저장
        
    print("가져온 데이터 : %d 건" %(cnt))
    print ('%s_naver_%s.json SAVED' % (srcText, node))
    
if __name__ == '__main__':        # 소스파일(nvCrawler.py)이 임포트되지 않고 독립적으로 실행할 경우에는 main() 
    main()                        # 즉 CODE 0 을 호출하여 시작하라는 의미
