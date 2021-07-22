from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json
import xmltodict
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
#startDate, endDate, numOfRows
def rentpric(sigunguCd, bjdongCd, platGbCd, bun, ji, pageNo) :
    url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo'
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): 'd/RxZ54Jxd9jN5sYn+/6QRBkcvLKkZwjsic2/wOToKB8ModmLJxSRIIaWePcUOgN3QTGOfijdZ29nc9d3a14oQ==',
     quote_plus('sigunguCd'): sigunguCd,
     quote_plus('bjdongCd'): bjdongCd,
     quote_plus('platGbCd'): platGbCd,
     quote_plus('bun'): bun,
     quote_plus('ji'): ji,
     #quote_plus('startDate'): startDate,
     #quote_plus('endDate'): endDate,
     #quote_plus('numOfRows'): numOfRows,
     quote_plus('pageNo'): pageNo})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

jsonString = json.loads(json.dumps(xmltodict.parse(response_body), ensure_ascii=False))
results = jsonString['response']['body']['items']['item']
return results

#for i in range(len(results)) :
# result=results[i]
# print(result)