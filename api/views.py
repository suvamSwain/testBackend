from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.

# def home(request):
# 	return HttpResponse(
# 		"<div><h1>This is the backend</h1></div>"
# 		);

class ProjectManagerViewset(viewsets.ViewSet):
    #http_method_names = ['post','get','put','delete']
    permission_classes = [permissions.AllowAny]
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer
      
    def list(self,request):
        queryset = ProjectManager.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)

class ProjectViewset(viewsets.ViewSet):
    #http_method_names = ['post','get','put','delete']
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
      
    def list(self,request):
        queryset = Project.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
        
    def retrieve(self,request,pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = 400)
        
    def destroy(self,request,pk=None):
        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)

