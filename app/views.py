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
	print request.form
	global names
	global master_list
	global text
	if "my-form" in request.form:
		text = request.form['students-list']
		names=text.split(',')

		names=[str(item) for item in names]

		# Save a master class list for later
		master_list=names

		temp_student=random.sample(names, 1)[0]

		#Remove current temp student so student won't be chosen twice.
		names.remove(temp_student)
		print names

		return render_template('index.html', studentlist=text, randomstudent=temp_student)
	elif "new-student" in request.form:
		print names
		try:
			temp_student=random.sample(names, 1)[0]

			#Remove current temp student so student won't be chosen twice.
			names.remove(temp_student)

			return render_template('index.html', studentlist=text, randomstudent=temp_student)
		except:
			return render_template('index.html', studentlist=text, randomstudent="No more students!")


