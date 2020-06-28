import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

header = {'Cookie':'uuid_n_v=v1; uuid=CC1FD5A0B68711EAACB6BBD781D8993831C7C63DF412413A8944E9E658997CBE; _csrf=a00d595c55dd1995c6f6e99ca8f15606c185bed7fac14e7b3b32284807190676; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593050498; mojo-uuid=7db502457ba09770df914609ea40ebb9; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=172e9358325c8-0f6d2fb401f1b7-31607402-7e9000-172e9358325c8; _lxsdk=CC1FD5A0B68711EAACB6BBD781D8993831C7C63DF412413A8944E9E658997CBE; mojo-session-id={"id":"9fbc717b5ce010980b7b8fbc97afcca8","time":1593161817749}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593161818; __mta=174373405.1593050498009.1593050501310.1593161819402.3; _lxsdk_s=172efd824a0-76f-9e5-82b%7C%7C2',
'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)
# print(response.status_code)
bs_info = bs(response.text, 'html.parser')

movies = []

def parse_text(str):
    return str.strip().split('\n')[-1].strip()

for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    for atags in tags.find_all('div', attrs={'class':'movie-hover-title'}):
        for tag in atags.find_all('span', attrs={'class':'hover-tag'}):
            if tag.text == '类型:':
                category = parse_text(tag.find_parent('div').text)
                title = tag.find_parent('div').get('title')
            if tag.text == '上映时间:':
                time = parse_text(tag.find_parent('div').text)
                movie = [title, category, time]
                movies.append(movie)

df = pd.DataFrame(movies[:10],columns=['title', 'category', 'time'])
df.to_csv('./movie1.csv',encoding='utf8',index=False,header=False)