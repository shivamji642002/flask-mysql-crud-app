from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ji642002@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


# Routes
@app.route('/')
def index():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name, email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", user=user)


@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Create tables if not exists
    with app.app_context():
        db.create_all()
    app.run(debug=True)
