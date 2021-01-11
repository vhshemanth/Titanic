# importing the necessary dependencies
import pickle

from flask import Flask, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():

    if request.method=='POST':
        try:
            pclass=int(request.form['pclass'])
            gender=request.form['gender']
            age=int(request.form['age'])
            sib=int(request.form['sib'])
            parch=int(request.form['parch'])
            fare=float(request.form['fare'])
            embarked=request.form['embarked']


            if gender=='Male':
                 Male=1
            elif gender=='Female':
                 Male=0

            if embarked=='Cherbourg':
                Queenstown = 0
                Southampton = 0
            elif embarked=='Queenstown':
                Queenstown=1
                Southampton = 0
            else:
                Southampton=1
                Queenstown = 1

            model = pickle.load(open('titianic_survival_dtree.pickle', 'rb'))
            output=model.predict([[pclass,Male,age,sib,parch,fare,Queenstown,Southampton]])

            if output==1:
                return render_template('home.html',prediction_text="Woohoo..! The Person didn't die in the Titanic Crash")
            else:
                return render_template('home.html', prediction_text="Sorry..! The Person died in the Titanic Crash")
        except:
            return "Please enter correct Details"



if __name__=="__main__":
    app.run(debug=True)

