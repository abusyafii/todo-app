from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.column(db.String(100))
    complete = db.column(db.Boolean)

@app.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template("base.html") #, todo_list=todo_list)

if __name__ == "__main__":
#   db.create.all()
#   new_todo = Todo(title="todo 1", complete=False)
#   db.session.add(new_todo)
#   db.session.commit()
    app.run(debug=True)
