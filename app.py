# This is the main file which our app run from here

from flask import Flask, render_template, request, redirect, flash
import os
import sqlite3
import csv



# Flask object
app = Flask(__name__)  # flask use this (__name__ ) argument to determine location of application

# Upload folder
UPLOAD_FOLDER = 'static/csv'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

# upload image
UPLOAD_IMAGES = 'static/images'
app.config['UPLOAD_IMAGES'] =  UPLOAD_IMAGES

app.secret_key = "AimanAj1987!@"



connection =sqlite3.connect('aiman.db', check_same_thread=False)
cursor = connection.cursor()


# this Function will Delete Exist Table Otherwise Create new one
def create_table():
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, name TEXT, nsize TEXT, distance TEXT, author TEXT, pitcure TEXT, keyword TEXT)')










# Root URL Upload CSV
@app.route('/')
def upload_page():
    return render_template('UploadCSV.html')





# This use to search for a Room number and return result to Same page
@app.route('/search', methods=['POST', 'GET'])
def search_room():

    if request.method == 'POST':
        room = request.form['name']
        cursor.execute("SELECT * FROM users WHERE room=?", (room, ))
        current_data = cursor.fetchone()
        if current_data :
            return render_template('search.html', post=current_data)

        else:
            flash("Record Not Found")
            return render_template('search.html',post="")


    if request.method =='GET':
       # cursor.execute("SELECT * FROM users WHERE room=?", (room,))
      #  current_data = cursor.fetchone()
        return render_template('search.html',post="current_data")

    else:
        flash("Record Not Found")
        return render_template('Homepage.html')





# This use to search for a Name  and return result to Same page
@app.route('/search_name', methods=['POST', 'GET'])
def search_name():
    if request.method == 'POST':
        name = request.form['name']
        cursor.execute("SELECT * FROM users WHERE name=?", (name,))
        current_data = cursor.fetchone()

        if current_data:
            return render_template('search_name.html', post=current_data)

        else:
            flash("Record Not Found")
            return render_template('search_name.html', post="")

    if request.method == 'GET':

        #cursor.execute("SELECT * FROM users WHERE room=?", (room,))
        #current_data = cursor.fetchone()
        return render_template('search_name.html', post="current_data")

    else:
        flash("Record Not Found")
        return render_template('Homepage.html')










# uploaded CSV file
file_path =''
@app.route("/UploadCSV", methods=['POST','GET'])
def uploadFile():

      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
           arr = file_path.split('.')
           sub_string = arr[1]
           if sub_string == 'csv': 
                uploaded_file.save(file_path)
                parseCSV(file_path)
            
                cursor.execute('select * from users')
                current_data = cursor.fetchall()
               
                return render_template('Homepage.html', post = current_data)

           else:
                    flash("Only CSV file allowed")
                    return render_template('UploadCSV.html')

      else:
          return render_template('UploadCSV.html')


# Read Data From CSV file
def parseCSV(file_path):
    with open(file_path,'r') as file:
        has_header = csv.Sniffer().has_header(file.read())
        file.seek(0)
        reader = csv.reader(file)
        if has_header:
            next(reader)
            
            for row in file:
                list=  row.strip().split(',')
                name = list[0]
                nsize = list[1]
                distance = list[2]
                author = list[3]
                pitcure = list[4]
                keyword =list[5]

                cursor.execute("INSERT INTO users (name, nsize, distance, author, pitcure, keyword ) VALUES (?, ?, ?, ?, ?, ?)", (name, nsize, distance, author, pitcure, keyword))
                connection.commit()
 



# Upload Images
@app.route("/uploadimage/<int:id>", methods=['POST','GET'])
def uploadimage(id):
      # get the uploaded file
      if request.method == 'POST':
            flag = True
            uploaded_image = request.files['image']
            if uploaded_image.filename != '':
                file_path = os.path.join(app.config['UPLOAD_IMAGES'], uploaded_image.filename)
                folder = 'static/images'
                arr = file_path.split('.')
                sub_string = arr[1]
                if sub_string != 'txt' and sub_string != 'csv':

                    for filename in os.listdir(folder):
                        file_path = os.path.join(folder, filename)
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            cursor.execute('SELECT pitcure FROM users')
                            current_data = cursor.fetchall()
                            for i in current_data:
                                if uploaded_image.filename == i[0]:
                                    flash(" Image already exist use different Image")
                                    cursor.execute('SELECT * FROM users')
                                    current_data = cursor.fetchall()
                                    return render_template('Homepage.html', post=current_data)
                                    flag = False
                                    break
                                else:
                               #file_path = os.path.join(app.config['UPLOAD_IMAGES'], uploaded_image.filename)

                                    # Save the file path
                                    uploaded_image.save(file_path)
                                    update_query = """Update users SET pitcure=?  where id = ?"""
                                    data2 = (uploaded_image.filename)
                                    data = (data2, id)
                                    cursor.execute(update_query, data)
                                    #connection.commit()
                                    # save the file
                                    flash("Image upload Successfully")
                                    cursor.execute('SELECT * FROM users')
                                    current_data = cursor.fetchall()
                                    return render_template('Homepage.html', post=current_data)
                            if flag ==False:
                                break
                else:
                    flash("Only Image file allowed")
                    cursor.execute('SELECT * FROM users')
                    current_data = cursor.fetchall()
                    return render_template('Homepage.html', post=current_data)

