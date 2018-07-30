import requests
from bs4 import BeautifulSoup

filename = 'work.txt'

def getContentInfo(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    for card in soup.select('.post-card'):
        title = card.select('.nickname')[0]['title']
        if title == '心理咨询师':
            i = 0
            print(' #answer#\n ')
            with open(filename,'a',encoding = 'utf-8') as f:
                f.write(' #answer#\n ')
            while len(card.select('.content p')[i].attrs) == 0:
                content = card.select('.content p')[i].text + '\n'
                print(content)
                with open(filename,'a',encoding = 'utf-8') as f:
                    f.write(content)
                i += 1
        else:
            continue

def getNewsInfo(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.text,'html.parser')
    for list in soup.select('.list-item'):
        title = ' #title# ' + list.select('.title')[0].text.replace('&nbsp;','') + '\n'
        link = list.select('.link')[0]['href']
        newslink = '/'.join(url.split('/')[:-1]) + '/' + link
        with open(filename,'a',encoding = 'utf-8') as f:
            f.write(title)
        print(title)
        getContentInfo(newslink)

def getInfo(url):
    print('\n---------------page1--------------\n\n')
    with open(filename,'a',encoding = 'utf-8') as f:
        f.write('\n---------------page1--------------\n\n')
    getNewsInfo('https://bbs.pku.edu.cn/v2/thread.php?bid=690&mode=topic')
    for i in range(2,10):
        num = str(i)
        page = '\n--------------' + num + '---------------\n\n'
        print(page)
        with open(filename,'a',encoding = 'utf-8') as f:
            f.write(page)
        getNewsInfo(url.format(i))

getInfo('https://bbs.pku.edu.cn/v2/thread.php?bid=690&mode=topic&page={}')