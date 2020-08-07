from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from pytz import timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
user_timezone = pytz.timezone('America/Sao_Paulo') #UTC-3
#user_timezone = pytz.timezone('America/Los_Angeles') #UTC-7
utc_timezone = pytz.utc

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	completed = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime(timezone=True), default=datetime.now(tz=pytz.utc))

	def __repr__(self):
		return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		task_content = request.form['content']
		new_task = Todo(content=task_content)

		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue adding your task'

	else:
		tasks = Todo.query.order_by(Todo.date_created).all()
		# print(tasks)
		# print(tasks[0].date_created)
		# print(tasks[0].date_created.replace(tzinfo=utc_timezone))
		# print(tasks[0].date_created.replace(tzinfo=utc_timezone).astimezone(user_timezone))
		return render_template('index.html', tasks=tasks, user_timezone=user_timezone, utc_timezone=utc_timezone)

@app.route('/delete/<int:id>')
def delete(id):
	task_to_delete = Todo.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return 'There was a problem deleting that task.'
	
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	task = Todo.query.get_or_404(id)

	if request.method == 'POST':
		task.content = request.form['content']

		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'There was a problem updating this task.'

	else:		
		return render_template('update.html', task=task)


if __name__ == "__main__":
	app.run(debug=True)