from flask import Flask, request, render_template
# import csv to read data file
import csv
# import pandas to interpret data file
import pandas as pd
# import scripts
import data_analysis as analysis

app = Flask(__name__)

# add url or reference to data file
data_file = "./data/names.csv"

# import scripts from jupyter notebook file
#baby_names = pd.read_csv(data_file)

@app.route('/', methods=['GET', 'POST'])
def names():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return render_template('return.html', tables=analysis.export(data_file))