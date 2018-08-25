import requests
import time

#存储路径
path = '/Users/steward/Desktop/a.mp4'
downloadUrl = 'http://cdn.fqfengxun.com:36150/html5/xin/vip4/43.mp4'
startTime = time.time()
resp = requests.get(downloadUrl)
target = resp.content
f = open(path, 'wb')
f.write(target)
f.close()
endTime = time.time()
print('下载完成，共耗时' + str(endTime - startTime) + 's')