from flask import Flask, render_template, request, redirect
import quandl
from datetime import datetime, timedelta
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

import os
cdir = os.getcwd()

app = Flask(__name__)
quandl.ApiConfig.api_key = 'uZNGc2dnuL7QmecmpzBx'
# quandl.ApiConfig.api_key = os.ENVIRON['QUANDL_KEY']

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('question.html')

@app.route('/show', methods=['POST'])
def show():
    stock = request.form['stock']   
    now = datetime.now().strftime("%Y-%m-%d")
    past = (datetime.now() + timedelta(days = -30)).strftime("%Y-%m-%d")
    data = quandl.get("WIKI/" + stock + ".4", start_date=past, end_date=now)
    Y = [p for p in data['Close']]
    X = range(len(Y))

    p = figure(title="Stock last month", x_axis_label='time', y_axis_label='value')
    p.line(X, Y, line_width=2)
    script, div = components(p)

    return render_template('graph.html', script = script, div = div)

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    #app.run(port=33507)
    app.run()
