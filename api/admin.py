from django.contrib import admin
from .models import Project,ProjectManager

# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectManager)