
from flask import Flask, render_template, request



app = Flask(__name__)


# Define all The list Which will each one have all the comments from The users
desktop_review1 = list()
desktop_review2 = list()
desktop_review3 = list()

laptop_review1 = list()
laptop_review2 = list()
laptop_review3 = list()

new_phone1_review = list()
new_phone2_review = list()
new_phone3_review = list()

use_phone1_review = list()
use_phone2_review = list()
use_phone3_review = list()


price_desktops = [1250,1800,2500]
description_desktops =['New Alienware Desktop','Toshiba Gaming Desktop','Apple Mini Desktop']

price_laptops = [1000,1500,500]
description_laptops =['Better For Games','Lightweight Laptop','Good For School']

price_new_phones = [1200,1100,200]
description_new_phones =['Iphone 11 pro','Galaxy S9+','Motorola razr v4']

price_use_phones = [350,100,450]
description_use_phones =['Iphone 5S','Galaxy S7 Edge','I phone 6s Plus']


# total No of Items
Total_item = list()

# The whole Price
Total_cart = list()


# Redirect USER to Home page
@app.route('/')
def upload_page():
    return render_template('home.html')


# Redirect USER From Home page to same page
@app.route('/home')
def redirect_homepage():
    return render_template('home.html')


# Redirect USER to Computer page
@app.route('/computer')
def redirect_computer():
    return render_template('computer.html')


# ---------------------------------------- All pages with Information ----------------------------------------------#

# Redirect USER To desktops Page
@app.route('/desktop', methods=['POST', 'GET'])
def redirect_desktop():
    if request.method == 'POST':
        if request.form['submit_desktop'] == 'submit1':
            comment1 = request.form['description1']
            desktop_review1.append(comment1)


        if request.form['submit_desktop'] == 'submit2':
            comment2 = request.form['description2']
            desktop_review2.append(comment2)


        if request.form['submit_desktop'] == 'submit3':
            comment3 = request.form['description3']
            desktop_review3.append(comment3)


    return render_template('desktop.html', comment1=desktop_review1, comment2=desktop_review2, comment3=desktop_review3,
                           description1=description_desktops[0], price1=price_desktops[0],
                           description2=description_desktops[1], price2=price_desktops[1],
                           description3=description_desktops[2], price3=price_desktops[2])




# Redirect USER To laptop Page
@app.route('/laptop', methods=['POST','GET'])
def redirect_laptop1():
    if request.method == 'POST':
        if request.form['laptop_submit'] == 'laptop1':
            comment1 = request.form['description1']
            laptop_review1.append(comment1)

        if request.form['laptop_submit'] == 'laptop2':
            comment2 = request.form['description2']
            laptop_review2.append(comment2)

        if request.form['laptop_submit'] == 'laptop3':
            comment3 = request.form['description3']
            laptop_review3.append(comment3)


    return render_template('laptop.html', comment1=laptop_review1, comment2=laptop_review2, comment3=laptop_review3,
                           price1=price_laptops[0], description1=description_laptops[0], price2=price_laptops[1],
                           description2=description_laptops[1], price3=price_laptops[2],
                           description3=description_laptops[2])





# Redirect USER To Phone page
@app.route('/phone')
def redirect_phones():
    return render_template('phone.html')



# Redirect USER To New Phone page
@app.route('/new_phones', methods=['POST','GET'])
def redirect_new_phones():
    if request.method == 'POST':

        if request.form['submit_new_phone'] == 'new_phone1':
            comment1 = request.form['description1']
            new_phone1_review.append(comment1)

        if request.form['submit_new_phone'] == 'new_phone2':
            comment2 = request.form['description2']
            new_phone2_review.append(comment2)

        if request.form['submit_new_phone'] == 'new_phone3':
            comment3 = request.form['description3']
            new_phone3_review.append(comment3)


    return render_template('new_phones.html', comment1=new_phone1_review, comment2=new_phone2_review,
                           comment3=new_phone3_review, price1=price_new_phones[0],
                           description1=description_new_phones[0], price2=price_new_phones[1],
                           description2=description_new_phones[1], price3=price_new_phones[2],
                           description3=description_new_phones[2])





