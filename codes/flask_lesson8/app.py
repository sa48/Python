from flask import Flask,request
from sklearn.linear_model import LogisticRegressionCV
from keras.models import Sequential
import numpy as np
import tensorflow as tf

# we are creating a variable which is the Flask application
app = Flask(__name__) 

from joblib import dump, load
loaded_lr = clf = load('lr_iris.joblib') 

from keras.models import model_from_json
# load json and create model
json_file = open('iris_nn.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("iris_nn.h5")
loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
graph = tf.get_default_graph()

@app.route('/predict_lr/<sl>/<sw>/<pl>/<pw>')
def predict_lr(sl,sw,pl,pw):
    return loaded_lr.predict([[float(sl),float(sw),float(pl),float(pw)]])[0]

@app.route('/predict_nn/<sl>/<sw>/<pl>/<pw>')
def predict_nn(sl,sw,pl,pw):
    global graph
    with graph.as_default():
        loaded_model.predict(np.array([[5.8, 2.8, 5.1, 2.4]]))
        nn_y = loaded_model.predict(np.array([[float(sl),float(sw),float(pl),float(pw)]]))[0]
        if nn_y[0] == 1:
            return 'setosa'
        elif nn_y[1] == 1:
            return 'versicolor'
        else:
            return 'virginica'

@app.route('/hello')
def hello():
    return 'Hello'

if __name__ =='__main__':
    app.run(debug=True)

