#!/usr/bin/python3
import requests
import time
import random
from lxml import html
from selenium.webdriver import Firefox
from selenium import webdriver
import re
driver = webdriver.Firefox()

key_words = ["usenix", "eurosys", "osdi", "sosp", "asplos", "isca", "fast", "sigmetrics", "sc", "ppopp", "dac", "pldi", "oopsla", "hpca", "micro"]
                                                #OSDI                           SOSP                                                #ASPLOS
#key_words = ['usenix atc', 'eurosys', 'ACM Symposium on Operating Systems', 'Symposium on Operating systems principles', 'International Conference on Architectural Support for Programming Languages and Operating Systems', 'International Symposium on Computer Architecture', "Conference on File and Storage Technologies", "International Conference on Measurement and Modeling of Computer Systems", "International Conference for High Performance Computing, Networking, Storage, and Analysis", "ACM SIGPLAN Symposium on Principles & Practice of Parallel Programming", "Design Automation Conference", "ACM SIGPLAN Conference on Programming Language Design & Implementation", "Conference on Object-Oriented Programming Systems, Languages, and Applications", "High Performance Computer Architecture", "ACM International Symposium on Microarchitecture"]
n_pages = 50

#test
pat = re.compile('20[0-9][0-9]')

for (key_id, key_word) in enumerate(key_words[:]):
    key_word = key_word.lower()
    f = open('paper_list2/%s' % key_word, 'w')

    for year in range(2018, 2022):
        user_url = "https://dblp.org/db/conf/%s/%s%d.html" % (key_word, key_word, year)
        driver.get(user_url)
        tree = html.fromstring(driver.page_source)
        res_list = tree.xpath('//span[@class="title"]')

        content_list = tree.xpath('//span[@class="title"]/../../li[@class="drop-down"][0]/a/@href')
        #content_list = tree.xpath('//span[@class="title"]/../a[@toc-link]/@href')
        for (ind, res) in enumerate(res_list):
            f.write('%s | %s\n' % (res.text_content(), year))
            #content = res.text_content()
            #res = pat.findall(content)
            #if res and int(res[0]) >= 2018:
            #    print(content_list[ind])

    #    abs = abs_list[ind].text_content().replace('\n', ' ')
    #    print('key_id = %d, key_word = %s, page_id = %d, title = %s' % (key_id, key_word, page_id, content))
    #    f.write('%s | %s | %s\n' % (content, ref_list[ind].text_content(), abs))
        time.sleep(random.random() + 3)
    f.close()
driver.quit()
