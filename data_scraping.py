# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:39:49 2020

@author: Hitesh
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen as urlReq
import pandas as pd

TV=[]
r=0
TV_Brand=[]
TV_Ratings=[]
TV_size=[]
TV_HD=[]
TV_speakers=[]
TV_hdmi=[]
TV_usb=[]
TV_cost=[]
    
URL1="https://www.flipkart.com/search?q=tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv%7CTVs&requestId=3ee7e2ac-b845-4a0c-a075-232968460b29&as-backfill=on"
URL2="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"
URL3="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=3"
URL4="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=4"
URL5="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=5"
URL6="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=6"
URL7="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=7"
URL8="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=8"
URL9="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=9"

URL=[URL1,URL2,URL3,URL4,URL5,URL6,URL7,URL8,URL9]
for i in URL:
    Client=urlReq(URL1)
    html_data=Client.read()
    Client.close()
    print(i)
    soup = BeautifulSoup(html_data, 'html.parser')
    
    #Brand of TV
    names=soup.find_all("div",{"class":"_3wU53n"})
    for name in names:
        TV_Brand.append(name.text.split(' ')[0])
    
    
    #TV ratings
    ratings=soup.find_all("div",{"class":"hGSR34"})
    for rating in ratings:
        if(r<len(TV_Brand)):
            TV_Ratings.append(float(rating.text))
            r+=1
    
    #TV size
    sizes=soup.find_all("div",{"class":"_3wU53n"})
    for size in sizes:
        size_of_tv = size.text[int(size.text.find("("))+1:int(size.text.find(")"))]
        if('inch' in size_of_tv):
            size_of_tv=size_of_tv.split()[0]
            
        TV_size.append(float(size_of_tv))
    
    #HD
    HDs=soup.find_all("ul",{"class":"vFw0gD"})
    for HD in HDs:
        for li in HD.find_all("li",{"class":"tVe95H"}):
            if('Full HD' in li.text):
               TV_HD.append('Full HD')
            if('HD Ready'in li.text):
               TV_HD.append('HD')
            if('Ultra HD (4K)'in li.text):
               TV_HD.append('Ultra HD 4K')
            if('Ultra HD (8K)'in li.text):
               TV_HD.append('Ultra HD 8K')
            else:
                TV_HD.append('Other')

    #Speakers
    speakers=soup.find_all("ul",{"class":"vFw0gD"})
    for speaker in speakers:
        for li in speaker.find_all("li",{"class":"tVe95H"}):
            if('Speaker' in li.text):
                TV_speakers.append(int(li.text.lower().split('w')[0]))
    
    #Hdmi
    HDMIS=soup.find_all("ul",{"class":"vFw0gD"})
    for HDMI in HDMIS:
        for li in HDMI.find_all("li",{"class":"tVe95H"}):
            if('HDMI' in li.text):
                TV_hdmi.append(int(li.text.split('x')[0]))
        
    #USB
    USBS=soup.find_all("ul",{"class":"vFw0gD"})
    for USB in USBS:
        for li in USB.find_all("li",{"class":"tVe95H"}):
            if('USB' in li.text):
                TV_usb.append(int(li.text.split('x')[1].split('| ')[1]))
                break
    
    #Cost of TV
    costs=soup.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
    for cost in costs:
        price= cost.text.split('₹')[1]
        price= price.replace(',', '')
        TV_cost.append(int(price))
        
    #creatinf dataframe
for Brand,Ratings,Speaker,Size,HD,HDMI,USB,Cost in zip(TV_Brand,TV_Ratings,TV_speakers,TV_size,TV_HD,TV_hdmi,TV_usb,TV_cost):
    TV.append({'Brand':Brand,'Ratings':Ratings,'Speaker':Speaker,'Size':Size,'HD':HD,'HDMI':HDMI,'USB':USB,'Cost':Cost})
    
    
TV_data=pd.DataFrame(TV)
    
TV_data.to_csv(r'G:\Hitesh\TV from flipkart\TV.csv',index=False)
