from flask import render_template
from app import app
from flask import request
import random

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def student_list():
    text = request.form['students-list']
    names=text.split(',')
    print len(names)
    temp_index=random.randint(0, len(names)-1)
    print names[temp_index]
    return render_template('index.html', studentlist=text, randomstudent=names[temp_index])

