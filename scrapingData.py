import requests
from bs4 import BeautifulSoup
url="https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Flushing%2C+NY"
r=requests.get(url)

#print(r)
#print(r.content)
#give back to html content related to that request
soup=BeautifulSoup(r.content)
#print(soup)
#print(r.content)
links=soup.find_all("a")
#print(links)
#for link in links :
    #print link

#for link in soup.find_all('a'):
    #print link.get("href")
    #print link.text

#password protected has limitation
#for link in links:
    #print "<a href='%s'>%s</a>" %(link.get("href"),link.text)

g_data = soup.find_all('div',{'class':'info'})
#print('g_data',g_data)
for item in g_data:
    try:
        print item.contents[0].find_all('span',{'itemprop':'name'})[0].text
    except:
        pass
    #try:
        #print item.contents[0].find_all('span',{'class':'street-address'}).text
        #print item.contents[1].text
    #except:
        #pass
