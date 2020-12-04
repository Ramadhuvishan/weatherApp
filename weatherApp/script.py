from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/report',methods=['POST'])
def report():
    cn = request.form['cityName']
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=7fd6991c6458f733cddc430437c3c106&units=metric'.format(cn)
    res = requests.get(url)
    data = res.json()
    return render_template('result.html',result = data)

@app.route('/front')
def front():
    return redirect('front.html')

if __name__ == '__main__':
    app.run(debug = True)
