from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)

db.create_table()

@app.route('/')
def index():
    try:
        tasks = db.select_all()
        if tasks is None:
            tasks = []
        return render_template('index.html', tasks=tasks)
    except Exception as e:
        return f"Ошибка: {e}"


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    priority = request.form['priority']
    if title and priority.isdigit():
        db.insert(title, int(priority))
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    if request.method == 'POST':
        title = request.form['title']
        priority = request.form['priority']
        if title and priority.isdigit():
            db.update(id, title, int(priority))
        return redirect(url_for('index'))
    else:
        task = db.select(id)
        return render_template('edit.html', task=task)


@app.route('/delete/<int:id>')
def delete_task(id):
    db.delete(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
