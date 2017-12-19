from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import lxml.html
import traceback
import threading
import datetime
import urllib2
import logging
import codecs
import math
import time
import sys
import os
import re

main_link = "http://www.fikrabul.com"
save_path = unicode("/home/aselsan/Users/kerem/NLP_Project/Fikralar")

page = urllib2.urlopen(main_link)
main_soup = BeautifulSoup(page)


for category in main_soup.findAll('a'):
        if "fikrabul/kategori/" in category.get('href'):
                number = int(re.search(r'\d+', category.get('href')).group())
                if number > 19 and number < 22:
                        cat_link = category.get('href')
                        cat_name = category.text
                        print "Category: ********* ", cat_name, "*********"
                        
                        cat_page = urllib2.urlopen(main_link + cat_link)
                        cat_soup = BeautifulSoup(cat_page)


                        nextPage = True
                        while nextPage:                             
                                for column in cat_soup.findAll("div", { "class" : "kategoriicerik" }):
                                        for element in column.contents:
                                                str_element = str(element)
                                                if "sari.gif" in str_element:
                                                        content = unicode('kufurlu')
                                                elif "yesil.gif" in str_element:
                                                        content = unicode('normal')
                                                elif "kirmizi.gif" in str_element:
                                                        content = unicode('belalti')
                                        
                                                if "href" in str_element:
                                                        fikra_name = element.text
                                                        if "/" in fikra_name:
                                                                fikra_name.replace("/", " ")
                                                        
                                                        fikra_link = element.get('href')

                                                
                                                if 'font' in str_element:
                                                        if str_element[18].isdigit():
                                                                score = str_element[15:19]
                                                        elif str_element[17].isdigit():
                                                                score = str_element[15:18] + '0' 
                                                        else:        
                                                                score = str_element[15] + ',00' 
                                                                        
                                                        f_path = save_path + "/" + cat_name + "/" + score + "_" + fikra_name + "_" + content + ".txt"
                                                        
                                                        if not os.path.exists(save_path + "/" + cat_name + "/"):
                                                            os.makedirs(save_path + "/" + cat_name + "/")
                                                            
                                                        f = codecs.open(f_path, "w", "UTF-8")

                                                        fikra_page = urllib2.urlopen(main_link + fikra_link)
                                                        fikra_soup = BeautifulSoup(fikra_page)

                                                        content = fikra_soup.find("div", { "class" : "icerik" })
                                                        f.write(content.text)
                                                        f.close()
                                                        print fikra_name


                                nextPage = False
                                all_links_in_cat_page = cat_soup.findAll("a")
                                for link in all_links_in_cat_page:
                                        if link.text == "Sonraki Sayfa":
                                                link_to_next_page = link.get('href')
                                                nextPage = True               
                                if nextPage:
                                        cat_page = urllib2.urlopen(main_link + link_to_next_page)
                                        cat_soup = BeautifulSoup(cat_page)




