import requests
from requests.auth import HTTPDigestAuth

url = 'http://endereço/'
#Pop up = HTTPDigestAuth, user,password
auth = HTTPDigestAuth('admin','admin')
r = requests.get(url=url, auth=auth)

print(r)
print(r.text)