# To showw all Images
      if request.method == 'GET':
          sql_query = """select * from users where id = ?"""
          cursor.execute(sql_query, (id,))
          records = cursor.fetchone()
          return render_template('uploadimage.html', post=records)
      else:
          return render_template('Homepage.html')









# this function will delete one Record by its ID number
@app.route('/Homepage/<int:id>')
def delete_record(id):

    query = """DELETE from users where id = ?"""
    cursor.execute(query, (id,))
    #connection.commit()
    cursor.execute('select * from users')
    current_data = cursor.fetchall()
    return render_template('Homepage.html', post=current_data)








# will Update data in DB by ID then store back to DB
@app.route('/update/<int:id>', methods=['POST','GET'])
def edit_record(id):
    if request.method == 'POST':

            name = request.form['name']
            state = request.form['state']
            salary = request.form['Salary']
            grade = request.form['grade']
            room = request.form['room']
            telephone = request.form['telephone']
            keywords = request.form['keyword']
            update_query = """Update users SET name = ?, state = ?, salary = ?, grade = ?, room = ?, telephone = ?, keyword = ?  where id = ?"""
            data = (name, state, salary, grade, room, telephone, keywords,id )
            cursor.execute(update_query, data)
            #connection.commit()
            cursor.execute('SELECT * FROM users')
            current_data = cursor.fetchall()
            return render_template('Homepage.html', post=current_data)

    if request.method == 'GET':
        sql_query = """select * from users where id = ?"""
        cursor.execute(sql_query, (id,))
        records = cursor.fetchone()
        print(records)
        return render_template('update.html', post=records)
    else:
        return render_template('Homepage.html')






# Nav Home to return user to HomePage
@app.route('/Homepage')
def redirect_homepage():
    cursor.execute('SELECT * FROM users')
    current_data = cursor.fetchall()
    return render_template('Homepage.html', post=current_data)



# Show Gallery Page
@app.route('/gallery', methods=['GET', 'POST'])
def print_pictures():
    if request.method == 'POST':
        grade1 = request.form['grade1']
        grade2 = request.form['grade2']
        cursor.execute("SELECT * FROM users WHERE grade BETWEEN ? AND ?", (grade1, grade2, ))

        current_data = cursor.fetchall()
        print(current_data)
        return render_template('gallery.html', post=current_data)

    if  request.method == 'GET':
        #cursor.execute('SELECT * FROM users')
        #current_data = cursor.fetchall()
        return render_template('gallery.html', post="current_data")











# TO print All names of Images
@app.route('/name_image', methods= ['POST', 'GET'])
def name_image():
    if request.method == 'POST':
        uploaded_image = request.files['image']
        if uploaded_image.filename != '':
            file_path = os.path.join(app.config['UPLOAD_IMAGES'], uploaded_image.filename)
            arr = file_path.split('.')
            sub_string = arr[1]
            if sub_string != 'txt' and sub_string != 'csv':
                # Save the file path
                uploaded_image.save(file_path)
                cursor.execute("INSERT INTO users (pitcure) VALUES (?)", (file_path))
                connection.commit()
                # save the file

                cursor.execute('SELECT name , pitcure FROM users')
                current_data = cursor.fetchall()
                return render_template('name_image.html', post=current_data)


            else:
                flash("Only Image file allowed")
                cursor.execute('SELECT * FROM users')
                current_data = cursor.fetchall()
                return render_template('Homepage.html', post=current_data)

    # To showw all Images
    if request.method == 'GET':
        # sql_query = """select * from users"""
        # cursor.execute(sql_query)
        # records = cursor.fetchall()
        return render_template('name_image.html', post="records")
    else:
        return render_template('Homepage.html')
























if __name__ == "__main__":
    create_table()
    app.run( debug=True)


