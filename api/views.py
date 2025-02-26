from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from message.settings import STATIC_URL
import os
import json
# Create your views here.
class getMessage(APIView):
    def get(self,request):
        
        databse_url = os.path.join(STATIC_URL,'database.json')
        

        databse = open(databse_url)
        data = json.load(databse)
        # data['message'].append({'name':name,'message':message})
        
        # with open(databse_url, "w") as outfile:
        #     json.dump(data, outfile,indent=4)
        
        return Response(data)