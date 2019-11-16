# Model Deployment using Flask::Linear Regression
---

This demo implementation exposes APIs/endpoints to interact with a linear regression model.


## Steps

__Starting the Server__
```
# Starting the server using command prompt

>python server.py
# This will start the flask server in debug mode at port **9090**
# Checkout the server by opening a browser at http://localhost:9090
```

__Using the Server__
```
# Welcome page
Open up a browser at http://localhost:9090/

# Train a linear regression model
Open up a browser at http://localhost:9090/train_model

# Get Predictions from  linear regression model
Open up a browser at http://localhost:9090/predict_outcome?house_size=1750
```
