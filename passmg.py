from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='final'

mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["POST","GET"])
def login():
    msg=''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username,password))
        user = cur.fetchone()
        if user:
            #session['mailid'] = user['email']
            #session['username'] = user['name']
            # return 'Logged in successfully!'
            return redirect(url_for('home'))
        else:
            return 'Incorrect username/password!'
    return render_template('login.html')

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=='POST':
        userdetails=request.form
        username=userdetails['username']
        password=userdetails['password']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users(username,password) VALUES(%s,%s)",(username,password))
        mysql.connection.commit()
        cur.close()
        return 'YOU ARE SUCCESSFULLY REGISTERED !'
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/apply',methods=["POST","GET"])
def apply():
    if request.method=='POST':
        userdetails=request.form
        Applicationid=userdetails['applicationid']
        Firstname=userdetails['firstname']
        Lastname=userdetails['lastname']
        Fathername=userdetails['fathername']
        Gender=userdetails['gender']
        DOB=userdetails['dateofbirth']
        Age=userdetails['age']
        Qualification=userdetails['education']
        RELIGION=userdetails['religion']
        MaritalStatus=userdetails['maritalstatus']
        Nationality=userdetails['nationality']
        AADHAARNumber=userdetails['aadhar']
        PANNumber=userdetails['pan']
        Email=userdetails['mailid']
        PhoneNumber=userdetails['phoneno']
        Address=userdetails['address']
        Pincode=userdetails['pincode']
        Passporttype=userdetails['passporttype']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO applicant(Applicationid,Firstname,Lastname,Fathername,Gender,DOB,Age,Qualification,RELIGION,MaritalStatus,Nationality,AADHAARNumber,PANNumber,Email,PhoneNumber,Address,Pincode,Passporttype) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Applicationid,Firstname,Lastname,Fathername,Gender,DOB,Age,Qualification,RELIGION,MaritalStatus,Nationality,AADHAARNumber,PANNumber,Email,PhoneNumber,Address,Pincode,Passporttype))
        mysql.connection.commit()
        cur.close()
        return 'YOU ARE SUCCESSFULLY REGISTERED !'
    return render_template('apply.html')
#display
@app.route('/display',methods=["POST","GET"])
def display():
    if request.method=='POST':
        userdetails=request.form
        applicationid=userdetails['applicationid']
        cur = mysql.connection.cursor()
        result=cur.execute("SELECT * FROM applicant WHERE Applicationid= %s",(applicationid))
        if result>0:
            user_detail=cur.fetchone()
            return render_template('check.html',detail=user_detail)
    return render_template('display.html')

if __name__=='__main__':
    app.run(debug=True)