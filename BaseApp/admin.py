from django.contrib import admin
from .models import Guitar, Bass, Client

# Register your models here.
admin.site.register(Guitar)
admin.site.register(Bass)
admin.site.register(Client)