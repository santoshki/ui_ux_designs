from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/home')
def form():
    return render_template('hapti.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
