from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
        'id': 1,
        'name': 'Joseph',
        'age': 28,
        'job_title': 'Web Developer',
        'phone': '0264388686'
    },
    {
        'id': 2,
        'name': 'Daniel',
        'age': 26,
        'job_title': 'Android Developer',
        'phone': '0548179767'
    },
    {
        'id': 3,
        'name': 'Fitzgerrald',
        'age': 27,
        'job_title': 'iOs Developer',
        'phone': '0207598483'
    },
    {
        'id': 4,
        'name': 'Francis Doh',
        'age': 15,
        'job_title': 'Teacher',
        'phone': '0202817112'
    }
]

db = sqlite3.connect('database/y2kdatabase.sqlite')


@app.route('/')
def home():
    return "Welcome to Y2K Api"


@app.route('/developers')
def index():
    return jsonify(data)


@app.route('/developers/<string:username>')
def show(username):
    name = {}
    for obj in data:
        if obj.get('name').lower() == username:
            name = obj

    return jsonify(name)


@app.route('/developers/<int:user_id>')
def find_by_id(user_id):
    name = {}
    for obj in data:
        if obj.get('age') == user_id:
            name = obj

    return jsonify(name)


if __name__ == '__main__':
    app.run()
