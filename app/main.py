from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/contact_me')
    def contact():
        return render_template('contact.html')
    
    @app.route('/todos', methods=['GET', 'POST'])
    def todo():
        if request.method == 'POST':
            task_content = request.form['content']
            if not task_content.strip():
                flash('Task content cannot be empty.', 'error')
            else:
                new_task = Task(content=task_content)
                db.session.add(new_task)
                db.session.commit()
        tasks = Task.query.all()
        return render_template('todo.html', tasks=tasks)


    @app.route('/delete/<int:id>')
    def delete(id):
        task_to_delete = Task.query.get_or_404(id)
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/todos')
        
    @app.route('/complete/<int:id>')
    def complete(id):
        task = Task.query.get_or_404(id)
        task.is_completed = True
        db.session.commit()
        return redirect('/todos')
    
    # @app.route('/todo', methods=['GET', 'POST'])
    # def todo_app():
    #     sort_by = request.args.get('sort', default='id')  # Default sorting by ID
    #     tasks = Task.query.order_by(sort_by).all()
    #     return render_template('todo.html', tasks=tasks)


    @app.route('/update/<int:id>', methods=['GET', 'POST'])
    def update(id):
        task = Task.query.get_or_404(id)
        if request.method == 'POST':
            task.content = request.form['content']
            db.session.commit()
            return redirect('/todos')
        else:
            return render_template('update.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
