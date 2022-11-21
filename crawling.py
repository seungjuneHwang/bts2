import requests
from bs4 import BeautifulSoup

def get_movie():
    ret_list = []
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('tbody')
        titles = ul.select('div.tit3 > a')
        for rank, title in enumerate(titles):
            # print(title)
            # print(f"{rank+1}위 {title.get_text()}")
            ret_list.append((rank+1, title.get_text()))
    else : 
        print(response.status_code)

    return ret_list

def get_music():
    ret_list = []
    url = 'https://www.melon.com/chart/'
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        ul = soup.select_one('tbody')
        titles = ul.select('div.ellipsis.rank01 > span > a')
        for rank, title in enumerate(titles):
            # print(f"{rank+1}위 {title.get_text()}")
            ret_list.append((rank+1, title.get_text()))
        # titles = ul.select('div.ellipsis.rank02 > span > a')
        # for rank, title in enumerate(titles):
        #     # print(title)
        #     print(f"{rank+1}위 {title.get_text()}")
    else : 
        print(response.status_code)
    
    return ret_list