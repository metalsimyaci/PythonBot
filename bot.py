from bs4 import BeautifulSoup
#import urllib.request
from urllib.request import urlopen
import re


def GetUrls():
    sitemap_path = "http://mabushimajo.com/sitemap.xml"
    url_oku = urlopen(sitemap_path)
    soup = BeautifulSoup(url_oku, "html.parser")
    locs = []
    for loc in soup.find_all('loc'):
        loc_content = loc.contents[0]
        # print(loc_content)
        # print('/onlineokuma/' not in loc_content)
        if '/onlineokuma/' not in loc_content:
            if locs.count(loc_content) <= 0:
                locs.append(loc_content)
    print(locs)
    print("Adet Link bulundu:{0}".format(len(locs)))
    return locs


def not_mabushimajo(href):
    return not (not href or re.compile("http://mabushimajo").search(href) or re.compile("#").search(href) or re.compile(
        "http://inkhive.com/").search(href) or re.compile("mailto:schatzm_1903@hotmail.com").search(href) or re.compile(
        "https://www.facebook.com/MabushiMajo").search(href) or re.compile(
        "http://igemooneobi.blogspot.com.tr/").search(href) or re.compile(
        "http://soguk-nevale.blogspot.com.tr/").search(href) or re.compile("page/").search(href) or re.compile(
        "http://mabushi%20majo").search(href) or re.compile("https://www.youtube.com").search(href) or re.compile(
        "https://www.reddit.com").search(href) or re.compile("http://uptobox.com").search(href) or re.compile(
        "blogspot.com").search(href) or re.compile(
        "http://www.mediafire.com").search(href) or re.compile("http://www.mangapanda.com").search(href) or re.compile(
        "http://Mabushimajo").search(href) or re.compile(
        "https://youtu.be").search(href) or re.compile("http://yok").search(href) or re.compile(
        "http://www.webtoons.com").search(href) or re.compile(
        "https://www.dropbox.com").search(href))


def searcher(furl):
    f = open('kayitlar.txt', 'a')
    url_oku = urlopen(furl)
    soup = BeautifulSoup(url_oku, 'html.parser')
    searc_result = soup.find_all('a', href=not_mabushimajo)
    f.write('Taranan Sayfa:' + furl + '\n')
    if len(searc_result) > 0:
        for result in searc_result:
            print(result)
            f.write(str(result))
            f.write('\n')
    # print(searc_result)
    f.close()


urls = GetUrls()
for index, url in enumerate(urls):
    print("""Çalıştırılan {0}/{1}""".format(index + 1, len(urls)))
    searcher(url)
