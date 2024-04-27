from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from const import FLAG, CRENDENTIALS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{CRENDENTIALS}@db:5432/application'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form['username']
    password = request.form['password']

    if username != 'admin' or password[:5] != 'admin' or password[-5:] != 'admin':
        return 'Login failed. Please check your username and password.'


    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    user = db.session.execute(db.text(query)).fetchone()

    if user:
        return 'Hello admin ' + FLAG
    else:
        return 'Login failed. Please check your username and password.'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
