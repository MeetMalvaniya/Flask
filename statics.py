from flask import Flask,render_template,url_for
app = Flask(__name__)
@app.route("/app")
def statics():
    return render_template("statics.html")

if __name__ == "__main__":
    app.run(debug=True)
