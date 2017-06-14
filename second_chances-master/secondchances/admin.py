from django.contrib import admin
from .models import *
from directmessages.models import Message

admin.site.register(User_Profile)
admin.site.register(Job)
admin.site.register(Location)
admin.site.register(User_Location)
admin.site.register(Skills)
admin.site.register(Provided_Skill)
admin.site.register(Required_Skill)
admin.site.register(Needs)
admin.site.register(User_Needs)
admin.site.register(Provided_Needs)
admin.site.register(Service)
admin.site.register(Connection)
admin.site.unregister(Message)
admin.site.register(Message)
