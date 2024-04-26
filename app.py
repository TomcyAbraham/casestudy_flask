from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
with open('model.pkl','rb') as model_file:
    model=pickle.load(model_file)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method=='POST':


        Gend=request.form['Gender']
        if Gend=="Male":
            Gender=1
        elif Gend=='Female':
            Gender=0

        Age=float(request.form['Age'])
        print(Age)
        EstimatedSalary=float(request.form['EstimatedSalary'])
      
        newdata=np.array([[Gender,Age,EstimatedSalary ]])

        Purchased = model.predict(newdata)
      
        return render_template('index.html',Purchased[0])

if __name__=='__main__':
    app.run()