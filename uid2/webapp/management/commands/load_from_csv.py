import os
from datetime import datetime
from webapp.models import Profile, FieldValue, Field
from django.conf import settings
from subprocess import call
from django.core.management.base import CommandError, NoArgsCommand
from django.db import models
from dateutil.relativedelta import relativedelta
from time import sleep
import csv

class Command(NoArgsCommand):
    help = 'load in data from csv'
    def handle_noargs(self, **options):
        # load in each of the rows of csv data and populate the database.
		fp = open('msor.csv', 'rb')
		reader = csv.reader(fp)

		for line in reader:
			print "Processing data", line
			profile = Profile()
			profile.expiry_date = datetime.utcnow() + relativedelta(years=+1)	
			#profile.creation_date = datetime.utcnow()
			profile.save()
			
			# for reference
			# dataformat = ['Name','Address','City', 'St', 'Zip', 'County', 'Offense', 'Count', 'Compliant']

			fv = FieldValue()
			fv.field = Field.objects.get(name='last_name')
			fv.value = line[0].split(',')[1] 		# parse last name
			print fv.value
			fv.profile = profile
			fv.save()	# profile_id cannot be null bug
			
			fv = FieldValue()
			fv.field = Field.objects.get(name='first_name')
			fv.value = line[0].split(',')[0].rstrip(', ')
			fv.profile = profile
			fv.save()

			fv = FieldValue()
			fv.field = Field.objects.get(name='address')
			address = ''
			for i in range(1, 6):
				address += line[i].strip() + " "
			fv.value = address
			fv.profile = profile
			fv.save()

			fv = FieldValue()
			fv.field = Field.objects.get(name='sex_offense')
			fv.value = line[6].strip(', ')
			fv.profile = profile
			fv.save()

			fv = FieldValue()
			fv.field = Field.objects.get(name='sex_offense_count')
			fv.value = line[7].strip(', ')
			fv.profile = profile
			fv.save()

			fv = FieldValue()
			fv.field = Field.objects.get(name='sex_offender_compliant')
			fv.value = line[8].strip(', ')
			fv.profile = profile
			fv.save()

			profile.save()

