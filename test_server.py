from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        data = {'name': name, 'email': email, 'password': password}
    
        url = f'http://127.0.0.1:9005/register'
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return response.json()
    if request.method == 'GET':
        return render_template('register.html')


@app.route('/', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the username and password match

        data = {'email': email, 'password': password}
        url = f'http://127.0.0.1:9005/login'
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()
    if request.method == 'GET':
        return render_template('login.html')

if __name__ == "__main__":

    app.run(port=9001, debug=True)