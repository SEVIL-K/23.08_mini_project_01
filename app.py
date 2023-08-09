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
# ======조호진 추가입니다.=============
@app.route('/m4')
def m4_page():
   return render_template('m4.html')
# ===========================================

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

# ===================조호진 추가입니다===================
@app.route("/guestbook_m4", methods=["POST"])
def guestbook_m4_post():
    visitor_name4_receive = request.form['visitor_name4_give']
    visitor_comment4_receive = request.form['visitor_comment4_give']
    star_receive = request.form['star_give']
    # 혹시나 겹칠까봐 visitor_name4 이런식으로 바꿨습니다.. star는 아직 못바꿨습니다..
    doc = {
            'visitor_name4': visitor_name4_receive,
            'visitor_comment4' : visitor_comment4_receive,
            'star':star_receive
    }
    # visitor 대신 이제 guestbook_m4로 바꿈
    db.guestbook_m4.insert_one(doc)
    return jsonify({'msg': '저장 완료'})

@app.route("/guestbook_m4", methods=["GET"])
def guestbook_m4_get():
    #  여기도
    all_comments = list(db.guestbook_m4.find({},{'_id':False}))
    return jsonify({'result': all_comments})
# =====================================================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
