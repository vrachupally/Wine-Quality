import numpy as np
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


    int_features = [float(x) for x in request.form.values()]
    # int_features = [float(x) for x1 in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    
    if prediction==1:
        return render_template('index.html',
                               prediction_text='Wine is of LOW quality'.format(prediction),
                               )
    elif prediction==2:
        return render_template('index.html',
                               prediction_text='Wine is of MEDIUM quality'.format(prediction),
                               )                          
    else:
        return render_template('index.html',
                               prediction_text='Wine is of HIGH quality'.format(prediction),
                              )



if __name__ == "__main__":
    app.run(debug=True)