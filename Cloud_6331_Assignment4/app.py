# Second Assignment


import math
import random

from flask import Flask, render_template, request, flash
import os
import datetime as dt
import csv
import pymysql

# Flask object
app = Flask(__name__)  # flask use this (__name__ ) argument to determine location of application

# Upload folder
UPLOAD_FOLDER = 'static/'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
app.secret_key = "AimanAj1987!@"


try:
    # the connection is successful connected to DB in Azure which we can not see it because we use PaaS
    username = 'aiman@advance-server'
    password = 'ssar1987!'
    database = 'cloud_db_6331'
    server = 'advance-server.mysql.database.azure.com'
    cnx = pymysql.connect(host=server, user=username, passwd=password, db=database, local_infile=True)
    cursor = cnx.cursor()
except:
    flash("No Connection to DataBase ^_^")
    print("NO CONNECTION ^_^")





# this Function will Delete Exist Table.
def drop_table():
    cursor.execute('DROP TABLE IF EXISTS earthquick')





# Return USER to HOME page
@app.route('/')
def upload_page():
    return render_template('home.html')



# Return USER to Main page
@app.route('/main')
def to_main_page():
    return render_template('main.html')




# Nav Home to return user to Main page
@app.route('/home')
def redirect_homepage():
    return render_template('main.html')




# Draw Pie Chart for Maginitudes
@app.route('/pie', methods=['POST', 'GET'])
def search_magnitude():
    if request.method == 'POST':
            magnitude2 = request.form['magnitude2']
            magnitude3 = request.form['magnitude3']
            sql = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between {} and {}".format(magnitude2,magnitude3)
            cursor.execute(sql)
            current_data = cursor.fetchmany()
            first1 =current_data[0][0]
            sql1 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag <=1"
            cursor.execute(sql1)
            current_data = cursor.fetchmany()
            first2 = current_data[0][0]
            sql2 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 0 and 1"
            cursor.execute(sql2)
            current_data = cursor.fetchall()
            first3 =current_data[0][0]
            sql3 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 1 and 2"
            cursor.execute(sql3)
            current_data = cursor.fetchall()
            first4 =current_data[0][0]

            sql3 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 2 and 3"
            cursor.execute(sql3)
            current_data = cursor.fetchall()
            first5 =current_data[0][0]

            sql4 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 3 and 4"
            cursor.execute(sql4)
            current_data = cursor.fetchall()
            first6 =current_data[0][0]

            sql5 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 4 and 5"
            cursor.execute(sql5)
            current_data = cursor.fetchall()
            first7 =current_data[0][0]

            sql6 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 5 and 6"
            cursor.execute(sql6)
            current_data = cursor.fetchall()
            first8 =current_data[0][0]

            sql7 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 6 and 7"
            cursor.execute(sql7)
            current_data = cursor.fetchall()
            first9 =current_data[0][0]

            sql8 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 7 and 8"
            cursor.execute(sql8)
            current_data = cursor.fetchall()
            first10 =current_data[0][0]


            return render_template('pie.html', first1 =first1, first2 =first2, first3=first3, first4=first4, first5=first5,first6=first6,first7=first7,first8=first8,first9=first9,first10=first10)


    if request.method == 'GET':
            return render_template('pie.html')

    else:
        return render_template('main.html')




