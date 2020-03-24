from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import  APIView
# Create your views here.
from .main import Prediction
class API(APIView):
    def post(self , request , *args , **kwargs):
        data = request.data
        print(data)
        age = data['age']
        heartrate = data['heartrate']
        gender = data['gender']
        bloodpressure = data['bloodpressure']
        diabetic = data['diabetic']
        smooker = data['smooker']
        drinker = data['drinker']
        athlete = data['athlete']
        bmi = data['bmi']
        pred = Prediction(age=age ,HeartRate=heartrate , Gender=gender , bloodpressure=bloodpressure , Diabetic=diabetic
                          , Smooker=smooker , Drinker=drinker , Athlete=athlete , BMI=bmi)
        return Response({'prediction' : pred})

   # {
   #     'age' : 60,
    #    'heartrate' : 150,
     #   'gender' : 1,
      #  'bloodpressure' : 0,
       # 'diabetic' : 1 ,
        #'smooker' : 1 ,
        #'drinker' : 0,
        #'athlete' : 1 ,
        #'bmi': 2
    # }