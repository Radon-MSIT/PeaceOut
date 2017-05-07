from django.contrib import admin

from .forms import InfoForm

from .models import  Info

class InfoAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email", "timestamp", "updated"]
	list_display_links = ["__str__"]
	search_fields = ["Full_Name", "Phone_No"]
	
	form = InfoForm

admin.site.register(Info, InfoAdmin)