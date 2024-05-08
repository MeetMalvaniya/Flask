from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'hello '

@app.route('/')
def hello_world():
    str="""
<html>
<body>
<h1>Hello</h1>
</body>
</html>"""
    return str

if __name__ == '__main__':
    app.run(debug=True)