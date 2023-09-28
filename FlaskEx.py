from flask import Flask
app = Flask(__name__)


@app.route("/home")
def home():
    return "Welcome to web application using Flask"


@app.route("/help")
def help():
    return "This is Help Page using Flask"


def contact():
    return "This is Contact page using Flask"


app.add_url_rule("/contact","contact",contact)


if __name__ == '__main__':
    app.run(debug=True)