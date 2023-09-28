from flask import Flask
app = Flask(__name__)


@app.route("/home")
def home():
    return "Welcome to web application using Flask"


@app.route("/help")
def help():
    return "This is Help Page using Flask"


def contact():
<<<<<<< HEAD
    return "This is Contact page using  the Flask"
=======
    return "This is Contact page using Flask"
>>>>>>> 716360fabe1e8601c98f583c4ad891e6f33af32f


app.add_url_rule("/contact","contact",contact)


if __name__ == '__main__':
    app.run(debug=True)