# Redirect USER To Use Phone page
@app.route('/used_phones', methods=['POST','GET'])
def redirect_used_phones1():
    if request.method == 'POST':

        if request.form['used_phone_submit'] == 'used_phone1':
            comment1 = request.form['description1']
            use_phone1_review.append(comment1)

        if request.form['used_phone_submit'] == 'used_phone2':
            comment2 = request.form['description2']
            use_phone2_review.append(comment2)

        if request.form['used_phone_submit'] == 'used_phone3':
            comment3 = request.form['description3']
            use_phone3_review.append(comment3)


    return render_template('used_phones.html', comment1=use_phone1_review, comment2=use_phone2_review,
                           comment3=use_phone3_review, p1=price_use_phones[0],
                           d1=description_use_phones[0], p2=price_use_phones[1],
                           d2=description_use_phones[1], p3=price_use_phones[2],
                           d3=description_use_phones[2])





# -----------------------------------  Search Option--------------------------------------------------------------#



@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method =='POST':

            search = request.form['search']

            if search == '':
                return render_template('home.html')

            for i in description_desktops:
                    # Search For Substring or String
                    if search in i or search == i:
                        return render_template('desktop.html', comment1=desktop_review1, comment2=desktop_review2,
                                               comment3=desktop_review3, description1=description_desktops[0],
                                               price1=price_desktops[0],
                                               description2=description_desktops[1], price2=price_desktops[1],
                                               description3=description_desktops[2], price3=price_desktops[2])
                        break

            for i in desktop_review1:
                # Search For Substring or String
                if search in i or search == i:
                    return render_template('desktop.html', comment1=desktop_review1, comment2=desktop_review2,
                                           comment3=desktop_review3, description1=description_desktops[0],
                                           price1=price_desktops[0],
                                           description2=description_desktops[1], price2=price_desktops[1],
                                           description3=description_desktops[2], price3=price_desktops[2])
                    break

            for i in desktop_review2:
                # Search For Substring or String
                if search in i or search == i:
                    return render_template('desktop.html', comment1=desktop_review1, comment2=desktop_review2,
                                           comment3=desktop_review3, description1=description_desktops[0],
                                           price1=price_desktops[0],
                                           description2=description_desktops[1], price2=price_desktops[1],
                                           description3=description_desktops[2], price3=price_desktops[2])
                    break


            for i in desktop_review3:
                # Search For Substring or String
                if search in i or search == i:
                    return render_template('desktop.html', comment1=desktop_review1, comment2=desktop_review2,
                                           comment3=desktop_review3, description1=description_desktops[0],
                                           price1=price_desktops[0],
                                           description2=description_desktops[1], price2=price_desktops[1],
                                           description3=description_desktops[2], price3=price_desktops[2])
                    break

