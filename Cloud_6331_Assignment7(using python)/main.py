

from flask import Flask, render_template,request,redirect,url_for,jsonify




app = Flask(__name__)
app.secret_key = "AimanAj1987!@"

@app.route('/')
def index():
    return redirect("/home")




# Redirect USER From Home page to same page
@app.route('/')
def redirect_homepage():
    return redirect("/home")


# Redirect to stopApp
@app.route('/stopApp')
def stopApp():
    return render_template('stopApp.html')




# ============================================ APP START FROM HERE ===================================#


teacher_question = ''
student_answer = ''

total_grade = 0
average=0
currentGrade =0

teacherName = ''
studentName = ''
adminName = ''

total_questions = list()
total_answers = list()


allGrades = list()

timer=0

need_help_option =''
admin_hint =''



@app.route('/home', methods=['POST','GET'])
def redirect_TO_mainPage():
        global teacherName
        global studentName
        global adminName

        if request.method =='POST':

            name = str(request.form['name'])
            select =  request.form['select']

            if select == 'Teacher':
                teacherName= name
                return redirect(url_for('teacher'))




            if select == 'Student':
                studentName =name
                return redirect(url_for('student'))




            if select == 'Admin':
               adminName =name
               return redirect(url_for('admin', num=0))





        else:
            return render_template('home.html')






# Teacher Operations
@app.route('/teacher', methods=['POST','GET'])
def teacher():

    global total_grade
    global average
    global teacher_question
    global currentGrade

    if request.method == 'POST':
        if request.form['submit'] == 'form1':
            question = str(request.form['question'])
            teacher_question = question
            total_questions.append(teacher_question)


    if student_answer != '':
        if request.method == 'POST':
            if request.form['submit'] == 'form2':
                currentGrade = int(request.form['grade'])
                total_grade = total_grade+currentGrade
                allGrades.append(currentGrade)
                average = total_grade / len(allGrades)


    return render_template('teacher.html', student_name=studentName, teacher_name=teacherName,
                                   student_answer=student_answer,num=timer)






#======================================== =================================================#

# Student Operations
@app.route('/student', methods=['POST','GET'])
def student():
    global need_help_option
    global student_answer

    if request.method == 'POST':

        if request.form['submit'] == 'form1':
                answer = str(request.form['answer'])
                student_answer = answer
                total_answers.append(student_answer)
        if request.form['submit'] == 'form2':
                    option = request.form['option']
                    need_help_option = option



    return render_template('student.html', student_name=studentName, teacher_name=teacherName,
                           teacher_question=teacher_question,
                           currentGrade=currentGrade, total_grade=total_grade, average=average,
                           num=timer,admin_hint=admin_hint)



#======================================== =================================================#

# Admin Operations

@app.route('/admin<int:num>', methods=['POST','GET'])
def admin(num):
    global timer
    timer = num * 60
    admin_infor =''

    admin_infor = zip(total_questions,total_answers)
    return render_template('admin.html',admin_infor=admin_infor,num=timer)





# THIS FOR HINT PAGE
@app.route('/hint', methods=['POST','GET'])
def hint():
    global admin_hint

    if request.method =='POST':
        admin_hint = request.form['answer']


    return render_template('hint.html',teacher_question=teacher_question,need_help_option=need_help_option)








# Stop And Delete All Informations
@app.route('/stopApp',methods=['POST','GET'])
def kill_app():
    global teacher_question
    global student_answer
    global total_grade
    global average
    global currentGrade
    global teacherName
    global studentName
    global adminName
    global total_questions
    global total_answers
    global allGrades
    global timer
    global admin_hint
    if request.method =='POST':
        kill = str(request.form['kill']).lower()
        if kill =='yes':
            teacher_question = ''
            student_answer = ''
            admin_hint =''
            total_grade = 0
            average = 0
            currentGrade = 0
            timer =0

            teacherName = ''
            studentName = ''
            adminName = ''

            total_questions = list()
            total_answers = list()
            allGrades = list()

            return redirect("/home")

    return redirect("/stopApp")






if __name__ == "__main__":
    app.run()










