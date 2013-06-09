from django.db import models

# Create your models here.


class ProfileModel(Model.Model):
	#expiry_date
	#source
	pass

class FieldModel(Model.Model):
	name = models.TextField(max_length=255)

class FieldValueModel(Model.Model):
	field = models.ForeignKey('FieldModel')
	profile = models.ForeignKey('ProfileModel')
	value = models.TextField()


first_name = "Miles"
last_name = "Richardson"
ssn = '628-26-2612'
profile = FieldValueModel.Objects.all(field=field.Objects.get(name='first_name'), value=first_name)\
			.Objects.all(field=field.Objects.get(name='last_name'), value=last_name)\
			.Objects.all(field=field.Objects.get(name='ssn', value=ssn))\
			.profile
