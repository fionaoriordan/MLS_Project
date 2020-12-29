

# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
# used to save and then use models
import joblib

# required for using tf keras model
from tensorflow.keras.models import load_model

linearreg = joblib.load("models/linearreg.pkl")
polyreg = joblib.load("models/polyreg.pkl")
polyreg3 = joblib.load("models/polyreg3.pkl")
model = load_model("models/kerasmodel.h5")

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# CURL  127.0.0.1:5000/api/linearreg/6
testwind = 4
print("Linear Model, testwind linearreg:", testwind, linearreg.predict([[testwind]]))


# Add linear model root.
@app.route('/api/linearmodel/<float:wind>')
@app.route('/api/linearmodel/<int:wind>')
def linearmodel(wind):
    prediction = linearreg.predict([[wind]])
    return {"value": str(prediction[0])}


# CURL  127.0.0.1:5000/api/polyreg/6
# print("Polyreg 2D Model, testwind entered:", testwind, polyreg.predict([[testwind, testwind**2]]))

# Add polynominal reggresion root with x powered to x^2
@app.route('/api/polyregmodel/<float:wind>')
@app.route('/api/polyregmodel/<int:wind>')
def polyregmodel(wind):
    # replicate as in single test & power up wind and pass as additional value.
     
    prediction = polyreg.predict([[wind, wind**2]])
    return {"value": str(prediction[0])}


# Add polynominal reggresion root with x powered to x^2 and x^3
@app.route('/api/polyreg3model/<float:wind>')
@app.route('/api/polyreg3model/<int:wind>')
def polyreg3model(wind):
    # replicate as in single test & power up wind and pass as additional value.
     
    prediction = polyreg3.predict([[wind, wind**2, wind**3]])
    return {"value": str(prediction[0])}


# # Add uniform route.
# @app.route('/api/uniform')
# def uniform():
#   return {"value": np.random.uniform()}


# CURL  127.0.0.1:5000/api/kerasmodel/6.5
testwind = 8.5
print("Keras Model testwind entered:", testwind, model.predict([[testwind]]))

@app.route('/api/kerasmodel/<float:wind>')
@app.route('/api/kerasmodel/<int:wind>')
def kerasmodel(wind):
    prediction = model.predict([wind])
    return {"value": str(prediction[0][0])}

# @app.route('/api/kerasmodel/<float:wind>')
# print(wind)
# def kerasmodel(wind):
#     prediction = model.predict([wind])
#     return {"value": str(prediction[0][0])}