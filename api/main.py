from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
def Prediction(age , HeartRate , Gender , bloodpressure , Diabetic , Smooker , Drinker , Athlete , BMI):
    data = pd.read_excel('api/data.xlsx' , sheet_name="datasheet")
    #data['AGE'] = pd.cut(data['AGE'] , bins=[0 , 50 , 200] , labels=["young" , "old"])
    #data['Heart Rate'] = pd.cut(data['Heart Rate'] , bins=[0 , 60 , 101 , 400] , labels=["bad" , "good" , "Bad"])
    #data['AGE'] = pd.factorize( data['AGE'] )[0]
    #data['Heart Rate'] = pd.factorize(data['Heart Rate'])[0]
    #print(data)
    data = data.to_numpy()
    X = data[: , :9]
    Y = data[: , 9]

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.2 , random_state=0)
    gnb = DecisionTreeClassifier(random_state=0, max_depth=13)

    gnb.fit(X_train, Y_train)
    estimator = 200
    btd = AdaBoostClassifier(gnb,
                             algorithm="SAMME",
                             n_estimators=estimator, random_state=0
                             )
    btd.fit(X_train, Y_train)
    #res = btd.predict(X_test)
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
    prediction = btd.predict(d)
    return prediction