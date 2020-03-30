from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def names():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return request.form['name']