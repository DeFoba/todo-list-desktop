from flask import Flask, jsonify
from flask import render_template

from os import listdir

TODO_LISTS_FOLDER = 'todo_pages'

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/todo/<todo_id>')
def todo_page(todo_id):
    return render_template('todo.html', todo_id=todo_id)

@app.route('/get_todo_lists')
def get_todo_lists():
    todo_lists = [x.split('.')[0] for x in listdir(TODO_LISTS_FOLDER)]
    return jsonify(todo_lists)

if __name__ == '__main__':
    app.run(debug=True)