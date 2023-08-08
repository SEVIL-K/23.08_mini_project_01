from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# 2조 조호진입니다.
from pymongo import MongoClient
# 이건 제 mongo 주소인거같네요..
client = MongoClient('mongodb+srv://sparta:test@cluster0.aolfafs.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta



@app.route('/')
def home():
   return render_template('introduce.html')
   

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    visitor_name4_receive = request.form['visitor_name4_give']
    visitor_comment4_receive = request.form['visitor_comment4_give']
    star_receive = request.form['star_give']
    # 혹시나 겹칠까봐 visitor_name4 이런식으로 바꿨습니다.. star는 아직 못바꿨습니다..
    doc = {
            'visitor_name4': visitor_name4_receive,
            'visitor_comment4' : visitor_comment4_receive,
            'star':star_receive
    }
    # 여기도 visitor 로바꿨씁니다.
    db.visitor.insert_one(doc)
    return jsonify({'msg': '저장 완료'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    #  여기도 visitor 로 바꿨습니다.
    all_comments = list(db.visitor.find({},{'_id':False}))
    return jsonify({'result': all_comments})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
