from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

# @app.route('/')
# def index():
#     return  'this is the homepage. Mehod used: %s' % request.method
#
#
# @app.route('/bacon', methods=['GET', 'post'])
# def bacons():
#     if request.method== 'POST':
#         return  'this is the bacon\n. Mehod used:POST'
#     else:
#         return 'using get'
#
# @app.route('/profile/<name>')
# def index(name):
#     return  render_template("profile.html", nam=name)

@app.route('/home')
def home():
    return render_template("home.html")     #launch home of website

@app.route('/process',methods=['POST'])
def process():
    search_item = request.form['search']    #query from the search box of the website

    db = sqlite3.connect('C:\sqlite\mydb.db')
    cursor = db.cursor()

    query="SELECT product_name, web_link, image_link FROM product WHERE product_name LIKE '%"+search_item+"%'"  #string

    cursor.execute('%s' % query)




    productTitleList=[]     #list
    productLinkList=[]      #list
    productImageList=[]     #list
    all_rows = cursor.fetchall()
    for row in all_rows:
        #row[0] returns the product_name, row[1] returns web_link, row[2] returns image_link
        print(row[0]+ row[1]+ row[2])
        print("hi")
        productTitleList.append(row[0])
        productLinkList.append(row[1])
        productImageList.append(row[2])
    print(search_item)

    return render_template("product.html", title_link_image=zip(productTitleList,productLinkList,productImageList))     #return query output in product page



if __name__ == "__main__":
    app.run(debug=True)