from urllib import request

baseUrl = 'http://jzk.flz4.cn:8001/v_play/index.php#2'
# baseUrl = 'http://jzk.flz4.cn:8001/tz/tz.php?action=ios'
with request.urlopen(baseUrl) as mReq:
    data = mReq.read()
    #打印正文
    print(data.decode('utf-8'))