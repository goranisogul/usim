from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.projectname


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/db', methods=['GET'])
def show_db():
    data = list(db.table.find({}, {'_id': False}))
    return jsonify({'all_data': data})


@app.route('/db', methods=['POST'])
def save_db():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    doc = {
        'title': title_receive,
        'content': content_receive
    }

    db.table.insert_one(doc)

    return jsonify({'msg': '저장완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
