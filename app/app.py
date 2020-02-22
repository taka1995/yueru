from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    menhera = ["返信まだ？","返信まだ?","返信まだ？","浮気？笑"]
    return render_template("index.html",name=name, menhera=menhera)

@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    menhera = ["返信まだ？","返信まだ?","返信まだ？","浮気？笑"]
    return render_template("index.html",name=name, menhera=menhera)


if __name__ == "__main__":
    app.run(debug=True)
