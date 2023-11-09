from django.shortcuts import render
from rest_framework import generics
from .serializers import ToDoSerializer
from .models import ToDo


# Create your views here.

class ListToDo(generics.ListAPIView): #read
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
  
 
    def get_queryset(self):
        return ToDo.objects.filter(owner=self.request.user) 

class CreateToDo(generics.CreateAPIView): #create
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


    def perform_create(self, serializer):
        return serializer.save() 
    

class DetailToDo(generics.RetrieveUpdateAPIView): #update
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def get_queryset(self):
        return ToDo.objects.filter()

class DeleteToDo(generics.DestroyAPIView): #delete
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    lookup_field = "id" 

    def get_queryset(self):
        return ToDo.objects.filter()