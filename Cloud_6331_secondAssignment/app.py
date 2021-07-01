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




# TO SEARCH For Magnitude Large than 5.0
@app.route('/magnitude', methods=['POST', 'GET'])
def search_magnitude():
    if request.method == 'POST':
        magnitude = request.form['magnitude']
        value = float(magnitude)

        if value > 5.0:
            sql_query = "SELECT * FROM cloud_db_6331.earthquick WHERE mag > '{}'".format(magnitude)
            cursor.execute(sql_query)
            current_data = cursor.fetchall()
            total = len(current_data)
            return render_template('magnitude.html', post=current_data, total =total)
        else:
            flash("Enter only Values Greater than 5.0")
            return render_template('magnitude.html')


    if request.method == 'GET':
            return render_template('magnitude.html')

    else:
        return render_template('main.html')






# TO SEARCH For Magnitude in Specific Interval
@app.route('/magnitudeoneWeek', methods=['POST', 'GET'])
def magnitudeoneWeek_page():
    if request.method == 'POST':
        magnitudeoneWeek1 = request.form['magnitudeoneWeek1']
        magnitudeoneWeek2 = request.form['magnitudeoneWeek2']
        day1 = request.form['day1']
        day2 = request.form['day2']

        sql_query = "SELECT * FROM cloud_db_6331.earthquick WHERE (earthquick.mag between '{}' and '{}')  AND earthquick.time BETWEEN '{}' AND '{}'".format(magnitudeoneWeek1 , magnitudeoneWeek2 , day1 , day2)
        cursor.execute(sql_query)
        current_data = cursor.fetchall()


        return render_template('magnitudeoneWeek.html', post=current_data)

    if request.method == 'GET':
            return render_template('magnitudeoneWeek.html')

    else:
        return render_template('main.html')






# Clustering
@app.route('/clusters', methods=['POST', 'GET'])
def cluster():
    if request.method == 'POST':
        val1 = float(request.form['from_latitude'])
        val2 = float(request.form['from_longitude'])
        val3 = float(request.form['to_latitude'])
        val4 = float(request.form['to_longitude'])
        val5 = int(request.form['area'])
        length_area = math.pow(val5 , 0.5)
        degree_change = length_area / 100
        x_latitude = degree_change if val3 - val1 > 0 else -degree_change
        x_longitude = degree_change if val4 - val2 > 0 else -degree_change
        clusters = []
        lat_index = int(math.ceil((val3 - val1) / x_latitude))
        long_index = int(math.ceil((val4 - val2) / x_longitude))
        start_lat = val1
        Map = []

        for i in range(lat_index):
            end_lat = start_lat + x_latitude
            start_long = val2
            lower_lat = start_lat if start_lat < end_lat else end_lat
            upper_lat = start_lat if start_lat > end_lat else end_lat
            for j in range(long_index):
                end_long = start_long + x_longitude
                clusters.append([start_lat, start_long, end_lat, end_long])
                lower_long = start_long if start_long < end_long else end_long
                upper_long = start_long if start_long > end_long else end_long

                sql = "SELECT COUNT(*) AS COUNT, AVG(mag) AS MAG_AVG FROM cloud_db_6331.earthquick WHERE (latitude BETWEEN " + str(
                    lower_lat) + " AND " + str(upper_lat) + ") AND (LONGITUDE BETWEEN " + str(
                    lower_long) + " AND " + str(upper_long) + ")"
                rows = cursor.execute(sql)
        return render_template('clusters.html', post=rows)

    if request.method == 'GET':
        return render_template('clusters.html', post="current_data")





    # TO SEARCH For earthquakes near Specified Location 20KM or 50KM or ..etc





#Find earthquakes that were near (20 km, 50 km?) of a specified location.
@app.route('/earthquakes_near_location', methods=['POST', 'GET'])
def earthquakes_near_location_page():
    if request.method == 'POST':
        lat = request.form['lat']
        long = request.form['lon']
        dist = request.form['dist']

        cursor.execute("select * from cloud_db_6331.earthquick")
        rows = cursor.fetchall()
        count = 0
        radius = 6373.0

        for row in rows:
            lat1 = math.radians(float(lat))
            lon1 = math.radians(float(long))
            if row[1]!= '':
                lat2 = math.radians(float(row[1]))
            if row[2] != '':
                lon2 = math.radians(float(row[2]))
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = radius * c
            if (d < float(dist)):
                count = count + 1
        return render_template('earthquakes_near_location.html', count=count, dist=dist)

    if request.method == 'GET':
            return render_template("earthquakes_near_location.html", post="res")
    else:
        return render_template('main.html')













# TO SEARCH For Magnitude > 4 and Happend between 21 & 8 Oclock Midnight
@app.route('/large_mag', methods= ['POST', 'GET'])
def do_large_4():
    if request.method == 'POST':

        magnitude1 = request.form['magnitude22']

        value = float(magnitude1)
        if value > 4.0:
            sql_query = "SELECT * FROM cloud_db_6331.earthquick WHERE mag > '{}'".format(magnitude1)
            cursor.execute(sql_query)
            rows = cursor.fetchall();
            res = []
            for r in rows:
                date = r[0].split('T')[0] + r[0].split('T')[1][:-1]
                d = dt.datetime.strptime(date, '%Y-%m-%d%H:%M:%S.%f')
                night = dt.time(20, 00, 00, 00000)
                lighttime = dt.time(8, 0, 0, 0)
                day_time = d.time()
                if ((day_time > night) or (day_time < lighttime)):
                    res.append(r)
            return render_template("large_mag.html", post=res)
        else:
            flash("Enter Magnitude Greate than 4.0")
            return render_template("large_mag.html", post="res")

    if request.method == 'GET':
        return render_template("large_mag.html", post="res")













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


