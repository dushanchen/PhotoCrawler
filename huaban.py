import requests
import json
from pprint import pprint
import time

#花瓣网
url = 'http://huaban.com/all/'#.encode("utf-8").decode("latin1")
params = {
	'fetch':'',	
	'jctounes':'',	
	'since':1495091618,
	'limit':100,
	'wfl':1
}
base_url = 'http://img.hb.aicdn.com/'
headers = {
	'Accept':'application/json',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Connection':'keep-alive',
	'Cookie':'_uab_collina=151683570564919570960402; _ga=GA1.2.355367494.1516409234; UM_distinctid=1611108a3349-0a5d470cb597ec8-49566e-fa000-1611108a3353be; CNZZDATA1256914954=1723688894-1516350514-null%7C1516350514; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAADZklEQVRIic2VXWjVdRjHv8tlp9goODgIRhSESV1ESJclqwhkQi83hjdRMRBqdZMI2ZtlRC%2BQZUKJ0iAHgdiIpCvp95wdhe33%2B882aUTdDAul6RgxWKfp7NPFec7OTlvHDXeaD%2Fz5vzzPj%2F%2FzeV4loO61DEFag3T9cs4sVfZO7qXepYrDTx49ChK79uxhzezs3DvSh0jNS4C4BekM0kOrCrJ2ZoaJfJ7Wqamad6R1VwDIzXvejvTgIjZXnaklg9w0Pc1EPs%2B68%2BcR0Do1NQeCtAXpG6QWv3cj5ZC%2BRnoF6SOkJgf5DekPpGNINyI9gfQp0rdIG5C6kHqQjrhdfsVBxtva%2BGrrVg50ddG7bRulXA6kPNJapFMe2WeQ3kG6Dek1L6mSA7%2Fk%2BiakYaTNSLvcdqefuxdpAqkZ6WOkhxuSkcVKC6kVyRxkuzvU5NHd7SB5pBcrPYL0HNKrSLe7fb%2BD34P0M9J1ntmVBanTI20OcsZBKpHdhNTr3yYceAfSAw7yhtv85JBP%2B7m7HKTJQRb01FWB%2FHtqPd7XV5la%2B5BuQBrw%2Bj%2BI1Id0n%2Bt7kE4jfYD0mGfudaQ3HfKQZ%2BwTv%2B%2F03rgbKUN6eUVBlrJHWMLkcejWpTi3HFlRkNWUawKEkG3Aso7%2F1PdnnYRQd%2Bk2DARLRSxBSCfKzo7lsHQOSxcIA%2B1Vu%2FgWFsexdApLxVrAsRyWfiUkw9IkhezRWv1AOxYLWJr%2B%2FPz%2BBoGEsRwWS4R4fJ7To4T0VNVm6E4sXsKybsJoC5ZmsLRjXjC%2Bw%2BJ42TYerjzP6U%2BOtFGI7xLSXw0D8Z%2F3EOIsxcH1FIc2lqNbLREs68DSRcJAOyE0Y3GKEA9Xz6cMS31uu5sQZzk50lbzj%2BLQRiz%2B2ViQwuAdWLqIxS8I6SAh9tToLb2PxUsMDuYdfLgCUgZL01g6JHmfWCwtALGso%2BEg7txxLJawdJbi4Ppa3dCWuhmxOIqlI%2BWgxLcXzcj%2FBlIun8uEOLxAl2U3l%2Fsi6672VHqBEJoppGex2FvtkfQZls56Jjdj8X5prrRK%2By%2Fsa%2Fz4xeIvhLjohsbSe4Q4gaXTlalFIT2Ppb%2F5Pm7yqXUCS5OE9EgZKv5OSJnD%2F4Clyz%2BOHLsG9kh%2Fdiv9WWcdfSdhtGVRnY%2FyL88dWH2QlZArLcR%2FAGx5IFMItbrvAAAAAElFTkSuQmCC%2CMacIntel.1280.800.24; __asc=9a6e1a9d1612a70a04f6007dc1b; __auc=9a6e1a9d1612a70a04f6007dc1b; _cnzz_CV1256903590=is-logon%7Clogged-out%7C1516835768744; CNZZDATA1256903590=589584137-1516773418-%7C1516773418',
	'Host':'huaban.com',
	'Referer':'http://huaban.com/all/',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
	'X-Request':'JSON',
	'X-Requested-With':'XMLHttpRequest'
}

params['limit'] = 100

result = requests.get(url,headers=headers,params=params,timeout=3)
pins = json.loads(result.text)['pins']
pprint(pins)
count = 0
for pin in pins:
	count = count + 1
	try:
		img_url = pin['file']['key']
		image = requests.get(base_url+img_url)
		name = int(time.time()*1000)
		with open('huaban/huaban'+str(name)+'.png','wb') as file:
			file.write(image.content)
		print(count,":",img_url)
	except Exception as e:
		print(count,':',e.message)


