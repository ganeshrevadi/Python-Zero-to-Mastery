from flask import Flask ,render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return "This is my blog!"