from flask import *
import pymysql
app=Flask(__name__)
# home page
@app.route('/')
def home():
    return render_template('index.html')

# signuppage
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method=='POST':
       

        # we are receiving information from the form 
        username=request.form['username']
        password=request.form['password']
        phonenumber=request.form['phonenumber']
        confirm=request.form['confirm_password']

        email=request.form['email']
        image=request.files['image']
        
        image.save('static/images/' + image.filename)

        if password !=confirm:
            return render_template('signup.html',error='Password dont match')
        else:
        # get data from the form
          connection = pymysql.connect(host='localhost', user='root', password='', database='mpesatestdb')

                                   

        # define the sql query
        sql = "insert into register(username,password,phonenumber,email,image) values (%s,%s,%s,%s,%s)"
        # create the cursor
        cursor=connection.cursor()
        # execute the sql

        data=(username,password,phonenumber,email,image.filename) 
        cursor.execute(sql,data)


        # commit the changes in the database

        connection.commit()
        return render_template('signup.html',success='Saved successfully')

    else:
         return render_template('signup.html')


# run the application


# read data from the database:login,display info
@app.route('/display')
def display():
     connection = pymysql.connect(host='localhost', user='root', password='', database='mpesatestdb')
     cursor=connection.cursor()
     sql="select * from register"
     cursor.execute(sql)

     count=cursor.rowcount
     if count==0:
         return render_template('display.html',message='No data available')
     else:
         data=cursor.fetchall()
         return render_template('display.html',records=data)
         


    

app.run(debug=True)