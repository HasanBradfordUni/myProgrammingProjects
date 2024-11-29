from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

#method to update an existing task
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id] = request.form.get('task')
    return redirect(url_for('index'))

#method to clear all tasks
@app.route('/clear', methods=['POST'])
def clear_tasks():
    tasks.clear()   
    return redirect(url_for('index'))

#method to sort tasks in ascending order
@app.route('/sort/ascending', methods=['POST'])
def sort_ascending():
    tasks.sort()
    return redirect(url_for('index'))

#method to sort tasks in descending order
@app.route('/sort/descending', methods=['POST'])
def sort_descending():
    tasks.sort(reverse=True)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run("localhost", 6922)