from django.db import models

# Create your models here.


class Profile(models.Model):
	expiry_date = models.DateTimeField()
	#creation_date = models.DateTimeField()

	def __str__(self):
		return str(self.pk)

class Field(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class FieldValue(models.Model):
	field = models.ForeignKey('Field')
	profile = models.ForeignKey('Profile')
	value = models.TextField()


# first_name = "Miles"
# last_name = "Richardson"
# ssn = '628-26-2612'
# profile = FieldValueModel.Objects.all(field=field.Objects.get(name='first_name'), value=first_name)\
# 			.Objects.all(field=field.Objects.get(name='last_name'), value=last_name)\
# 			.Objects.all(field=field.Objects.get(name='ssn', value=ssn))\
# 			.profile
