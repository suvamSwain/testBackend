from django.db import models

#Create your models here.
class ProjectManager(models.Model):
    name = models.CharField(unique=True,max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(unique=True,max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.CharField(max_length = 500, blank=True, null=True)
    status = models.CharField(max_length = 100)
    projectmanager = models.ForeignKey(ProjectManager,on_delete = models.CASCADE, blank=True, null=True) #manager is deleted then project deleted
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
