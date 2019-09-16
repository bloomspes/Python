import urllib.request
import urllib.parse

url="http://stkp-api.kisti.re.kr/dictionary/1.0/authority"
req=urllib.request.Request(url)
res=urllib.request.urlopen(req)