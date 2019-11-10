################################
# import 
################################
import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib


################################
# train the model
################################
def train_model():
    try:    
        model_path = 'linear_regression.pkl'
        
        house_size_sq_ft = list(range(1100,2100,100))
        house_price = [119000, 126000, 133000, 150000, 
                       161000, 163000, 169000, 182000, 201000, 209000]
        
        model = linear_model.LinearRegression()
        model.fit(np.reshape(house_size_sq_ft,(-1,1)), house_price)
    
        # persist model
        joblib.dump(model, model_path) 
        
        return str(model)
    except Exception as ex:
        return "ERROR:"+str(ex)
    
def predict_outcome(house_size,model_path='linear_regression.pkl',
                    response_type=None):
    try:
        model = joblib.load(model_path)
        if response_type=='json':
            return model.predict(np.reshape(house_size,(1,-1)))[0]
        else:
            return "House of size " + str(house_size) + \
                " has a Predicted Price : " + \
                str(model.predict(np.reshape(house_size,(1,-1)))[0])
    except Exception as ex:
        return "ERROR:"+str(ex)
    