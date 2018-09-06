from django.contrib import admin
from .models import Stations,UserProfileMode

class UserprofileAdmin(admin.ModelAdmin):
	list_display=['user','station_type']


admin.site.register(Stations,)
admin.site.register(UserProfileMode,UserprofileAdmin)
