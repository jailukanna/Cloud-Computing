# This is Assignment 3
import random
from flask import Flask, render_template, request, flash
import os
import csv
import pymysql
import time
import hashlib
import redis
import pickle



# Flask object
app = Flask(__name__)  # flask use this (__name__ ) argument to determine location of application

# Upload folder
UPLOAD_FOLDER = 'static/'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
app.secret_key = "AimanAj1987!@"


# this is Db Connection
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
    print("No Connection to DataBase ^_^")



 # this is Redis Connection
try:

    password1 = 'xLJPkQpges+XL884lic+GOJvF008rB0F5noRvWowAXk='
    database1 = 'cloud_db_6331'
    servhoster1 = 'aiman.redis.cache.windows.net'
    redis_connection = redis.StrictRedis(host=servhoster1, password=password1, db=0, port='6379', ssl = False)


except:
    flash("No Connection to Redis Cache ^_^")
    print("No Connection to Redis Cache ^_^")





# this Function will Delete Exist Table.
def drop_table():
    cursor.execute('DROP TABLE IF EXISTS assignment3earthquick')



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






# uploaded CSV file And Calculate Time to Create Table
file_path =''
@app.route("/home", methods=['POST','GET'])
def uploadFile():

    # get the uploaded file
    uploaded_file1 = request.files['file1']
    if uploaded_file1.filename != '':
        file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file1.filename)
        arr = file_path1.split('.')
        sub_string = arr[1]
        if sub_string == 'csv':
            uploaded_file1.save(file_path1)
            # Drop table if Exist
            drop_table()
            start = time.time()
            with open(file_path1, 'rt', encoding='Latin-1') as csvfile:
                reader = csv.reader(csvfile, quotechar='`')
                head = next(reader)

            sql = "create table if not exists assignment3earthquick("
            for i in range(0, len(head) - 1):
                sql += head[i] + " varchar(100), "
            sql += head[len(head) - 1] + " varchar(100))"
            cursor.execute(sql)
            end = time.time()
            get_all_data = """LOAD DATA LOCAL INFILE '{}'
                INTO TABLE assignment3earthquick FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;""".format(file_path1)

            cursor.execute(get_all_data)
            cnx.commit()
            total_time = end - start

            return render_template('main.html', total_time = total_time)

        else:
            flash("Only CSV file allowed")
            return render_template('home.html')

    else:
        return render_template('home.html')






# To Do random Query and show How much Time it Take Witout Cache
@app.route('/randomQuery', methods=['POST', 'GET'])
def search_magnitude():
    if request.method == 'POST':
        query = request.form['randomQuery']
        value = int(query)
        start_time = time.time()
        if value <= 1000:
            for i in range(0, value):
                mag = random.uniform(-1.27, 8)
                mag = str("{0:.2f}".format(mag))
                sql = "select * from cloud_db_6331.assignment3earthquick where mag =" + mag
                cursor.execute(sql)
            end_time = time.time()
            total_time = end_time - start_time
            return render_template('randomQuery.html', total_time=total_time, max_number =value)
        else:
            flash("Enter only Values Up to 1000")
            return render_template('randomQuery.html')
    if request.method == 'GET':
            return render_template('randomQuery.html')

    else:
        return render_template('main.html')



# To Do random Query using Redis Cache
@app.route('/memory_cache_randomQuery', methods=['POST', 'GET'])
def search_memory_cache():
    if request.method == 'POST':
        magnitude = request.form['randomQuery']
        value = int(magnitude)
        if value <= 1000:
                start_time = time.time()
                for i in range(0, value):
                    mag = random.uniform(-1.27, 8)
                    mag = str("{0:.2f}".format(mag))
                    sql = "select * from cloud_db_6331.assignment3earthquick where mag =" + mag
                    hash = hashlib.sha224(sql.encode('utf-8')).hexdigest()
                    key = "redis_cache:" + hash
                if (redis_connection.get(key)):
                    print("redis cached")
                else:
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    rows = []
                    for dataa in data:
                        rows.append(str(dataa))
                    redis_connection.set(key, pickle.dumps(list(rows)))
                    cursor.execute(sql)

                end_time = time.time()
                total_time = end_time - start_time
                return render_template('memory_cache_randomQuery.html', total_time=total_time, max_number =value)
        else:
            flash("Enter only Values Up to 1000")
            return render_template('memory_cache_randomQuery.html')
    if request.method == 'GET':
            return render_template('memory_cache_randomQuery.html')

    else:
        return render_template('main.html')







# To Do Restricted random Query and show How much Time it Take Witout Cache
@app.route('/restrictedQuery', methods=['POST', 'GET'])
def search_restrictedQuery():
    if request.method == 'POST':
        restrictedQuery = request.form['restrictedQuery']
        mag1 = request.form['mag1']
        mag2 = request.form['mag2']
        mag11 = str(mag1)
        mag22 = str(mag2)
        start_time = time.time()
        value = int(restrictedQuery)
        if value <= 1000:
            for i in range(0, value):
                mag = random.uniform(-1.27, 8)
                mag = str("{0:.2f}".format(mag))

                sql = "select * from cloud_db_6331.assignment3earthquick where mag =" + mag + "AND mag between {} AND {}".format(mag11, mag22)
                cursor.execute(sql)
            end_time = time.time()
            total_time = end_time - start_time
            return render_template('restrictedQuery.html', total_time=total_time, MAG1 =mag1 , MAG2 =mag2)
        else:
            flash("Enter only Values Up to 1000")
            return render_template('restrictedQuery.html')
    if request.method == 'GET':
            return render_template('restrictedQuery.html')

    else:
        return render_template('main.html')





# To Do Restricted random Query Using Redis Cache
@app.route('/memory_chach_restrictedQuery', methods=['POST', 'GET'])
def search_memory_chach_restrictedQuery():
    if request.method == 'POST':
        restrictedQuery = request.form['chach_restrictedQuery']
        mag1 = request.form['mag1']
        mag2 = request.form['mag2']
        mag11 = str(mag1)
        mag22 = str(mag2)
        value = int(restrictedQuery)
        if value <= 1000:
            start_time = time.time()
            for i in range(0, value):
                mag = random.uniform(-1.27, 8)
                mag = str("{0:.2f}".format(mag))

                sql = "select * from cloud_db_6331.assignment3earthquick where mag =" + mag + "AND mag between {} AND {}".format(mag11, mag22)
                hash = hashlib.sha224(sql.encode('utf-8')).hexdigest()
                key = "redis_cache:" + hash
            if (redis_connection.get(key)):
                print("redis cached")
            else:
                cursor.execute(sql)
                data = cursor.fetchall()
                rows = []
                for dataa in data:
                    rows.append(str(dataa))
                redis_connection.set(key, pickle.dumps(list(rows)))
                cursor.execute(sql)

            end_time = time.time()
            total_time = end_time - start_time
            return render_template('memory_chach_restrictedQuery.html', total_time=total_time, MAG1 =mag1 , MAG2 =mag2)
        else:
            flash("Enter only Values Up to 1000")
            return render_template('memory_chach_restrictedQuery.html')
    if request.method == 'GET':
            return render_template('memory_chach_restrictedQuery.html')

    else:
        return render_template('main.html')












if __name__ == "__main__":

    app.run( debug=True)










