import math
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json
import xmltodict
from datetime import datetime, timedelta

url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo'
# 요청메세지 명세
# sigunguCd': '11680', 시군구코드
# 'bjdongCd': '10300' 법정동코드
# 'platGbCd'): '0' 대지구분코드
# 'bun'): '0012' 번
# 'ji'): '0000' 지
# 'startDate' 검색시작일
# 'endDate' 갬색종료일
# 'numOfRows' 리스트수
# 'pageNo' 페이지 번호

queryParams = '?' + urlencode(
    {quote_plus(
        'ServiceKey'): 'd/RxZ54Jxd9jN5sYn+/6QRBkcvLKkZwjsic2/wOToKB8ModmLJxSRIIaWePcUOgN3QTGOfijdZ29nc9d3a14oQ==',
     quote_plus('sigunguCd'): '11680',
     quote_plus('bjdongCd'): '10300',
     quote_plus('platGbCd'): '0',
     quote_plus('bun'): '0012',
     quote_plus('ji'): '0000',
     quote_plus('startDate'): '',
     quote_plus('endDate'): '',
     quote_plus('numOfRows'): '10',
     quote_plus('pageNo'): '1'})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

jsonString = json.loads(json.dumps(xmltodict.parse(response_body), ensure_ascii=False))
results = jsonString['response']['body']['items']['item']

for i in range(len(results)):
    result = results[i]
    res1 = result['useAprDay']
    res2 = result['bldNm']
    if res2==None:
       print("value가 없습니다")
    x_str = str(res1)
    y = int(x_str[0:4])
    m = int(x_str[4:6])
    d = int(x_str[6:8])
    #print(y, m, d)
    #print('사용승인일:'+res1)
    time1 = datetime(y, m, d).date()
    now = datetime.now().date()
    print(str(math.floor((now - time1).days / 370)) + "년입니다."+ str(res2))
