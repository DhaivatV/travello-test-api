from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from .models import Destination
from .Serializers import DestinationSerializer


def index(request):
    
    dests = Destination.objects.all()

    
    return render(request, 'index.html',{'dests':dests})
    
def about (request):
    return render(request, 'about.html')

def contact (request):
    return render(request, 'contact.html')


class DestinatioList(APIView):
    def get(self, request):
        Destination1 = Destination.objects.all()
        serializer = DestinationSerializer(Destination1, many= True)
        return HttpResponse(serializer.data)

    def post(self):
        pass