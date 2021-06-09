import requests
import datetime
from bs4 import BeautifulSoup
class Detect_month:
    def __init__(self, t = 1):
        self.t= t
        if self.t==0:
            a=datetime.date.today()+datetime.timedelta(1)
        else:
            a=datetime.date.today()
        a = str(a).split('-')
        if a[1][0] == '0':
            self.tm = a[1][1]
        else:
            self.tm = a[1]
        self.time = f'https://islom.uz/vaqtlar/27/{self.tm}'
        self.headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.full_page = requests.get(self.time, self.headers)
        self.soup = BeautifulSoup(self.full_page.content , 'html.parser')
        self.convert = self.soup.findAll('span' , {'class': 'today_date'})
        self.tex = self.convert[0].text
        self.oy1= self.tex.split('|')
        self.oy1= self.oy1[0].split(' ')[1]
    def oy(self):
        return  self.oy1