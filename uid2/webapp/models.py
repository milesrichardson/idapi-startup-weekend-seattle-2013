from django.db import models

class Profile(models.Model):
	expiry_date = models.DateTimeField()

	def __str__(self):
		return str(self.pk)
def lookup_firstname(instance):
        val = list(FieldValue.objects.filter(field=Field.objects.filter(name='first_name')).filter(profile=instance.pk))
        if len(val) > 0:
                val = val[0].value
        else:
                val = None
        return val
def lookup_lastname(instance):
        val = list(FieldValue.objects.filter(field=Field.objects.filter(name='last_name')).filter(profile=instance.pk))
        if len(val) > 0:
                val = val[0].value
        else:
                val = None
        return val
def lookup_dob(instance):
        val = list(FieldValue.objects.filter(field=Field.objects.filter(name='last_dob')).filter(profile=instance.pk))
        if len(val) > 0:
                val = val[0].value
        else:
                val = None
        return val
def lookup_ssn(instance):
        val = list(FieldValue.objects.filter(field=Field.objects.filter(name='ssn')).filter(profile=instance.pk))
        if len(val) > 0:
                val = val[0].value
        else:
                val = None
        return val
def lookup_source_url(instance):
        val = list(FieldValue.objects.filter(field=Field.objects.filter(name='source_url')).filter(profile=instance.pk))
        if len(val) > 0:
                val = val[0].value
        else:
                val = None
        return val
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
# profile = FieldValueModel.Objects.all(field=field.Objects.get(name='first_name'), pytvalue=first_name)\
# 			.Objects.all(field=field.Objects.get(name='last_name'), value=last_name)\
# 			.Objects.all(field=field.Objects.get(name='ssn', value=ssn))\
# 			.profile
# ./manage.py syncdb
