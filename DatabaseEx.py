from flask import *
from mysql import connector
app = Flask(__name__)


@app.route('/insert',methods=['POST','GET'])
def insert():

    if request.method=='POST':
        uname = request.form['uname']
        email = request.form['email']
        password = request.form['pass']
        myDbConnection = connector.connect(host='localhost', user='root', password='root',
                                           database='pythonmagnus')
        c1 = myDbConnection.cursor()
        c1.execute("insert into user(username,email,password) values(%s,%s,%s)",(uname,email,password))
        myDbConnection.commit()
        data = "Data Inserted Successfully"
    else:
        data = "Data not Inserted Successfully and used method is"+request.method
    return render_template('out.html',output=request.form)



if __name__ == '__main__':
    app.run(debug=True)