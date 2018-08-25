from urllib import request
from urllib.parse import urljoin
import ssl

baseUrl = "https://movie.xjbtdwsgh.org:890/index.html"
# baseUrl = "https://m.zzhtxxjc.com:890/index.html?c=50022"

webHeader = {
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'DNT': '1',
    'Connection': 'Keep-Alive'
}

context = ssl._create_unverified_context()
req = request.Request(url = baseUrl, headers = webHeader)
webPage = request.urlopen(req, context = context)
data = webPage.read().decode('utf-8')
jsonUrl = urljoin(baseUrl, "/json/8.json")
print(data)
#获取目标json完整地址
print(jsonUrl)
