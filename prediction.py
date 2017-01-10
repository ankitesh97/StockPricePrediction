import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(filename):
	csvfile = open(filename,'r')
	csvFileReader = csv.reader(csvfile)
	next(csvFileReader) #this skips column names
	for row in csvFileReader:
		dates.append(int(row[0].split('-')[0]))
		prices.append(float(row[1]))
	return

def predict_price(dates, prices,x):
	linear_mod = linear_model.LinearRegression()
	dates = np.reshape(dates, (len(dates),1))
	prices = np.reshape(prices, (len(prices),1))
	linear_mod.fit(dates,prices)
	predicted_price = linear_mod.predict(x)
	return predicted_price[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]

def show_plot(dates, prices):
	linear_mod = linear_model.LinearRegression()
	dates = np.reshape(dates, (len(dates),1))
	prices = np.reshape(prices, (len(prices),1))
	linear_mod.fit(dates,prices)
	plt.scatter(dates, prices, color='yellow')
	plt.plot(dates,linear_mod.predict(dates), color='blue', linewidth=3)
	plt.show()
	return

get_data('goog.csv')
print dates
print prices
print "\n"

show_plot(dates,prices)
predicted_price, coeff, constant = predict_price(dates,prices,29)
print "The stock open price for 29th Feb is: $",str(predicted_price)
print "The regression coefficient is ",str(coeff),", and the constant is ", str(constant)
print "the relationship equation between dates and prices is: price = ",str(coeff),"* date + ",str(constant)



