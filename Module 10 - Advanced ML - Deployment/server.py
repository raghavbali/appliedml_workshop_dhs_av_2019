################################
# import 
################################
from flask import Flask, render_template, request
from flask import jsonify
import requests
import json
import os

import linear_regression as lr

################################
# SETUP 
################################
app = Flask("ML Deployment:Linear Regression Server",
            static_folder=r'static', static_url_path='')
app.requests_session = requests.Session()
app.secret_key = os.urandom(42)


with open(r'config.json') as f:
    config = json.load(f)
    

################################
# SERVER ENDPOINTS 
################################  
  
@app.route('/', methods=['GET'])
def default_url():
    """Default URL for the server"""
    return render_template(
            'lr_html.html',
            endpoint='/',
            data=json.dumps(config, sort_keys=True, indent=4),
            )


@app.route("/train_model", methods=['GET'])
def train_lin_reg():
    """Trains a LR model and persists it as pickle file"""
    return render_template(
            'default_html.html',
            endpoint='train_model',
            data=lr.train_model(),
            )  
    
@app.route("/predict_outcome", methods=['GET'])
def predict_outcome():
    """Uses a saved model to make predictions"""
    
    # extract url parameters
    house_size = float(request.args.get('house_size'))
    response_type = request.args.get('response_type')
    
    # return a response based on required type
    if response_type=='json':
        return jsonify(
        house_price=lr.predict_outcome(house_size,response_type=response_type),
        house_size=house_size
        )
    else:
        return render_template(
            'default_html.html',
            endpoint='predict_outcome',
            data=lr.predict_outcome(house_size),
            )   
    

################################
# START SERVER
################################     
if __name__ == '__main__':
    app.debug = os.environ.get('FLASK_DEBUG', True)
    app.run(port=9090)       