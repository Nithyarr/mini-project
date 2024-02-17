from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user


local_server = True
app=Flask(__name__,template_folder='template')
app.secret_key = 'nithya'

login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return Register.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/hms'
db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class Register(UserMixin,db.Model):
    __tablename__="userr"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))


@app.route("/")
def index():
    return render_template('ok.html') 
@app.route("/doctors")
def doctors():
    return render_template('doctors.html') 
@app.route("/paitents")
def paitents():
    return render_template('paitents.html')
@app.route("/booking")
def booking():
    return render_template('booking.html')  
@app.route("/login",methods=['POST','GET']) ##login
def login():
    # if request.method == "POST":
    #     email=request.form.get('email')
    #     password=request.form.get('password')
    #     print(email,password)
    #     user=User.query.filter_by(email=email).first()
    #     if user and check_password_hash(user.password,password):
    #         login_user(user)
    #         print("Login Success","primary")
    #         return render_template('/index')
    #     else:
    #         print("invalid credentials","danger")
    #         return render_template('login.html')
    return render_template('login.html') 
@app.route("/help")
def help():
    return render_template('help.html')   
@app.route("/home")
def logout():
    return render_template('booking.html')  


@app.route("/signin",methods=['POST','GET']) ##signin
def signin():
     if request.method=='POST':
         username=request.form.get('username')
         email=request.form.get('email')
         password=request.form.get('password')
         user=Register.query.filter_by(email=email).first()
         if user:
             print("email already exists")
             return render_template('signin.html')
         hashed_password= generate_password_hash(password)
         new_user=Register(username=username,email=email,password=hashed_password)
         db.session.add(new_user)
         db.session.commit()
         #db.engine.execute(f"INSERT INTO userr (username, email, password) VALUES ('{username}', '{email}', '{password}')")
         return render_template('login.html')
     return render_template('signin.html')
    



@app.route("/test")
def test():
    try:
        Test.query.all()
        return 'my database connect'
    except:
        return 'my db not connect'
    
if __name__=="__main__":
    app.run(debug=True)

