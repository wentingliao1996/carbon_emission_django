from django.shortcuts import render
from .models import TestDB
import requests
import datetime

# Create your views here.
def welcome(request):
    now = datetime.datetime.now().strftime("%Y/%m/%d")
    c={'date':now}
    return render(request,'index.html',c)

def freighter(request):
    return render(request,'main.html')

def caculate_freighter(request):
    id = request.POST['id']
    distance = float(request.POST['distance'])
    weight = float(request.POST['weight'])
    
    result = round(distance*0.0425*weight,4)
     
    insertdatabase = TestDB()
    insertdatabase.name = id
    insertdatabase.distance = distance
    insertdatabase.teu = weight
    insertdatabase.carbon = result
    insertdatabase.save()
    return render(request,'caculate_freighter.html',{'ship_id':id,'ship_distance':distance,'teu':weight,"result":result})