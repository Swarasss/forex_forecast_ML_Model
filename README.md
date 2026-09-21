If you just run this Python file exchange_rate_forecasting_laggedEngineering.py in your working directory.
With the matplotlib, random forestregressor and sckit learn libraries installed you should just see something like this printed on your terminal
exhange_rate_forecasting_laggedEngineering.py
YF.download() has changed argument auto_adjust default to True
[*********************100%***********************]  1 of 1 completed
Price          Close      High       Low      Open   Volume
Ticker      EURUSD=X  EURUSD=X  EURUSD=X  EURUSD=X EURUSD=X
Date                                                       
2015-01-01  1.209863  1.209863  1.209863  1.209863        0
2015-01-02  1.208941  1.208956  1.201080  1.208868        0
2015-01-05  1.194643  1.197590  1.188909  1.195500        0
2015-01-06  1.193902  1.197000  1.188693  1.193830        0
2015-01-07  1.187536  1.190000  1.180401  1.187479        0
Default - RMSE: 0.0047, R² Score: 0.9248
mtry=half - RMSE: 0.0047, R² Score: 0.9224
mtry=double - RMSE: 0.0047, R² Score: 0.9248

RMSE Comparison Table:
Default: 0.0047
mtry=half: 0.0047
mtry=double: 0.0047

results of exchange_rate_forecasting.py file on my terminal
YF.download() has changed argument auto_adjust default to True
[*********************100%***********************]  1 of 1 completed
Price          Close      High       Low      Open   Volume
Ticker      EURUSD=X  EURUSD=X  EURUSD=X  EURUSD=X EURUSD=X
Date                                                       
2015-01-01  1.209863  1.209863  1.209863  1.209863        0
2015-01-02  1.208941  1.208956  1.201080  1.208868        0
2015-01-05  1.194643  1.197590  1.188909  1.195500        0
2015-01-06  1.193902  1.197000  1.188693  1.193830        0
2015-01-07  1.187536  1.190000  1.180401  1.187479        0
2015-01-01 00:00:00 2024-12-31 00:00:00
(2606, 5)
Price   Ticker  
Close   EURUSD=X    0
High    EURUSD=X    0
Low     EURUSD=X    0
Open    EURUSD=X    0
Volume  EURUSD=X    0
dtype: int64
RMSE: 0.0060
R² Score: 0.8742