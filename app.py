from flask import Flask, jsonify, request
from flask import render_template, redirect
import json

from os import listdir

TODO_LISTS_FOLDER = 'todo_pages'

app = Flask(__name__)

def get_list():
    return [x.split('.')[0] for x in listdir(TODO_LISTS_FOLDER)]

@app.route('/')
def home_page():
    todo_lists = get_list()

    return render_template('index.html', todo_lists=todo_lists)

@app.route('/create')
def create_todo():
    return render_template('create.html')

@app.route('/todo/<todo_id>')
def todo_page(todo_id):
    todo_lists = get_list()

    if not todo_id in todo_lists:
        message = 'Todo is not found.'
        return render_template('404.html', message=message)


    with open(f'todo_pages/{todo_id}.json', 'r') as file:
        info = json.loads(file.read())


    return render_template('todo.html', todo_id=todo_id, info=info)

@app.route('/get_todo_lists')
def get_todo_lists():
    todo_lists = get_list()
    return jsonify(todo_lists)

@app.route('/createTodoFile', methods=['POST'])
def create_todo_file():
    name = request.form.get('title')
    description = request.form.get('description')

    if name.replace(' ', '').strip() == '':
        message = f'Name: "{name}" can\'t be empty.'
        return render_template('404.html', message=message)

    if name in get_list():
        message = f'This name: "{name}" not unique in todo list.'
        return render_template('404.html', message=message)

    todo = {'name': name, 'description': description}

    with open(f'todo_pages/{name}.json', 'w') as file:
        json.dump(todo, file)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)