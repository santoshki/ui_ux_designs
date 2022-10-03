from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/data/', methods=["GET", "POST"])
def data():
    return render_template("app1.html")


if __name__ == '__main__':
    app.run(debug=True)