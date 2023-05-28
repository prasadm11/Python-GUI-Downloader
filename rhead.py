import requests
a=requests.get("https://youtube.com")

print(a.headers.get("Content-Length"))