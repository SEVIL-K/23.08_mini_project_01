from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.1uqyocz.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/m1')
def m1_page():
    return render_template('m1.html')

@app.route('/m3')
def m3_page():
    return render_template('m3.html')

@app.route("/guestbook_team", methods=["POST"])
def guestbook_team_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.guestbook_team.insert_one(doc)

    return jsonify({'msg': '방명록 댓글 게시 완료'})


@app.route("/guestbook_team", methods=["GET"])
def guestbook_team_get():
    # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
    team_comments = list(db.guestbook_team.find({}, {'_id': False}))
    return jsonify({'result': team_comments})


# ========================= m1 POST, GET============================
@app.route("/guestbook_m1", methods=["POST"])
def guestbook_m1_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.guestbook_m1.insert_one(doc)

    return jsonify({'msg': '방명록 댓글 게시 완료'})


@app.route("/guestbook_m1", methods=["GET"])
def guestbook_m1_get():
    # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
    m1_comments = list(db.guestbook_m1.find({}, {'_id': False}))
    return jsonify({'result': m1_comments})
# ==================================================================

# ========================= m3 POST, GET============================
@app.route('/guestbook_m3', methods=["POST"])
def guestbook_m3_post():
    nickname_receive = request.form['nickname_give']
    emoticon_receive = request.form['emoticon_give']
    comment_receive = request.form['comment_give']
    
    doc = {
        'nickname':nickname_receive,
        'emoticon':emoticon_receive,
        'comment':comment_receive
    }

    db.guestbook_m3.insert_one(doc)

    return jsonify({'msg':'댓글 감사합니다!!!!'})

@app.route("/guestbook_m3", methods=["GET"])
def guestbook_m3_get():
    m3_comments = list(db.guestbook_m3.find({},{'_id':False}))
    return jsonify({'result':m3_comments})
# ==================================================================

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
