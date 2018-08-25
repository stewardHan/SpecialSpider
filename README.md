# python爬虫针对灰色网站的花式应用
###背景介绍
######不知从何时开始，我们常浏览的一些新闻和社交网页上偶尔会出现一些灰色网站的入口，入口图片和网站内容低俗、色情、暴力，并且会诱导用户充值，对牢记并实践社会主义核心价值观的我们产生了很坏的影响。Python爬虫在分析网页代码结构和获取网络资源方面有着独特的优势。
######今天，我们就从代码的层面实例分析这些灰色网站的架构细节和其中蕴含的骗术。
###实例分析
######今天海贼王中文网更新了最新的915话，在iPhone safari浏览器的漫画末尾处有一处灰色网站入口，点击进入后从浏览器顶部可以获取到http://jzk.flz4.cn:8001/v_play/index.php#2这个地址。于是将这个地址复制到pc的chrome浏览器中，发现改地址重定向到百度首页。
- ######用如下代码去爬取改地址信息
```
from urllib import request

baseUrl = 'http://jzk.flz4.cn:8001/v_play/index.php#2'
with request.urlopen(baseUrl) as mReq:
    data = mReq.read()
    #打印正文
    print(data.decode('utf-8'))
```
######打印出的数据为
```
<script>
if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
    window.location.href="/tz/tz.php?action=ios";
} else if (/(Android)/i.test(navigator.userAgent)) {
    window.location.href="/tz/tz.php?action=az";
} else {
    window.location.href="/tz/tz.php?action=ios";
};
</script>
```
- ######发现初始地址会根据不同的浏览平台重定向到不同的地址，我们选取[http://jzk.flz4.cn:8001/tz/tz.php?action=ios](http://jzk.flz4.cn:8001/tz/tz.php?action=ios)这个地址继续爬取
######修改baseUrl
```
baseUrl = 'http://jzk.flz4.cn:8001/tz/tz.php?action=ios'
```
######爬取到内容为
```
<script>
    if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
        window.location.href="https://m.zzhtxxjc.com:890/index.html?c=50022";
    } else if (/(Android)/i.test(navigator.userAgent)) {
        window.location.href="https://m.zzhtxxjc.com:890/index.html?c=50022";
        //window.location.href="https://panda.wedicfashion.net:890/50022/index.html";
    } else {
        window.location.href="https://m.zzhtxxjc.com:890/index.html?c=50022";
    };
</script>
```
- ######我们可以发现，又是一次重定向，不过判断语句的各个流程都是相同的链接。
######我们再次修改baseUrl
```
baseUrl = 'https://m.zzhtxxjc.com:890/index.html?c=50022'
```
######需要注意的是，我们这次要爬取的链接是https协议，需要自建ssl证书，所以这次我们的代码需要稍微修改如下
```
from urllib import request
import ssl

baseUrl = "https://m.zzhtxxjc.com:890/index.html?c=50022"
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
print(data)
```
######爬取到的内容为
```
<html>
<head>
<meta charset="utf-8">
<title>百度一下</title>

<meta name="referrer" content="never" >
<meta name="referrer" content="no-referrer">
<meta name="referrer" content="never">
<script type="text/javascript">  
var d='https://movie.xjbtdwsgh.org:890/index.html';
try
{
	if (history.replaceState){
		history.replaceState(null, null, 'baidu.html'+location.search);
	}
}
catch(err)
{
} 
window.location.replace(d+location.search)
</script>
</head>
<body>
正在打开...
</body>
</html>
```
- ######这个老兄又饶了一圈，不过我们也终于获取到了最后一个地址https://movie.xjbtdwsgh.org:890/index.html，我们继续修改baseUrl
```
baseUrl = "https://movie.xjbtdwsgh.org:890/index.html"
```
######爬取到的内容为
```
<!DOCTYPE html>
<html>
<head>

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>激情影院</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
    <meta name="format-detection" content="telephone=no">
	<link href="/css/frozen.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/css/css.css" media="all">
    <link rel="stylesheet" href="/ico/iconfont.css">
</head>

<body>
<div id="123"></div>
<div id="yanse"></div>
<div id="toubu" class="ui-toubu ui-toubu-positive ui-toubu-b" style="height:45px;background-image: none;">
<ul style="width:33%; float:left"><img style="display: block;float: left;height: 1.2em;margin-top: .9em;" src="https://img3.lywanbaofeng.com:1000/html5/css/logo3.png"></ul>
<ul class="toubuyonghu"></ul>
<li style=" float:right" data-href="/tab6.html" class=""><span class="icon iconfont icon-wode" style="font-size:27px;color: #fff;margin-top: .3em;"></span></li>
</div>
	<header id="header" class="ui-header ui-header-positive ui-border-b" style="height:50px;background-image: none;">
		<ul class="ui-tiled ui-border-t" style="height:49px;background-image: none;border:none;">
            <li data-href="/index.html" id="lanm1" class="active"></li>
            <li data-href="/tab2.html" id="lanm2" class=""></li>
            <li data-href="/tab3.html" class=""><span class="icon iconfont icon-pindao- icoyanse"></span><p class="hmwz">频道</p></li>
            <li data-href="/tab4.html" class=""><span class="icon iconfont icon-luntan2 icoyanse"></span><p class="hmwz">论坛</p></li>
            <li data-href="/tab5.html" class=""><span class="icon iconfont icon-zhibo icoyanse"></span><p class="hmwz">直播</p></li>
        </ul>
    </header>
<section class="ui-slider">
    <ul class="ui-slider-content" style="width: 400%;">
        <li class="current"><span class="toplayb" title="同情我变单亲爸巨乳邻人妻诱惑我给干到中出！" mp4="html5/xin/hdp/h51.mp4" pic="html5/xin/hdp/1xq.jpg" style="background-image: url('https://img3.lywanbaofeng.com:1000/html5/xin/hdp/h51.jpg');"><em>同情我变单亲爸巨乳邻人妻诱惑我给干到中出！</em></span></li>
        <li class=""><span class="toplayb" title="真实搭讪内射 爆乳女店员下海拍片！ 友利七叶"  mp4="html5/xin/hdp/h52.mp4" pic="html5/xin/hdp/2xq.jpg" style="background-image: url('https://img3.lywanbaofeng.com:1000/html5/xin/hdp/h52.jpg');"><em>真实搭讪内射 爆乳女店员下海拍片！ 友利七叶</em></span></li>
        <li class=""><span class="toplayb" title="想要零用钱妹妹帮素股！结果爽到自行插入肏到爽！"  mp4="html5/xin/hdp/h53.mp4" pic="html5/xin/hdp/3xq.jpg" style="background-image: url('https://img3.lywanbaofeng.com:1000/html5/xin/hdp/h53.jpg');"><em>想要零用钱妹妹帮素股！结果爽到自行插入肏到爽！</em></span></li>
</ul>

</section>

	<section class="ui-panel">
        <ul class="kg"></ul>
        <ul class="ui-grid-trisect hb" id="vlist">
            <li v-cloak v-for="item in data" v-on:click="play(item.title,item.video,item.pic)">
                <div class="ui-grid-trisect-img">
					<span><img v-bind:src="picurl+item.img"></span>
                </div>
                <h4 class="ui-nowrap">{{item.title}}</h4>
                <!-- <p class="ui-nowrap ui-txt-info">...</p>-->
                <span class="cnl-tag">{{item.tag}}</span><span class="cnl-tag tag">{{item.qxd}}</span>
            </li>
        </ul>
    </section>
	
    <div style="text-align: center; font-size: 16px;" class="topay paytip" onClick="pay()">更多精华资源，仅限会员专享。。。</div>

   
    <!-- 充值提醒 -->
    <div style="display: none;" class="ui-newstips-wrap flip-top">
        <div class="ui-newstips"><i class="ui-icon-checked-s"></i>
            <div>第<span id="showno">58464</span>位会员充值成功！</div>
        </div>
    </div>
	
	<script>
    var param = "";
    var ispay = false;
    var showjs = "1";
    var pop = false;
    var APP = "";
    var sbnum = "100";
    var canplay = true;
    </script>
    <script src="/js/jquery.min.js"></script>
    <script>jQuery.noConflict()</script>
	<script src="/js/zepto.min.js"></script>
	<script src="/js/frozen.js"></script>
    <script src="/js/vue.min.js"></script>
    <script src="/js/ui.js"></script>
    <script src="/js/pay.js"></script>
    <script src="/js/layer/layer.js"></script>
	<script>
        if (gc('vip') == 0 || gc('vip') == null) cid = 0;
        if (gc('vip') == 1) cid = 1;
        if (gc('vip') == 2) cid = 2;
        if (gc('vip') == 3) cid = 3;
        if (gc('vip') == 4) cid = 4;
        if (gc('vip') == 5) cid = 5;
        if (gc('vip') == 6) cid = 6;
		if (gc('vip') == 7) cid = 7;
		if (gc('vip') == 8) cid = 8;
	if (showjs) {
    //var dataurl = APP+"/Index/jsonIndex/i/" + cid;
	var dataurl = "/json/" + cid + ".json";
    var vlist = new Vue({
        el: "body", data: {slider: [], data: []}, methods: {
            play: function (o, t, p) {
                play(o, t, p);
				
            }
        }, ready: function () {
            var o = this;
            $.ajax({
                type: "get",
                cache: true,
                async: true,
                url: dataurl,
                dataType: "jsonp",
                jsonpCallback: 'jsonp',
                success: function (json) {
					var t = json[0];
                    o.picurl = t.picurl || '';
                    o.data = t.data;
                    o.slider = t.slider;
                }
            });
        }
    });
    !function () {
        new fz.Scroll(".ui-slider", {role: "slider", indicator: !0, autoplay: !0, interval: 3e3})
    }()
}

    </script>
    <script>
		var qudaoid=gq("c");
		if(qudaoid){
			sc("qudaoid",qudaoid,"d30");
			sc("CID",qudaoid,"d30");
		}
		else{
			qudaoid=gc("qudaoid")||10000;
		}
		CID=gc("qudaoid")||0;
    </script>	

	<script type="text/javascript" src="//js.users.51.la/19524465.js"></script>
	
	<script src="/js/p2.js"></script>
</body>

</html>
```
- ######对上一步获取到的html稍加分析，我们注意到有这样的一段JavaScript代码
```
<script>
        if (gc('vip') == 0 || gc('vip') == null) cid = 0;
        if (gc('vip') == 1) cid = 1;
        if (gc('vip') == 2) cid = 2;
        if (gc('vip') == 3) cid = 3;
        if (gc('vip') == 4) cid = 4;
        if (gc('vip') == 5) cid = 5;
        if (gc('vip') == 6) cid = 6;
		if (gc('vip') == 7) cid = 7;
		if (gc('vip') == 8) cid = 8;
	if (showjs) {
    //var dataurl = APP+"/Index/jsonIndex/i/" + cid;
	var dataurl = "/json/" + cid + ".json";
    var vlist = new Vue({
        el: "body", data: {slider: [], data: []}, methods: {
            play: function (o, t, p) {
                play(o, t, p);
				
            }
        }, ready: function () {
            var o = this;
            $.ajax({
                type: "get",
                cache: true,
                async: true,
                url: dataurl,
                dataType: "jsonp",
                jsonpCallback: 'jsonp',
                success: function (json) {
					var t = json[0];
                    o.picurl = t.picurl || '';
                    o.data = t.data;
                    o.slider = t.slider;
                }
            });
        }
    });
    !function () {
        new fz.Scroll(".ui-slider", {role: "slider", indicator: !0, autoplay: !0, interval: 3e3})
    }()
}
</script>
```
######我们不去讨论代码对逻辑的实现合理与否，但通过阅读，可以大致得知，该网站将用户分为从0到8不同的vip级别，而不同的级别看到的视频是不同的
- ######下面我们重点关注不同类型的用户获取到的视频类型
```
   var dataurl = "/json/" + cid + ".json";
```
######毫不客气地说，这句代码暴露了一切，我们爬取vip界别8能浏览的内容
```
from urllib.parse import urljoin

jsonUrl = urljoin(baseUrl, "/json/8.json")
print(data)
```
######爬取到的内容为https://movie.xjbtdwsgh.org:890/json/8.json
- ######You can get everything you want in this target json!
- ######为了方便大家进一步了解爬虫的功能，我们最后讨论下如何用爬虫爬取视频文件
```
import requests
import time
downloadUrl = 'http://cdn.fqfengxun.com:36150/html5/xin/vip4/43.mp4'
startTime = time.time()
resp = requests.get(downloadUrl)
target = resp.content
path = '/Users/steward/Desktop/a.mp4'
f = open(path, 'wb')
f.write(target)
f.close()
endTime = time.time()
print('下载完成，共耗时' + str(endTime - startTime) + 's')
```
###结语
######知己知彼，百战不殆。打倒敌人，从了解敌人开始！
######本文源码托管在https://github.com/stewardHan/SpecialSpider.git，如觉不妥，请不吝赐教。




