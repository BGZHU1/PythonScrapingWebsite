import requests
from bs4 import BeautifulSoup

class ScraperClass:

    TAG_PAIR_LIST={'johnvarvatos':(['span','class','price-standard'],
                                  ['span','class','price-sales']),

                   'reebok':      (['span','class','sale-price discounted'],
                                  ['span','class','baseprice']),

                   'shop-rica':   (['span','class','product-price on-sale'],
                                  ['span','class','product-compare-price']),

                   'aeropostale': (['ul','class','price'],)

                                 }

    def __init__(self,urlList):
        #get urlName and link
        self.brandName=urlList[0]
        self.urlLink=urlList[1]

        #find matching pattern in the search pair
        self.tagPair=self.findTagPair(self.brandName)

        #perform the search
        self.performSearch(self.tagPair,self.urlLink,self.brandName)

    def findTagPair(self,brandName):
        #print(urlName)
        self.pattern=ScraperClass.TAG_PAIR_LIST[brandName]
        return self.pattern

    def performSearch(self,tagPair,urlLink,brandName):

        self.r=requests.get(urlLink)
        self.soup=BeautifulSoup(self.r.content,'lxml')

        #print(len(tagPair))
        print('\n'+brandName+'\n')
        for i in range(len(tagPair)):
            result=self.soup.find_all(tagPair[i][0],{tagPair[i][1]:tagPair[i][2]})
            print(result[0].text.strip())
