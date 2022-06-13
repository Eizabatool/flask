from flask import Flask, render_template, request, jsonify
application = Flask(__name__)
@application.route("/")
def index():
    return render_template("index.html")

#@application.route("/myname/", methods=['POST'])
#def my_name():
#
#     3fname = request.form['fname']
#    3 lname = request.form['lname']
# tname = request.form['tname']
#     name = int(fname) + int(lname) + int(tname)
#     return render_template('index.html', results=name)

@application.route("/myencoder/", methods=['GET'])
def myfunc():
    from sklearn.preprocessing import LabelEncoder
    import pandas as pd
    df=pd.read_csv('C:\Users\use  r\Downloads     \Iris.csv')
    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    encoded=le.fit_transform(df['Species'])
    return jsonify({"eiza": list (encoded)})

@application.route("/myencoder/", methods=['GET'])
def train():
    from sklearn import neighbors
    neighbors.KNeighborsClassifier
    dd
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)


if __name__ == "__main__":
    application.run(host="localhost", port=3459, debug=True)
