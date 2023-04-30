from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/nums/<int:num>/<int:num2>')
def nums(num, num2):
    maxi = max(num, num2)
    return str(maxi)


@app.route('/sqrt')
def sqrt():
    s = ' '.join([f"<li>: {i * i}</li>" for i in range(1, 101)])
    return f"<ol>{s}</ol>"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