#------------------------------------- End Iterate in Desktop Section -------------------------------------------------#




            for j in description_laptops:
                    if search in j or j == search :
                        return render_template('laptop.html', comment1=laptop_review1, comment2=laptop_review2,
                                               comment3=laptop_review3, price1=price_laptops[0],
                                               description1=description_laptops[0], price2=price_laptops[1],
                                               description2=description_laptops[1], price3=price_laptops[2],
                                               description3=description_laptops[2])
                        break

            for j in laptop_review1:
                if search in j or j == search:
                    return render_template('laptop.html', comment1=laptop_review1, comment2=laptop_review2,
                                           comment3=laptop_review3, price1=price_laptops[0],
                                           description1=description_laptops[0], price2=price_laptops[1],
                                           description2=description_laptops[1], price3=price_laptops[2],
                                           description3=description_laptops[2])
                    break



            for j in laptop_review2:
                if search in j or j == search:
                    return render_template('laptop.html', comment1=laptop_review1, comment2=laptop_review2,
                                           comment3=laptop_review3, price1=price_laptops[0],
                                           description1=description_laptops[0], price2=price_laptops[1],
                                           description2=description_laptops[1], price3=price_laptops[2],
                                           description3=description_laptops[2])
                    break


            for j in laptop_review3:
                if search in j or j == search:
                    return render_template('laptop.html', comment1=laptop_review1, comment2=laptop_review2,
                                           comment3=laptop_review3, price1=price_laptops[0],
                                           description1=description_laptops[0], price2=price_laptops[1],
                                           description2=description_laptops[1], price3=price_laptops[2],
                                           description3=description_laptops[2])
                    break

 # --------------------------------------------------------------- END Iterate Laptop Section -------------------------#



            for k in description_new_phones:
                    if search in k or k == search:
                        return render_template('new_phones.html', comment1=new_phone1_review, comment2=new_phone2_review,
                                               comment3=new_phone3_review, price1=price_new_phones[0],
                                               description1=description_new_phones[0], price2=price_new_phones[1],
                                               description2=description_new_phones[1], price3=price_new_phones[2],
                                               description3=description_new_phones[2])

                        break




            for k in new_phone1_review:
                    if search in k or k == search:
                        return render_template('new_phones.html', comment1=new_phone1_review, comment2=new_phone2_review,
                                               comment3=new_phone3_review, price1=price_new_phones[0],
                                               description1=description_new_phones[0], price2=price_new_phones[1],
                                               description2=description_new_phones[1], price3=price_new_phones[2],
                                               description3=description_new_phones[2])

                        break



            for k in new_phone2_review:
                    if search in k or k == search:
                        return render_template('new_phones.html', comment1=new_phone1_review, comment2=new_phone2_review,
                                               comment3=new_phone3_review, price1=price_new_phones[0],
                                               description1=description_new_phones[0], price2=price_new_phones[1],
                                               description2=description_new_phones[1], price3=price_new_phones[2],
                                               description3=description_new_phones[2])

                        break



            for k in new_phone3_review:
                    if search in k or k == search:
                        return render_template('new_phones.html', comment1=new_phone1_review, comment2=new_phone2_review,
                                               comment3=new_phone3_review, price1=price_new_phones[0],
                                               description1=description_new_phones[0], price2=price_new_phones[1],
                                               description2=description_new_phones[1], price3=price_new_phones[2],
                                               description3=description_new_phones[2])

                        break




#------------------------------------------------------------ End iterate New Phone Section ---------------------------#




            for t in description_use_phones:
                    if search in t or t == search:
                        return render_template('used_phones.html', comment1=use_phone1_review,
                                               comment2=use_phone2_review,
                                               comment3=use_phone3_review, p1=price_use_phones[0],
                                               d1=description_use_phones[0], p2=price_use_phones[1],
                                               d2=description_use_phones[1], p3=price_use_phones[2],
                                               d3=description_use_phones[2])

                        break

            for t in use_phone1_review:
                    if search in t or t == search:
                        return render_template('used_phones.html', comment1=use_phone1_review,
                                               comment2=use_phone2_review,
                                               comment3=use_phone3_review, p1=price_use_phones[0],
                                               d1=description_use_phones[0], p2=price_use_phones[1],
                                               d2=description_use_phones[1], p3=price_use_phones[2],
                                               d3=description_use_phones[2])

                        break

            for t in  use_phone2_review:
                if search in t or t == search:
                    return render_template('used_phones.html', comment1=use_phone1_review, comment2=use_phone2_review,
                                           comment3=use_phone3_review, p1=price_use_phones[0],
                                           d1=description_use_phones[0], p2=price_use_phones[1],
                                           d2=description_use_phones[1], p3=price_use_phones[2],
                                           d3=description_use_phones[2])

                    break

            for t in use_phone3_review:
                if search in t or t == search:
                    return render_template('used_phones.html', comment1=use_phone1_review, comment2=use_phone2_review,
                                           comment3=use_phone3_review, p1=price_use_phones[0],
                                           d1=description_use_phones[0], p2=price_use_phones[1],
                                           d2=description_use_phones[1], p3=price_use_phones[2],
                                           d3=description_use_phones[2])

                    break

    return render_template('home.html')








