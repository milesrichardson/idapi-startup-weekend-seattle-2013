from django.contrib import admin
from webapp.models import *

class ProfileAdmin(admin.ModelAdmin):
	pass

class FieldAdmin(admin.ModelAdmin):
	pass

class FieldValueAdmin(admin.ModelAdmin):
	pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(FieldValue, FieldValueAdmin)