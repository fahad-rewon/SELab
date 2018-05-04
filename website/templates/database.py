import sqlite3
from bs4 import BeautifulSoup
import requests

# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB


try:
    db = sqlite3.connect('C:\sqlite\mydb.db')
    cursor = db.cursor()
    # Get a cursor object
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product(product_id INTEGER PRIMARY KEY, product_name TEXT,
                           web_link TEXT, image_link TEXT)
    ''')
    db.commit()
except:
    print('table already exists1')
finally:
    product_id=0;


##men clothing scrapper bagdoom

    page_no = 0
    source = requests.get('https://www.bagdoom.com/men/clothing').text
    soup = BeautifulSoup(source, 'lxml')

    productAmountText = soup.find('p', class_='amount').text
    print(productAmountText)

    productAmount = productAmountText.split(' ')[33]  # 33rd index has amount of products
    print(productAmount)

    amount = int(productAmount)  # string to int
    print(amount)
    totalPage = int(amount / 60) + 1  # total no of pages that needs to be checked
    print(totalPage)

    while (page_no < totalPage):

        page_no = page_no + 1   #int
        pageRef = ('https://www.bagdoom.com/men/clothing.html?p=') + str(page_no)   #string
        source = requests.get(pageRef).text     #string
        # print(source)

        soup = BeautifulSoup(source, 'lxml')    #string
        # print(soup.prettify())

        allProducts = soup.find('ul', class_='products-grid first')     #string
        # print(allProducts.prettify())

        counter = 0 #int
        for singleProduct in allProducts.find_all('a', class_='product-image'):
            # singleProductRef=allProducts.find('a', class_='product-image')['href']
            # singleProductTitle=allProducts.find('a', class_='product-image')['title']
            # singleProductImage=allProducts.find('a', class_='product-image').img['src']

            singleProductRef = singleProduct['href']        #string
            singleProductTitle = singleProduct['title']     #string
            singleProductImage = singleProduct.img['src']   #string

            counter = counter + 1   #int
            print(singleProductRef)
            print(singleProductTitle)
            print(singleProductImage)
            print()

            cursor.execute(''' INSERT INTO product(product_id, product_name, web_link, image_link)
                VALUES (?, ?, ?, ?)''', (product_id, singleProductTitle, singleProductRef, singleProductImage))
            db.commit()
            product_id=product_id+1 #int. also primary key for the database


        print(counter)
        print(page_no)

##women clothing scrapper bagdoom

    page_no = 0
    source = requests.get('https://www.bagdoom.com/women/clothing.html?p=1').text
    soup = BeautifulSoup(source, 'lxml')

    productAmountText = soup.find('p', class_='amount').text
    print(productAmountText)

    productAmount = productAmountText.split(' ')[33]  # 33rd index has amount of products
    print(productAmount)

    amount = int(productAmount)  # string to int
    print(amount)
    totalPage = int(amount / 60) + 1  # total no of pages that needs to be checked
    print(totalPage)

    while (page_no < totalPage):

        page_no = page_no + 1
        pageRef = ('https://www.bagdoom.com/women/clothing.html?p=') + str(page_no)
        source = requests.get(pageRef).text
        # print(source)

        soup = BeautifulSoup(source, 'lxml')
        # print(soup.prettify())

        allProducts = soup.find('ul', class_='products-grid first')
        # print(allProducts.prettify())

        counter = 0
        for singleProduct in allProducts.find_all('a', class_='product-image'):
            # singleProductRef=allProducts.find('a', class_='product-image')['href']
            # singleProductTitle=allProducts.find('a', class_='product-image')['title']
            # singleProductImage=allProducts.find('a', class_='product-image').img['src']

            singleProductRef = singleProduct['href']
            singleProductTitle = singleProduct['title']
            singleProductImage = singleProduct.img['src']

            counter = counter + 1
            print(singleProductRef)
            print(singleProductTitle)
            print(singleProductImage)
            print()

            cursor.execute(''' INSERT INTO product(product_id, product_name, web_link, image_link)
                VALUES (?, ?, ?, ?)''', (product_id, singleProductTitle, singleProductRef, singleProductImage))
            db.commit()
            product_id=product_id+1


        print(counter)
        print(page_no)


##mobile scrapper bagdoom
    page_no = 0
    source = requests.get('https://www.bagdoom.com/electronics/mobiles-tabs/mobiles.html?p=1').text
    soup = BeautifulSoup(source, 'lxml')

    productAmountText = soup.find('p', class_='amount').text
    print(productAmountText)

    productAmount = productAmountText.split(' ')[33]  # 33rd index has amount of products
    print(productAmount)

    amount = int(productAmount)  # string to int
    print(amount)
    totalPage = int(amount / 60) + 1  # total no of pages that needs to be checked
    print(totalPage)

    while (page_no < totalPage):

        page_no = page_no + 1
        pageRef = ('https://www.bagdoom.com/electronics/mobiles-tabs/mobiles.html?p=') + str(page_no)
        source = requests.get(pageRef).text
        # print(source)

        soup = BeautifulSoup(source, 'lxml')
        # print(soup.prettify())

        allProducts = soup.find('ul', class_='products-grid first')
        # print(allProducts.prettify())

        counter = 0
        for singleProduct in allProducts.find_all('a', class_='product-image'):
            # singleProductRef=allProducts.find('a', class_='product-image')['href']
            # singleProductTitle=allProducts.find('a', class_='product-image')['title']
            # singleProductImage=allProducts.find('a', class_='product-image').img['src']

            singleProductRef = singleProduct['href']
            singleProductTitle = singleProduct['title']
            singleProductImage = singleProduct.img['src']

            counter = counter + 1
            print(singleProductRef)
            print(singleProductTitle)
            print(singleProductImage)
            print()

            cursor.execute(''' INSERT INTO product(product_id, product_name, web_link, image_link)
                VALUES (?, ?, ?, ?)''', (product_id, singleProductTitle, singleProductRef, singleProductImage))
            db.commit()
            product_id=product_id+1


        print(counter)
        print(page_no)



    db.close()