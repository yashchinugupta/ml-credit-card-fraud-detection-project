from flask import Flask,request, url_for, redirect, render_template
import pickle
import os
import numpy as np
import joblib

app = Flask(__name__)
model=pickle.load(open('modell.pkl','rb'))

picFolder = os.path.join('static','pics')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder


@app.route('/')
def myform ():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'cc.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'ccc.png')
    return render_template("random.html", user_image=pic1,user_image1=pic2)

@app.route('/predict', methods=['GET', 'POST'])
def basic():
    x_test=[[(x) for x in request.form.values()]]

    print(x_test)

    sc=joblib.load('scalar.save')
    predection=model.predict(sc.transform(x_test))
    print(predection)
    output=predection[0]
    if (output==0):
        pred="there is no fraud"
        return render_template("random.html", user_image=pic1, user_image1=pic2,predectionn=pred)
    elif(output==1):
        pred = "yes! there is fraud"
        return render_template("random.html", user_image=pic1, user_image1=pic2,predectionn=pred)
    else:
        pred="please enter valid value!!"
        return render_template("random.html", user_image=pic1, user_image1=pic2, predectionn=pred)
if __name__ == '__main__':
    app.run(debug=True)