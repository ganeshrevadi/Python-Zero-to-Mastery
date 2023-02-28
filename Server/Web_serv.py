from flask import Flask ,render_template
app = Flask(__name__)
print(__name__)

@app.route('/<username>')
def hello_world(username = None):
    return render_template('about.html', name = username)

@app.route('/blog')
def blog():
    return "This is my blog!"