from flask import render_template
from app import app
from flask import request
import random
import numpy as np

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def student_list():
    text = request.form['students-list']
    names=text.split(',')
    print len(names)
    temp_array= np.random.choice(len(names), len(names), replace=False)
    print temp_array
    temp_index=0
    return render_template('index.html', studentlist=text, randomstudent=names[temp_array[temp_index]])

