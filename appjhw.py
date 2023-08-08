from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.wop0dox.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile', methods=["POST"])
def profiles_post_comment():
    nickname_receive = request.form['nickname_give']
    emoticon_receive = request.form['emoticon_give']
    comment_receive = request.form['comment_give']
    
    doc = {
        'nickname':nickname_receive,
        'emoticon':emoticon_receive,
        'comment':comment_receive
    }

    db.profiles.insert_one(doc)

    return jsonify({'msg':'댓글 감사합니다!!!!'})

@app.route("/profile", methods=["GET"])
def profiles_get_comment():
    profiles_data = list(db.profiles.find({},{'_id':False}))
    return jsonify({'result':profiles_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)