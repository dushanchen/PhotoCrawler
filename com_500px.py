#-*- coding:utf-8 -*-
import requests
from pprint import pprint
from pyquery import PyQuery as pq 
import json


headers = {
	'Host': 'api.500px.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://500px.com/search',
	'X-CSRF-Token': 'Y0X+0H0xYytge2bMxzakSkabwrvbJBt5JhqMJfqTScaC29/ltha1Hp7GVZuMxXP4kz1KX7rEiGpOUUMTYus+aA==',
	'Origin': 'https://500px.com',
	'Cookie': '_hpx1=BAh7C0kiD3Nlc3Npb25faWQGOgZFVEkiJWJjZDkyNTUwYzhmMGJjZTk0MDMyYTc0ODFjZDQxNjBiBjsAVEkiCWhvc3QGOwBGIg41MDBweC5jb21JIhl1c2Vfb25ib2FyZGluZ19tb2RhbAY7AEZUSSIYc3VwZXJfc2VjcmV0X3BpeDNscwY7AEZGSSIQX2NzcmZfdG9rZW4GOwBGSSIxNFo0aE5jc24xalgrdlROWFMvUFhzdFdtaU9SaDRKTVRhRXZQTnBoNGQ2ND0GOwBGSSIRcHJldmlvdXNfdXJsBjsARkkiDC9zZWFyY2gGOwBU--b25a05446d814fb2d5482186f15e186b1396920a; optimizelyEndUserId=oeu1516733755983r0.3503923862879882; optimizelySegments=%7B%22569090246%22%3A%22false%22%2C%22569491641%22%3A%22campaign%22%2C%22575800731%22%3A%22ff%22%2C%22589900200%22%3A%22true%22%7D; optimizelyBuckets=%7B%7D; amplitude_id500px.com=eyJkZXZpY2VJZCI6IjhjYTNkNzhhLTFhNTgtNDk0ZC04NTcyLWY4YWJiOTJmNThlOFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUxNjgyMjA3NDY0NywibGFzdEV2ZW50VGltZSI6MTUxNjgyMjk5Njk3NywiZXZlbnRJZCI6MTUsImlkZW50aWZ5SWQiOjEsInNlcXVlbmNlTnVtYmVyIjoxNn0=; _ga=GA1.2.1396237797.1516733758; _gid=GA1.2.1671399216.1516733758; __hstc=133410001.451757ed58cafebe61d27b3d486ad019.1516733926809.1516817990066.1516822482306.7; __hssrc=1; hubspotutk=451757ed58cafebe61d27b3d486ad019; device_uuid=b9e9cac1-8d49-40ad-a8a4-6c4e9c0ed898; __gads=ID=7c4abf250481d37e:T=1516689551:S=ALNI_MZE22eF_p9lQKSKxI4cEaGWjtSuSA; _uetsid=_ueta04f95ea; __hssc=133410001.1.1516822482306; optimizelyPendingLogEvents=%5B%22n%3Doptly_activate%26u%3Doeu1516733755983r0.3503923862879882%26wxhr%3Dtrue%26time%3D1516822996.932%26f%3D10086591487%2C9502403088%2C8746762262%2C9737453591%2C9729990917%2C9502690399%2C8478672984%2C9661320798%2C9738180735%2C9503661200%2C9732794009%2C8179770025%2C8781643456%2C10090402082%2C9510832862%2C9494972573%2C8478040821%2C8560956350%2C10145410331%2C8484780344%2C9660800875%2C9518490284%2C10034978693%2C10053048254%2C8740624971%2C9510101479%26g%3D%22%2C%22n%3Dhttps%253A%252F%252F500px.com%252Fsearch%26u%3Doeu1516733755983r0.3503923862879882%26wxhr%3Dtrue%26time%3D1516822996.851%26f%3D10086591487%2C9502403088%2C8746762262%2C9737453591%2C9729990917%2C9502690399%2C8478672984%2C9661320798%2C9738180735%2C9503661200%2C9732794009%2C8179770025%2C8781643456%2C10090402082%2C9510832862%2C9494972573%2C8478040821%2C8560956350%2C10145410331%2C8484780344%2C9660800875%2C9518490284%2C10034978693%2C10053048254%2C8740624971%2C9510101479%26g%3D582890389%22%5D',
	'Connection': 'keep-alive',
	'X-CSRF-Token': 'dAPOPtjahgA7F6furQ6w56nQI/h5SyEJ8rO75Xda3DGVne8LE/1QNcWqlLnm/WdVfHarHBirshqa+HTT7yKrnw==',
	}

params = {
	'term':'muscle',
	'rpp':1
}
#《《《《《《《《《  start  》》》》》》》》》
#运行前先清空／500px.com 目录下的图片文件，不然之前的文件可能会被覆盖，修改term也可以没事
params['term'] = term = 'muscle'   #搜索图片关键字，
params['rpp'] = count = 150        #爬取总数
quality = 6                        #图片质量 1-10 ，值越大图片像素越高



url = "https://api.500px.com/v1/photos/search?type=photos&image_size[]=1&image_size[]=2&image_size[]=32&image_size[]=31&image_size[]=33&image_size[]=34&image_size[]=35&image_size[]=36&image_size[]=2048&image_size[]=4&image_size[]=14&include_states=true&formats=jpeg,lytro&include_tags=true&exclude_nude=true&page=1"
results = requests.get(url,headers=headers,params=params,timeout=3)
pprint(results)
imgs = json.loads(results.text)['photos']

for img in imgs:
    try:
	    url = img['image_url'][quality]
	    print(count,":",url)
	    stream = requests.get(url)
	    with open('500px.com/'+term+'_'+str(count)+'.png','wb') as file:
	    	file.write(stream.content)
	    count = count - 1
    except Exception as e:
	    print(count,':error:',e.message)
	


