from flask import Flask, url_for, request, render_template, redirect
from faker import Faker

app = Flask(__name__)
fake = Faker()


class User:
    __z_index = 0
    def __init__(self, username=None, email=None, age=None):
        self.id = self.__get_next_z_index()
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"User(username={self.username}, email={self.email}, age={self.age})"
    @classmethod
    def __get_next_z_index(cls):
        cls.__z_index += 1
        return cls.__z_index


USERS = [
    User(
        username=fake.user_name(),
        email=fake.email(),
        age=fake.random_int(min=18, max=80),
    )
    for _ in range(10)
]


@app.route("/")
def index():
    return render_template("index.html", users=USERS)


@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("user/add.html")
    user = User()
    user.username = request.form["username"]
    user.email = request.form["email"]
    user.age = request.form["age"]
    USERS.append(user)
    return redirect(url_for("index"))

@app.route("/user/delete/<int:user_id>")
def delete_user(user_id):
    global USERS
    USERS = [u for u in USERS if  not u.id == user_id]
  
    return redirect(url_for("index"))


my_app = Flask(__name__)
if __name__ == "__main__":
    app.run()
