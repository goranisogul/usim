from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen
import json
import xmltodict


url = 'http://apis.data.go.kr/1611000/nsdi/LandUseService/attr/getLandUseAttr'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키',
                                quote_plus('pnu') : '2623010200103620003',
                                })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
jsonString = json.loads(json.dumps(xmltodict.parse(response_body), ensure_ascii=False))
results = jsonString['response']['fields']['field']

for i in range(len(results)) :
    result = results[i]
    print(result)

