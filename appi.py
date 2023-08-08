from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index1.html')

## API 역할을 하는 부분
@app.route('/record', methods=['POST'])
def write_record():
        guest_receive = request.form['guest_give']
        record_receive = request.form['record_give']

        doc = {
            'guest': guest_receive,
            'record': record_receive
        }

        db.file.insert_one(doc)

        return jsonify({'msg': '방명록이 등록되었습니다.'})


@app.route('/record', methods=['GET'])
def read_records():
        records = list(db.file.find({}, {'_id': False}))
        return jsonify({'all_records': records})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)




