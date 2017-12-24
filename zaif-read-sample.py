#
import json
import hmac
import hashlib
import requests
# from future.moves.urllib.parse import urlencode
import urllib
#
# read latest nonce number and overwrite new incremented number 
filenonce = open('nonce.txt','r')
nonce = filenonce.read()
filenonce.close()
# print (nonce)
intnonce = int(nonce)
intnewnonce = intnonce + 1
newnonce = str(intnewnonce)
filenewnonce = open('nonce.txt','w')
filenewnonce.write(newnonce)
filenewnonce.close()
#
#
response = requests.get('https://api.zaif.jp/api/1/last_price/btc_jpy')
if response.status_code != 200:
    raise Exception('return status code is {}'.format(response.status_code))
print (json.loads(response.text))
#
secret = 'write your secret code here'
key = 'write your key here'
#
params = {
     'method': 'get_info',
#    'method': 'actiuve_orders',
     'nonce': intnonce
#    'currency_pairs': 'btc_jpy'
}
encoded_params = urllib.urlencode(params)
signature = hmac.new(bytearray(secret.encode('utf-8')), digestmod=hashlib.sha512)
signature.update(encoded_params.encode('utf-8'))
headers = {
    'key': key,
    'sign': signature.hexdigest()
}
response2 = requests.post('https://api.zaif.jp/tapi', data=encoded_params, headers=headers)
if response2.status_code != 200:
    raise Exception('return status code is {}'.format(response2.status_code))
print(json.loads(response2.text))
