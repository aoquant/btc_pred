import numpy as np
import random
from sklearn.linear_model import LinearRegression

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()

def load_from_file():
    prices = open("prices.txt", "r")
    lines = prices.readlines()
    for line in lines:
        s = line.split(',')
        TRAIN_INPUT.append([int(s[0])])
        TRAIN_OUTPUT.append(float(s[1]))
    print("finished grabbing input from prices.txt")


def do_learn_and_pred():
  load_from_file()
  predictor = LinearRegression(n_jobs=-1).fit(TRAIN_INPUT, TRAIN_OUTPUT) 
  #create logistic_regression and fit it  

  X_TEST = [[1568835565], [1735732800]] #1st one is 09/18/19, second one is 01/01/25
  outcome = predictor.predict(X_TEST) #predict
  #score = predictor.score(X_TEST, outcome)
  #coefficients = predictor.coef_

  print(outcome)
  #print("===============================")
  #print(score)
  print("finished prediction")

def console_notification():
    print("btc predictor using machine learning")
    print("coded by Sanjay K (@sanjaykdragon)")
    print("https://github.com/sanjaykdragon/btc_predictor_ml")
    print("credits to coindesk for the API, sklearn for the ML stuff, me for being a genius")


console_notification()
do_learn_and_pred()