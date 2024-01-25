from flask import Flask, url_for, request

my_app = Flask(__name__)


@my_app.route('/')
def hello_world():
    return 'Hello, World!'

@my_app.route('/add')
def add_user():
    return 'add user'

@my_app.route('/user/<username>')
def show_user_profile(username):
# show the user profile for that user
    return f"User {username}"

@my_app.route('/post/<int:post_id>')
def show_post(post_id):
# show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@my_app.route("/check_method", methods=['GET', 'POST', 'PUT'])
def check_method():
    if request.method == 'POST':
        return "You are using POST"
    elif request.method == 'PUT':
        return "You are using PUT"
    else:
        return "You are probably using GET"

if __name__ == '__main__':
    with my_app.test_request_context():
        print(url_for('hello_world'))
        print(url_for('add_user'))
        print(url_for('show_user_profile', username="test"))
        print(url_for('show_post', post_id=15))

    my_app.run()
