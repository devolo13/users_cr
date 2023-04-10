from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)


@app.route("/")
def show_users():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)


@app.route('/add_user', methods=['POST'])
def create_user():
    # create database entry
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.save(data)
    return redirect('/')


@app.route('/create')
def create_page():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
