import os
import requests
import csv
import pandas as pd
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

list0 = []
data = pd.read_csv("C:/Users/user/Downloads/applemobilitytrends-2022-03-29.csv")
geo_type = data['geo_type'].tolist()
country = data['country'].tolist()
for ele in range(len(geo_type)):
    if geo_type[ele] != "city":
        list0.append(ele)
for c in range(len(country)):
    if country[c] == "":
        country.pop(c)
country1 = set(country)
newcountry = list(country1)
newcountry.pop(0)
data.drop(list0,axis = 0, inplace=True)
data.drop("transportation_type",1)
data.drop("sub-region",1)
data.drop("alternative_name",1)
data.drop("country",1)
data.insert(810, column = "average", value = data.mean(axis = 1))
data.sort_values(by='average', ascending=False, inplace=True)
data.drop_duplicates(subset="region" , keep="first",inplace=True)
location = []
avg12 = []
for i in range(0,50):
    city = data.iat[i, 1]
    avg1 = data.iat[i, 810]
    location.append(city)
    avg12.append(avg1)
map = dict(type = 'choropleth',
locations = newcountry,
locationmode = 'country names',
colorscale= 'Hot',
z=[*range(1, 51, 1)],
colorbar = {'title':'Country Colours'})
chmap = go.Figure(data=[map])
iplot(chmap)
fig = plt.figure(figsize=(10, 15))
plt.bar(location, avg12, color='maroon',
        width=0.5)
plt.xlabel("Country")
plt.ylabel("Average mobility")
plt.title("Top 50 cities")
plt.xticks(rotation=90)
plt.show()