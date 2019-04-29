# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:14:07 2019

@author: shari
"""

# Importing the Libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

#Connectng with the URL
url= 'https://www.programmableweb.com/apis/directory'
web= requests.get(url)
web= web.text
soup= BeautifulSoup(web, 'html.parser')


# Extracting the Contents by Matching the Tags
body_odd = soup.find_all('tr',{'class':'odd'})
body_even = soup.find_all('tr',{'class':'even'})


# Test Extraction:
for b in body_even:
    title= b.find('a').text
    link= "https://www.programmableweb.com"+ b.find('a').get('href')
    category= b.find('td', {'class','views-field views-field-field-article-primary-category'}).text
    date= b.find('td', {'class','views-field views-field-created'}).text
    print(title, link,category,date)
    

# Extracting the odd Rows
count=0
odd_dict={}

while True:
    for b in body_odd:
        title= b.find('a').text
        link= "https://www.programmableweb.com"+ b.find('a').get('href')
        category= b.find('td', {'class','views-field views-field-field-article-primary-category'}).text
        date= b.find('td', {'class','views-field views-field-created'}).text
        count+=1
        odd_dict[count]= [title, link, category, date]

    url_tag= soup.find('a',{'title':'Go to next page'})
    if url_tag.get('href'):
        url= "https://www.programmableweb.com"+ url_tag.get('href')
    else:
        break

# Convert a Dictionary to a Dataframe

odd_df= pd.DataFrame.from_dict(odd_dict, orient='index', columns=['Title', 'Link', 'Category', 'Date'])


# Extracting the Even Rows
count=0
even_dict={}

while True:
    for b in body_even:
        title= b.find('a').text
        link= "https://www.programmableweb.com"+ b.find('a').get('href')
        category= b.find('td', {'class','views-field views-field-field-article-primary-category'}).text
        date= b.find('td', {'class','views-field views-field-created'}).text
        count+=1
        odd_dict[count]= [title, link, category, date]

    url_tag= soup.find('a',{'title':'Go to next page'})
    if url_tag.get('href'):
        url= "https://www.programmableweb.com"+ url_tag.get('href')
    else:
        break

# Convert a Dictionary to a Dataframe
even_df= pd.DataFrame.from_dict(even_dict, orient='index', columns=['Title', 'Link', 'Category', 'Date'])

# Concatenating the Two Dataframes

df= pd.concat([odd_df,even_df], ignore_index= True)

# Now df is the Final Dataframe
