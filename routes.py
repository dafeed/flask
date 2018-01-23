from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User  #this imports the db object from models.py
#import flask class and render_template function
from forms import SignupForm, LoginForm #importants SignupForm from forms.py
app = Flask(__name__)
#creates usable instance of the flask class and saves it into app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:abc123@localhost/flask'
db.init_app(app) #this intializes db to be ran in app

app.secret_key = "development-key" #this protects against cross site scripting

@app.route("/")
#this tells flask what URL should trigger the function.  When the user types the URL/ it will trigger the index function
def index():
#this names the function index
    return render_template("index.html")
    #this returns the render_template function and loads index.html
#routes the app

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=['GET', 'POST']) #this allows get and post methods to be used.  get request is when the form is being displayed, post is when it's been submitted
def signup():
    if 'email' in session:
        return redirect(url_for('home'))
    
    form = SignupForm() #stores the signup form in the var form
    
    if request.method == 'POST':
        if form.validate() == False:
            return render_template("signup.html", form=form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            
            session['email'] = newuser.email #creates a new session when a users signs up for an account
            return redirect(url_for('home'))
    
    elif request.method == 'GET':
        return render_template("signup.html", form=form) #this sends the form to a html page called signup.html

@app.route("/login", methods=["GET", "POST"])
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    
    form = LoginForm()    
    if request.method == "POST":
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user is not None or user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else: 
                return redirect(url_for('login'))
    elif request.method == 'GET': 
        return render_template('login.html', form=form)
    
@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))
    
@app.route("/home")
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    return render_template('home.html')
    
if __name__ == "__main__":
    app.run(debug=True)
#if __name__ is __main__ or if we are running the page as the main program, not a module or plugin, __name__ will be __main__ and then it will execute app.run which runs the app on a local server with debug being true, so it will show the errors it runs into