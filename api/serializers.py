from rest_framework import serializers
from .models import *

#the serializer contains all data going from backend to frontend and frontend to backend

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name','start_date','end_date','comments','status','projectmanager')

class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = ('name','id')