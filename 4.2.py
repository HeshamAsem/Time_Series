import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AR 
from statsmodels.tsa.arima_model import ARMA  
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.vector_ar.var_model import VAR
from random import random



# AR example

# contrived dataset
xdata = range(1, 100)
ydata = [x + (3*random()) for x in xdata]
plt.xlim(0, 100)
plt.ylim(0, 100)

plt.scatter(xdata,ydata,s=10)
plt.show()
print()

# fit model
model = AR(ydata)
model_fit = model.fit()

# make prediction
#yhat = model_fit.predict(len(xdata), len(ydata))
yhat = model_fit.predict( start= 90, end = 110 )
print('Predicted value for Auto Regression ', yhat)

#==========================================================

# MA example

# fit model
model = ARMA(ydata, order=(0, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict( start= 90, end = 110 )
print('Predicted value for Moving Average 0,1 ',yhat)


#==========================================================


# ARMA example
newdata = [random() for x in range(1, 100)]

# change order
model = ARMA(newdata, order=(2, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict( start= 90, end = 110 )
print('Predicted value for Moving Average 2,1 ',yhat)

#==========================================================

# contrived dataset
data = [x + random() for x in range(1, 100)]
# fit model
model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict( start= 90, end = 110 )
print('Predicted value using SARIMAX ',yhat)


#==========================================================

# VAR example


# contrived dataset with dependency
data = []
for i in range(100):
    v1 = i + random()
    v2 = v1 + random()
    row = [v1, v2]
    data.append(row)
    
data    
# fit model
model = VAR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.forecast(model_fit.y, steps=1)
print('Predicted value using VAR ',yhat)

