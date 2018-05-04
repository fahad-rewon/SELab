from bs4 import BeautifulSoup
import requests
import csv

page_no=0
source = requests.get('https://www.bagdoom.com/men/clothing').text
soup = BeautifulSoup(source, 'lxml')


productAmountText = soup.find('p', class_='amount').text
print(productAmountText)

productAmount = productAmountText.split(' ')[33]    #33rd index has amount of products
print(productAmount)

amount=int(productAmount)   #string to int
print(amount)
totalPage=int(amount/60)+1  #total no of pages that needs to be checked
print(totalPage)

while (page_no<totalPage):

    page_no=page_no+1
    pageRef=('https://www.bagdoom.com/men/clothing.html?p=')+str(page_no)
    source = requests.get(pageRef).text
    #print(source)

    soup = BeautifulSoup(source, 'lxml')
    #print(soup.prettify())

    allProducts = soup.find('ul', class_='products-grid first')
    #print(allProducts.prettify())

    counter=0
    for singleProduct in allProducts.find_all('a', class_='product-image'):

        # singleProductRef=allProducts.find('a', class_='product-image')['href']
        # singleProductTitle=allProducts.find('a', class_='product-image')['title']
        # singleProductImage=allProducts.find('a', class_='product-image').img['src']

        singleProductRef=singleProduct['href']
        singleProductTitle=singleProduct['title']
        singleProductImage=singleProduct.img['src']

        counter=counter+1
        print(singleProductRef)
        print(singleProductTitle)
        print(singleProductImage)
        print()


    print(counter)
    print(page_no)
