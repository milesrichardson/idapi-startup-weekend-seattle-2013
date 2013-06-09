from django.contrib import admin
from webapp.models import *

class ProfileAdmin(admin.ModelAdmin):
        list_display = ('expiry_date', lookup_firstname,lookup_lastname, lookup_dob, lookup_ssn, lookup_source_url,sex_offender)
        date_hierarchy = 'expiry_date'
        # search_fields = (lookup_firstname,) # doesn't work with callables

class FieldAdmin(admin.ModelAdmin):
	pass

class FieldValueAdmin(admin.ModelAdmin):
	pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(FieldValue, FieldValueAdmin)
