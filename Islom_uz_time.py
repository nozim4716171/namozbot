import requests
from bs4 import BeautifulSoup
import datetime
from Detect_month import Detect_month

class region_time:
    def __init__(self , region_id = 27):
        self.mont = Detect_month(t=1)
        self.region_id = region_id
        a = str(datetime.date.today()).split('-')
        if a[1][0]=='0':
            self.tm = a[1][1]
        else:
            self.tm= a[1]
        try:
            self.time = 'https://islom.uz/vaqtlar/{}/{}'.format(self.region_id,self.tm)
            self.headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
            self.full_page = requests.get(self.time, self.headers)
            self.soup = BeautifulSoup(self.full_page.content , 'html.parser')
            if datetime.date.today().weekday() == 4:
                self.convert = self.soup.findAll('tr' , {'class': 'juma bugun'})
            else:
                self.convert = self.soup.findAll('tr', {'class': 'p_day bugun'})
            self.tex = self.convert[0].text
            self.a = self.tex.split('\n')
        except:
            pass
    def month(self):
            return  f'{self.mont.oy()} ойининнг {self.a[1]}-куни'

    def hafta_kuni(self):
        return self.a[3]
    def tong(self):
        return self.a[4]
    def quyosh(self):
        return self.a[5]
    def peshin(self):
        return self.a[6]
    def shom(self):
        return self.a[8]
    def asr(self):
        return self.a[7]
    def xufton(self):
        return self.a[9]
class region_time_tomorrow:
    def __init__(self, region_id):
        self.mon = Detect_month(t=0)
        self.region_id = region_id
        self.con = region_time(self.region_id)
        a = str(datetime.date.today()+datetime.timedelta(1)).split('-')
        if a[1][0]=='0':
            self.tm = a[1][1]
        else:
            self.tm= a[1]
        self.time = 'https://islom.uz/vaqtlar/{}/{}'.format(self.region_id, self.tm)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.full_page = requests.get(self.time, self.headers)
        self.soup = BeautifulSoup(self.full_page.content, 'html.parser')
        self.con = region_time(self.region_id)
        if self.con.hafta_kuni() == 'Пайшанба':
            self.convert = self.soup.findAll('tr', {'class': 'juma erta'})
        else:
            self.convert = self.soup.findAll('tr', {'class': 'p_day erta'})
        self.tex = self.convert[0].text
        self.a = self.tex.split('\n')
    def month(self):
            return  f'{self.mon.oy()} ойининнг {self.a[1]}-куни'

    def hafta_kuni(self):
        return self.a[3]

    def tong(self):
        return self.a[4]

    def quyosh(self):
        return self.a[5]

    def peshin(self):
        return self.a[6]

    def shom(self):
        return self.a[8]

    def asr(self):
        return self.a[7]

    def xufton(self):
        return self.a[9]


