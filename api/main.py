from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import pandas as pd
import numpy as np
def Prediction(age , HeartRate , Gender , bloodpressure , Diabetic , Smooker , Drinker , Athlete , BMI):
    data = pd.read_excel('api/data.xlsx' , sheet_name="datasheet")
    data['AGE'] = pd.cut(data['AGE'] , bins=[0 , 50 , 200] , labels=["young" , "old"])
    data['Heart Rate'] = pd.cut(data['Heart Rate'] , bins=[0 , 60 , 101 , 400] , labels=["bad" , "good" , "Bad"])
    data['AGE'] = pd.factorize( data['AGE'] )[0]
    data['Heart Rate'] = pd.factorize(data['Heart Rate'])[0]
    data = data.to_numpy()
    X = data[: , :9]
    Y = data[: , 9]

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.2 , random_state=0)

    gnb = DecisionTreeClassifier()
    gnb.fit(X_train , Y_train)
# Predict all data and calculate accuracy
#Y_pred = gnb.predict(X_test)
#cnt = 0
#for i in range(0 , len(Y_pred)):
#    if Y_test[i] == Y_pred[i]:
#        cnt+=1
#accuracy = (cnt/len(Y_pred))*100
#print(accuracy)

#age = int(input("Enter Age : "))
#HeartRate = int(input("Enter HeartRate : "))
#Gender = int(input("Enter Gender : "))
#bloodpressure = int(input("Enter bloodpressure : "))
#Diabetic = int(input("Enter Diabetic : "))
#Smooker = int(input("Enter Smooker : "))
#Drinker = int(input("Enter Drinker  : "))
#Athlete = int(input("Enter Athlete : "))
#BMI = int(input("Enter BMI : "))
    d = np.array([[age , HeartRate , Gender , bloodpressure , Diabetic , Smooker , Drinker , Athlete , BMI]])
    prediction = gnb.predict(d)
    return prediction