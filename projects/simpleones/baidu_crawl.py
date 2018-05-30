import requests
import webbrowser

param = {'wd' : '阿里巴巴'}

r = requests.get('http://www.baidu.com/s', params=param)

print(r.url)

webbrowser.open(r.url)

