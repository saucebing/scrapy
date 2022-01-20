#!/usr/bin/python3
import requests
import time
import random
from lxml import html
from selenium.webdriver import Firefox
from selenium import webdriver
driver = webdriver.Firefox()

                                                #OSDI                           SOSP                                                #ASPLOS
key_words = ['usenix atc', 'eurosys', 'ACM Symposium on Operating Systems', 'Symposium on Operating systems principles', 'International Conference on Architectural Support for Programming Languages and Operating Systems', 'International Symposium on Computer Architecture', "Conference on File and Storage Technologies", "International Conference on Measurement and Modeling of Computer Systems", "International Conference for High Performance Computing, Networking, Storage, and Analysis", "ACM SIGPLAN Symposium on Principles & Practice of Parallel Programming", "Design Automation Conference", "ACM SIGPLAN Conference on Programming Language Design & Implementation", "Conference on Object-Oriented Programming Systems, Languages, and Applications", "High Performance Computer Architecture", "ACM International Symposium on Microarchitecture"]
n_pages = 50

#test
user_url = 'https://scholar.google.com/scholar?as_ylo=2018&q=%s&hl=zh-CN&as_sdt=0,5&start=%d' % ('usenix atc', 0)
User = {}
#r = requests.get(user_url)
#print(r.content)
#tree = html.fromstring(r.content)
driver.get(user_url)
tree = html.fromstring(driver.page_source)
time.sleep(120)

for (key_id, key_word) in enumerate(key_words[14:]):
    key_word = key_word.lower()
    key_word = key_word.replace(' ', '+')
    key_word2 = key_word.replace('+', '_')
    f = open('paper_list/%s' % key_word2, 'a+')

    for page_id in range(43, n_pages):
        user_url = 'https://scholar.google.com/scholar?as_ylo=2018&q=%s&hl=zh-CN&as_sdt=0,5&start=%d' % (key_word, page_id * 10)
        User = {}
        #r = requests.get(user_url)
        #print(r.content)
        #tree = html.fromstring(r.content)
        driver.get(user_url)
        tree = html.fromstring(driver.page_source)
        res_list = tree.xpath('//div[@class="gs_ri"]/h3[@class="gs_rt"]/a')
        ref_list = tree.xpath('//div[@class="gs_ri"]/h3[@class="gs_rt"]/a/../../div[@class="gs_a"]')
        abs_list = tree.xpath('//div[@class="gs_ri"]/h3[@class="gs_rt"]/a/../../div[@class="gs_rs"]')
        #res_list = tree.xpath('//div[@class="gs_ri"]/h3[@class="gs_rt"]/a')
        #ref_list = tree.xpath('//div[@class="gs_ri"]/div[@class="gs_a"]')
        for (ind, res) in enumerate(res_list):
            content = res.text_content()
            abs = abs_list[ind].text_content().replace('\n', ' ')
            print('key_id = %d, key_word = %s, page_id = %d, title = %s' % (key_id, key_word, page_id, content))
            f.write('%s | %s | %s\n' % (content, ref_list[ind].text_content(), abs))
        time.sleep(random.random() + 3)
    f.close()
driver.quit()
