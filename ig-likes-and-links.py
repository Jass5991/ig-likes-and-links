# Instagram Web Scraper for Likes and Links
# Developed by Jay

# Special thanks to realsirjoe for their Instagram Scraper at https://github.com/realsirjoe/instagram-scraper
# Please adhere to the MIT License he used for their Instagram Scraper

from igramscraper.instagram import Instagram
import pandas as pd
from datetime import date

ig = Instagram()

media = ig.get_medias("instagram", 10)
# Replace "instagram" with any account page URL after the .com/ part 
# example: "https://www.instagram.com/instagram/" so just take "instagram"

data = []

df = pd.DataFrame(columns = ['URL','Likes'])

for i in range(10):
    temp = media[i]
    num = str(temp.likes_count)
    data.append([[temp.link],num])


# In[8]:

# testing outputs
print(data)

print(data[5][0],data[5][1])
print(len(data))

df = pd.DataFrame(data, columns = ['URL','Likes'])
df['URL'] = df['URL'].str.join(',')
df['Likes'] = df['Likes'].str.join('')
df

location = "../"
today = date.today()
print(today)
fformat = ".csv"
today = str(today)
filename = location+today+fformat
print(filename)

# Saves the information to a file name with today's current date, ie "2020-09-16.csv"

with open(filename, "w+") as f:
    df.to_csv(f, index=False)






