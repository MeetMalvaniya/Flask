from flask import Flask,redirect,url_for,request

app=Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return "welcome %s" %name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['name']
        return redirect(url_for('welcome',name=user))
    else:
        user=request.args.get('name')
        return redirect(url_for('welcome',name=user))

if __name__ == '__main__':
    app.run(debug=True)
