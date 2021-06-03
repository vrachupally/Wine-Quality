# import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# read our pickle file and label our logisticmodel as model
model = pickle.load(open('finalized_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])   
def predict():

    # x1 = [7.4, 0.7, 0, 1.9, 0.076, 11, 34, 0.9978, 3.51, 0.56, 9.4]
    # x2 = [7.8, 0.88, 0, 2.6, 0.098, 25, 67, 0.9968, 3.2, 0.68, 9.8]
    # x3 = [7.8, 0.76, 0.04, 2.3, 0.092, 15, 54, 0.997, 3.26, 0.65, 9.8]
    print("test wine")
    
    if request.method == 'POST':
        input1 = float(request.form["input1"])
        input2 = float(request.form["input2"])
        input3 = float(request.form["input3"])
        input4 = float(request.form["input4"])
        input5 = float(request.form["input5"])
        input6 = float(request.form["input6"])
        input7 = float(request.form["input7"])
        input8 = float(request.form["input8"])
        input9 = float(request.form["input9"])
        input10 = float(request.form["input10"])
        input11 = float(request.form["input11"])

        features = [[input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11]]
        print(features)

        # int_features = [float(x) for x in user_wine]
    # int_features = [float(x) for x1 in request.form.values()]
        # final_features = [np.array(int_features)]
        
        model = pickle.load(open("finalized_model.pkl", "rb"))
        prediction = model.predict(features)
    # print("I'm in the money!")
        print(prediction)
    
        if prediction[0]=="1":
            print("wine low quality")
            return render_template('index.html',
                               prediction_text='Wine is of LOW quality'
                               )
        elif prediction[0]=="2":
            return render_template('index.html',
                               prediction_text='Wine is of MEDIUM quality'
                               )                          
        else:
            return render_template('index.html',
                               prediction_text='Wine is of HIGH quality'
                              )
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
