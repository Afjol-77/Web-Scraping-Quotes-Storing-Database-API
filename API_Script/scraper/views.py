from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CreateQuotesList(generics.CreateAPIView): #Create
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer
    permission_classes = [IsAuthenticated]
    
class ReadQuotesList(generics.ListAPIView): #Read
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer
    permission_classes = [IsAuthenticated]

class RetrieveQuotesList(generics.RetrieveAPIView): #Retrieve
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer
    permission_classes = [IsAuthenticated]

class DeleteQuotesList(generics.DestroyAPIView): #Delete
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer
    permission_classes = [IsAuthenticated]

