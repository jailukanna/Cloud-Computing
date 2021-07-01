# nltk.download()     This line use to download package of All Stop words

import os
from flask import Flask, render_template,request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.stem import PorterStemmer  # Use to Steam TXT ( like cats -> cat )
import re

#from colorama import init   # Use to color Text
#init()
from colorama import Fore, Back, Style



app = Flask(__name__)

ps = PorterStemmer()


# To Preprocessing files
def convertFiles():

    for i in os.listdir('static/inputFiles'):
        # Read & Write to Same time
        file_path ='static/inputFiles/{}'.format(i)
        write_file_path ='newFiles/{}'.format(i)

        readFile= open(file_path, encoding="utf8")
        stop_words = set(stopwords.words('english'))


        for line in readFile:

            #allTXT = ' '.join([ps.stem(w.lower()) for w in word_tokenize(line)])  # Convert to Lower case & Steam Words like parts -> part
            allTXT = ' '.join([w.lower() for w in word_tokenize(line)])  # Convert to Lower case then return it as string
            cleanString = re.sub('\W+', ' ', allTXT) # Remove all Special Chars

            allTXT1 = ''.join(c for c in cleanString if not c.isdigit())  # Remove any number
            allTXT2 = ''.join(c for c in allTXT1 if c not in punctuation)  # Remove any punctuation
            word_tokens = word_tokenize(allTXT2)
            allTXT3 = [w for w in word_tokens if w not in stop_words]   # Remove any Stop Words
            new_allTXT = " ".join(allTXT3)
            writeFile = open(write_file_path, 'a', encoding="utf8")
            writeFile.write(new_allTXT + "\n")
            writeFile.close()
    readFile.close()










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



# Read one Word & String from USER
@app.route("/word", methods=['POST','GET'])
def uploadFile():
            line_numer_places = list()
            line_have_word = list()
            words_position = list()
            book_name = list()

            if request.method == 'POST':
                word = str(request.form['word'])
                for books in os.listdir('newFiles'):
                    file = open('newFiles/{}'.format(books), encoding="utf8")  # Search in ALL  Files
                    count_lines = 0
                    for line in file:
                        count_lines =count_lines+1
                        if word in line:
                            word_position =0
                            word_offset = line.strip().split(' ') # List of words of  Line

                            for offset in word_offset:
                                word_position = word_position+1
                                if offset == word:
                                    words_position.append(word_position)
                                    line_have_word.append(line)
                                    line_numer_places.append(count_lines)
                                    book_name.append(books.split('.')[0])
                                    #break
                                else:
                                    continue



                    file.close()


                all_list = zip(book_name, line_numer_places, line_have_word ,words_position)  # Zip TO COLLECT ALL LISTS TO ONE BIG LIST


                return render_template('word.html',all_list =all_list, word =word)

            else:
                return render_template('word.html')







# Read one Word & String from USER
@app.route("/string", methods=['POST','GET'])
def combination():

            line_numer_places = list()
            line_have_word = list()
            book_name = list()

            if request.method == 'POST':
                word1 = str(request.form['word1'])

                for books in os.listdir('newFiles'):
                    file = open('newFiles/{}'.format(books), encoding="utf8")  # Search in ALL  Files
                    count_lines = 0
                    for line in file:
                        count_lines =count_lines+1
                        if word1 in line:
                            line_have_word.append(line)
                            line_numer_places.append(count_lines)
                            book_name.append(books.split('.')[0])
                    file.close()

                all_list = zip(book_name, line_numer_places, line_have_word)  # Zip TO COLLECT ALL LISTS TO ONE BIG LIST


                return render_template('string.html',all_list=all_list, word1=word1)

            if request.method == 'GET':
                return render_template('string.html')










if __name__ == "__main__":

    #convertFiles()

    app.run()










