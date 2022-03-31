from bs4 import BeautifulSoup
import requests

#ur request
url =  f"https://www.contractsfinder.service.gov.uk/Search/Results"

source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')

# print with prettify will print the output as a beautiful html file
print(soup.prettify())


div_search_result = soup.find_all('div',class_='search-result')


for x in range(len(div_search_result)):
    # Extract title
    title = div_search_result[x].h2.text
    print(f'\n{title}\n')

    #Extract sub head
    sub_header = div_search_result[x].find(class_='search-result-sub-header wrap-text').text
    print(f'{sub_header}\n')

    #Extract wrap text
    wrap_text = div_search_result[x].find_all(class_='wrap-text')[1].text
    print(f'{wrap_text}\n')

    #Extract strong
    strong = div_search_result[x].find_all(class_='search-result-entry')

    for o in range(len(strong)):
        print(strong[o].text)

    #Extract link    
    link = div_search_result[x].h2.a['href']
    print(f'\n{link}\n')
    print("-"*125)



titles = []
sub_headers=[]
wrap_texts=[]
links=[]
all_strongs = []

for x in range(len(div_search_result)):
    #Extract title
    title = div_search_result[x].h2.text
    titles.append(title)
    
    #Extract sub head
    sub_header = div_search_result[x].find(class_='search-result-sub-header wrap-text').text
    sub_headers.append(sub_header)
    
    #Extract wrap text
    wrap_text = div_search_result[x].find_all(class_='wrap-text')[1].text
    wrap_texts.append(wrap_text)
    
    #Extract strong
    strong = div_search_result[x].find_all(class_='search-result-entry')

    strongs = []
    
    for o in range(len(strong)):
        strongs.append(strong[o].text)
    
    all_strongs.append(strongs)
    #Extract link    
    link = div_search_result[x].h2.a['href']
    links.append(link)


import pandas as pd 
import numpy as np 


zipped = list(zip(titles,sub_headers,wrap_texts,all_strongs,links))


final_data = pd.DataFrame(zipped,columns=['titles','sub_headers','wrap_texts','all_strongs','links'])
final_data

final_data.to_csv('Gov_uk.csv')