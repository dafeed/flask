from flask import Flask, render_template
#import flask class and render_template function
app = Flask(__name__)
#creates usable instance of the flask class and saves it into app
@app.route("/")
#this tells flask what URL should trigger the function.  When the user types the URL/ it will trigger the index function
def index():
#this names the function index
    return render_template("index.html")
    #this returns the render_template function and loads index.html
#routes the app
if __name__ == "__main__":
    app.run(debug=True)
#if __name__ is __main__ or if we are running the page as the main program, not a module or plugin, __name__ will be __main__ and then it will execute app.run which runs the app on a local server with debug being true, so it will show the errors it runs into