# Draw Pie Chart for Maginitudes
@app.route('/bar_chart', methods=['POST', 'GET'])
def bar_chart():
    if request.method == 'POST':
            magnitude2 = request.form['magnitude2']
            magnitude3 = request.form['magnitude3']
            sql = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between {} and {}".format(magnitude2,magnitude3)
            cursor.execute(sql)
            current_data = cursor.fetchmany()
            # current_data[0][0] Will get only total number of return Values
            first1 =current_data[0][0]
            sql1 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag <=1"
            cursor.execute(sql1)
            current_data = cursor.fetchmany()
            first2 = current_data[0][0]
            sql2 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 0 and 1"
            cursor.execute(sql2)
            current_data = cursor.fetchall()
            first3 =current_data[0][0]
            sql3 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 1 and 2"
            cursor.execute(sql3)
            current_data = cursor.fetchall()
            first4 =current_data[0][0]

            sql3 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 2 and 3"
            cursor.execute(sql3)
            current_data = cursor.fetchall()
            first5 =current_data[0][0]

            sql4 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 3 and 4"
            cursor.execute(sql4)
            current_data = cursor.fetchall()
            first6 =current_data[0][0]

            sql5 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 4 and 5"
            cursor.execute(sql5)
            current_data = cursor.fetchall()
            first7 =current_data[0][0]

            sql6 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 5 and 6"
            cursor.execute(sql6)
            current_data = cursor.fetchall()
            first8 =current_data[0][0]

            sql7 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 6 and 7"
            cursor.execute(sql7)
            current_data = cursor.fetchall()
            first9 =current_data[0][0]

            sql8 = "SELECT count(*) FROM cloud_db_6331.earthquick WHERE mag between 7 and 8"
            cursor.execute(sql8)
            current_data = cursor.fetchall()
            first10 =current_data[0][0]


            return render_template('bar_chart.html', first1 =first1, first2 =first2, first3=first3, first4=first4, first5=first5,first6=first6,first7=first7,first8=first8,first9=first9,first10=first10)


    if request.method == 'GET':
            return render_template('bar_chart.html')

    else:
        return render_template('main.html')













# Show Line of graph for EarthQuickes between range of time & Mag
@app.route('/line_chart', methods=['POST', 'GET'])
def line_chart():
    if request.method == 'POST':
        magnitudeoneWeek1 = request.form['magnitudeoneWeek1']
        magnitudeoneWeek2 = request.form['magnitudeoneWeek2']
        day1 = request.form['day1']
        day2 = request.form['day2']
        sql1 = "SELECT  mag , substring(time, 1, 10) as date, count(*) as occurences from earthquick where mag between {} and {} and earthquick.time between '{}' and '{}' group by substring(time, 1, 10) order by date".format(magnitudeoneWeek1 , magnitudeoneWeek2 , day1 , day2)

        #sql = "SELECT * FROM cloud_db_6331.earthquick WHERE earthquick.mag between '{}' and '{}'  AND  earthquick.time BETWEEN '{}' AND '{}' order by time".format(magnitudeoneWeek1 , magnitudeoneWeek2 , day1 , day2)
        cursor = cnx.cursor()
        cursor.execute(sql1)
        result=cursor.fetchall()
        return render_template('line_chart.html', result=result)
    if request.method == 'GET':
        return render_template('line_chart.html', result="")









#Find earthquakes that were near (20 km, 50 km?) of a specified location.
@app.route('/scatter_plot', methods=['POST','GET'])
def scatter_plot():

        sql = "select  mag, earthquick.depth from cloud_db_6331.earthquick order by earthquick.time desc limit 100"
        cursor = cnx.cursor()
        cursor.execute(sql)
        result = cursor.fetchall();

        return render_template('scatter_plot.html', result=result)









# uploaded CSV file
file_path =''
@app.route("/home", methods=['POST','GET'])
def uploadFile():

    # get the uploaded file
    uploaded_file1 = request.files['file1']
    #uploaded_file2 = request.files['file2']

    if uploaded_file1.filename != '':

        file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file1.filename)
        # file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file2.filename)
        arr = file_path1.split('.')
        sub_string = arr[1]
        if sub_string == 'csv':
            uploaded_file1.save(file_path1)
       # uploaded_file2.save(file_path2)
            print(file_path1)
            drop_table()
            with open(file_path1, 'rt', encoding='Latin-1') as csvfile:
                reader = csv.reader(csvfile, quotechar='`')
                head = next(reader)

            sql = "create table if not exists earthquick("
            for i in range(0, len(head) - 1):
                sql += head[i] + " varchar(100), "
            sql += head[len(head) - 1] + " varchar(100))"

            cursor.execute(sql)
            get_all_data = """LOAD DATA LOCAL INFILE '{}'
                INTO TABLE earthquick FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;""".format(file_path1)

            cursor.execute(get_all_data)
            cnx.commit()


            return render_template('main.html')

        else:
            flash("Only CSV file allowed")
            return render_template('home.html')

    else:
        return render_template('home.html')






if __name__ == "__main__":
    app.run( debug=True)


