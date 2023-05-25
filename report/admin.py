from django.contrib import admin
from .models import repo,repo_type

# Register your models here.
admin.site.register(repo)
admin.site.register(repo_type)