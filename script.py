import urllib3
import json
import requests
http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
i = '191035761407437' # Album ID
at = '' # Access Token
print("YOU NEED AN ACCESS TOKEN FROM FACEBOOK FIRST, SO GET THAT AND PASTE HERE: ")
at = input()
s = 'https://graph.facebook.com/v2.10/'+i+'?fields=photos.limit(500){images}&access_token=' + at
r = http.request('GET', s)
r = r.data.decode('utf8')
k = json.loads(r)
kx = k["photos"]["data"]
ls = []
iii = 0
for p in kx:
	p = p["images"]
	lr = 0
	for ss in p:
		if ss["height"] > lr:
			lr = ss["height"]
			lsd = ss["source"]
	rxx = requests.get(lsd)
	iii += 1
	open('images/'+str(iii)+'.png', 'wb').write(rxx.content)
kx = k["photos"]["paging"]
if "next" in kx:
	s = kx["next"]
	while(True):
		r = http.request('GET', s)
		r = r.data.decode('utf8')
		k = json.loads(r)
		kx = k["data"]
		for p in kx:
			p = p["images"]
			lr = 0
			for ss in p:
				if ss["height"] > lr:
					lr = ss["height"]
					lsd = ss["source"]
			rxx = requests.get(lsd)
			iii += 1
			open('images/'+str(iii)+'.png', 'wb').write(rxx.content)
		kx = k["paging"]
		if "next" in kx:
			s = kx["next"]
		else:
			break
print("DONE! NOW BE HAPPY :)")