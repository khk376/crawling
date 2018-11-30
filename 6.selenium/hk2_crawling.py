

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from tkinter import *
from tkinter.filedialog import *
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import random
#from selenium.webdriver.common.keys import Keys

def Get_mok():
    data = []
    s1 = driver.page_source
    s2 = BeautifulSoup(s1, "html.parser")
    s3 = s2.find("div", id = "tabs_3")
    s3 = s3.text
    print(s3)
    driver.back()

def FilePath():
    global path1
    path1 = askopenfilename()
    print(path1)

def runDriver(url):
    global driver
    driver = webdriver.Chrome(path1)
    #driver = webdriver.PhantomJS(path1)
    driver.get(url)
    
def Rolling(aa):
    driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/li[' +aa+ ']/div/span/img').click()
    time.sleep(2)

def Pager(bb):
    driver.get('http://www.hanbit.co.kr/store/books/new_book_list.html?page='+bb+'&brand=&cate1=&cate2=&searchKey=&keyWord=')
    time.sleep(2)


FilePath()
runDriver('http://www.hanbit.co.kr/store/books/new_book_list.html')

for pages in range(1, 10000):
    print("======================")
    print(pages)
    print("======================")
    for roller in range(1, 21):
        roller = str(roller)
        Rolling(roller)
        Get_mok()
    pages = pages + 1
    pages = str(pages)    
    Pager(pages)