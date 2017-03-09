from ScraperClass import *

def main():
    url="https://www.johnvarvatos.com/linen-henley/K1368S4-QL6.html?dwvar_K1368S4-QL6_color=022#start=1"
    url2="http://www.reebok.com/us/reebok-crossfit-speed-tr-liberty-pack/BD3015.html"
    url3="https://www.shop-rica.com/collections/sale/products/amuse-society-gabriel-dress-black-sands"
    url4="http://www.aeropostale.com/lightweight-core-full-zip-hoodie/product.jsp?productId=63499836&cp=3534618.3534619.3534626.3595054.117324186"

    urlList=[('johnvarvatos',url),
             ('reebok',url2),
             ('shop-rica',url3),
             ('aeropostale',url4)
             ]

    #print(urlList[0][1])
    for i in range(len(urlList)):
        scraper=ScraperClass(urlList[i])


if __name__ == "__main__":
    main()
