from flask import Flask, request, render_template
import csv

app = Flask(__name__)

# add url or reference to data file
data_file = "./data/names.csv"

@app.route('/', methods=['GET', 'POST'])
def names():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return names