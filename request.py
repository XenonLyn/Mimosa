import requests

url = 'https://graph.mapillary.com/token'
# request header
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth MLY|8448796828551246|961e4f9d9a55b28a8eca88075b2f2788'
    # 对应我们注册application的Client secret
}
# post date to send
data = {
    'grant_type': "authorization_code",
    'client_id': 8448796828551246,
    #client_id
    'code': 'AQDXGC5GKOtTikB4V41kUJnzHnYXqBkSESd8v0hldMB3kXb-Lfms7YhBBWVyQ6E7f3F4dWBeZ_31e_uX58J7Dp09ZvFjrBgabi6zohP3sN5DQnjJhWmXfIDUlunKNS3u0nMpFMKFAnV_un2S41Heuy7kQQdkdYHPmr0go2HDKeBpA1hDRyWnE4PGn4ub4Ggh92iitYOeLwzRiEIcOvYD5Ukfs9WTOg1BG0HS4_FCvXw5IgOuUlzHnyB5boPDcqQC6tNEMzhGUpbgycA_-M7zTmmPF37mDh0JZ-wOIst03mvNdQ'
	#code: after authorized the authorization URL copy the code following the redirect URL
}
# https://www.mapillary.com/app/?code=AQDXGC5GKOtTikB4V41kUJnzHnYXqBkSESd8v0hldMB3kXb-Lfms7YhBBWVyQ6E7f3F4dWBeZ_31e_uX58J7Dp09ZvFjrBgabi6zohP3sN5DQnjJhWmXfIDUlunKNS3u0nMpFMKFAnV_un2S41Heuy7kQQdkdYHPmr0go2HDKeBpA1hDRyWnE4PGn4ub4Ggh92iitYOeLwzRiEIcOvYD5Ukfs9WTOg1BG0HS4_FCvXw5IgOuUlzHnyB5boPDcqQC6tNEMzhGUpbgycA_-M7zTmmPF37mDh0JZ-wOIst03mvNdQ
proxy = {
    'http':'http://127.0.0.1:59527',
    'https':'http://127.0.0.1:59527'
}
r = requests.post(url=url,data=data,headers=headers,proxies=proxy)
print(r.text)
with open('token_info.json','w') as f:
    f.write(r.text)
print('success')