# -----------------------------------  Buy Section Code --------------------------------------------------------------#



# Redirect USER To Purchase Page
@app.route('/buy', methods=['POST', 'GET'])
def buy_desktop1():


    if request.method == 'POST':
        if request.form['submit_desktop'] == 'desktop1':
            item_number1 = int(request.form['count_desktop1'])
            Total_cart.append(item_number1 * price_desktops[0])
            Total_item.append(item_number1)
            return render_template('desktop.html', comment1=desktop_review1, comment2=desktop_review2,
                                   comment3=desktop_review3,
                                   description1=description_desktops[0], price1=price_desktops[0],
                                   description2=description_desktops[1], price2=price_desktops[1],
                                   description3=description_desktops[2], price3=price_desktops[2])


        if request.form['submit_desktop'] == 'desktop2':
            item_number2 = int(request.form['count_desktop1'])
            Total_cart.append(item_number2 * price_desktops[1])
            Total_item.append(item_number2)
            return render_template('desktop.html', comment1=desktop_review1, comment2=desktop_review2,
                                   comment3=desktop_review3,
                                   description1=description_desktops[0], price1=price_desktops[0],
                                   description2=description_desktops[1], price2=price_desktops[1],
                                   description3=description_desktops[2], price3=price_desktops[2])



        if request.form['submit_desktop'] == 'desktop3':
            item_number3 = int(request.form['count_desktop1'])
            Total_cart.append(item_number3 * price_desktops[2])
            Total_item.append(item_number3)
            return render_template('desktop.html', comment1=desktop_review1, comment2=desktop_review2,
                                   comment3=desktop_review3,
                                   description1=description_desktops[0], price1=price_desktops[0],
                                   description2=description_desktops[1], price2=price_desktops[1],
                                   description3=description_desktops[2], price3=price_desktops[2])




        if request.form['submit_desktop'] == 'laptop1':
            item_number4 = int(request.form['count_desktop1'])
            Total_cart.append(item_number4 * price_laptops[0])
            Total_item.append(item_number4)
            return render_template('laptop.html', comment1=laptop_review1, comment2=laptop_review2,
                                   comment3=laptop_review3,
                                   price1=price_laptops[0], description1=description_laptops[0],
                                   price2=price_laptops[1],
                                   description2=description_laptops[1], price3=price_laptops[2],
                                   description3=description_laptops[2])

        if request.form['submit_desktop'] == 'laptop2':
            item_number5 = int(request.form['count_desktop1'])
            Total_cart.append(item_number5 * price_laptops[1])
            Total_item.append(item_number5)
            return render_template('laptop.html', comment1=laptop_review1, comment2=laptop_review2,
                                   comment3=laptop_review3,
                                   price1=price_laptops[0], description1=description_laptops[0],
                                   price2=price_laptops[1],
                                   description2=description_laptops[1], price3=price_laptops[2],
                                   description3=description_laptops[2])



        if request.form['submit_desktop'] == 'laptop3':
            item_number6 = int(request.form['count_desktop1'])
            Total_cart.append(item_number6 * price_laptops[2])
            Total_item.append(item_number6)
            return render_template('laptop.html', comment1=laptop_review1, comment2=laptop_review2,
                                   comment3=laptop_review3,
                                   price1=price_laptops[0], description1=description_laptops[0],
                                   price2=price_laptops[1],
                                   description2=description_laptops[1], price3=price_laptops[2],
                                   description3=description_laptops[2])



        if request.form['submit_desktop'] == 'new_phone1':
            item_number7 = int(request.form['count_desktop1'])
            Total_cart.append(item_number7 * price_new_phones[0])
            Total_item.append(item_number7)
            return render_template('new_phones.html', comment1=new_phone1_review, comment2=new_phone2_review,
                                   comment3=new_phone3_review, price1=price_new_phones[0],
                                   description1=description_new_phones[0], price2=price_new_phones[1],
                                   description2=description_new_phones[1], price3=price_new_phones[2],
                                   description3=description_new_phones[2])

        if request.form['submit_desktop'] == 'new_phone2':
            item_number8 = int(request.form['count_desktop1'])
            Total_cart.append(item_number8 * price_new_phones[1])
            Total_item.append(item_number8)
            return render_template('new_phones.html', comment1=new_phone1_review, comment2=new_phone2_review,
                                   comment3=new_phone3_review, price1=price_new_phones[0],
                                   description1=description_new_phones[0], price2=price_new_phones[1],
                                   description2=description_new_phones[1], price3=price_new_phones[2],
                                   description3=description_new_phones[2])


        if request.form['submit_desktop'] == 'new_phone3':
            item_number9 = int(request.form['count_desktop1'])
            Total_cart.append(item_number9 * price_new_phones[2])
            Total_item.append(item_number9)
            return render_template('new_phones.html', comment1=new_phone1_review, comment2=new_phone2_review,
                                   comment3=new_phone3_review, price1=price_new_phones[0],
                                   description1=description_new_phones[0], price2=price_new_phones[1],
                                   description2=description_new_phones[1], price3=price_new_phones[2],
                                   description3=description_new_phones[2])

        if request.form['submit_desktop'] == 'use_phone1':
            item_number10 = int(request.form['count_desktop1'])
            Total_cart.append(item_number10 * price_use_phones[0])
            Total_item.append(item_number10)
            return render_template('used_phones.html', comment1=use_phone1_review, comment2=use_phone2_review,
                                   comment3=use_phone3_review, p1=price_use_phones[0],
                                   d1=description_use_phones[0], p2=price_use_phones[1],
                                   d2=description_use_phones[1], p3=price_use_phones[2],
                                   d3=description_use_phones[2])


        if request.form['submit_desktop'] == 'use_phone2':
            item_number11 = int(request.form['count_desktop1'])
            Total_cart.append(item_number11 * price_use_phones[1])
            Total_item.append(item_number11)
            return render_template('used_phones.html', comment1=use_phone1_review, comment2=use_phone2_review,
                                   comment3=use_phone3_review, p1=price_use_phones[0],
                                   d1=description_use_phones[0], p2=price_use_phones[1],
                                   d2=description_use_phones[1], p3=price_use_phones[2],
                                   d3=description_use_phones[2])

        if request.form['submit_desktop'] == 'use_phone3':
            item_number12 = int(request.form['count_desktop1'])
            Total_cart.append(item_number12 * price_use_phones[2])
            Total_item.append(item_number12)
            return render_template('used_phones.html', comment1=use_phone1_review, comment2=use_phone2_review,
                                   comment3=use_phone3_review, p1=price_use_phones[0],
                                   d1=description_use_phones[0], p2=price_use_phones[1],
                                   d2=description_use_phones[1], p3=price_use_phones[2],
                                   d3=description_use_phones[2])



#------------------------------------- Check out Page -----------------------------------------------------------------#
@app.route('/Purchase')
def purchase():
    total_money = 0
    total_devices = 0
    for i in Total_cart:
        total_money = total_money + i

    for j in Total_item:
        total_devices = total_devices + j
    if total_money != 0:
        total_money = total_money +20

    return render_template('Purchase.html', total_price=total_money, total_cart=total_devices)








if __name__ == "__main__":

    app.run( debug=True)