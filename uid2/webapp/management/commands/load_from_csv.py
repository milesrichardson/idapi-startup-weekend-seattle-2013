import os
from datetime import datetime
from webapp.models import Profile, FieldValue, Field
from django.conf import settings
from subprocess import call
from django.core.management.base import CommandError, NoArgsCommand
from django.db import models
from dateutil.relativedelta import relativedelta
import csv
from subprocess import call

class Command(NoArgsCommand):
    help = 'load in data from csv'
    def handle_noargs(self, **options):
        # load in each of the rows of csv data and populate the database.
		fp = open('msor.csv', 'rb')
		reader = csv.reader(fp)

		last_name = Field.objects.get(name='last_name')
		first_name = Field.objects.get(name='first_name')
		address = Field.objects.get(name='address')
		sex_offense = Field.objects.get(name='sex_offense')
		sex_offense_count = Field.objects.get(name='sex_offense_count')
		sex_offender_complaint = Field.objects.get(name='sex_offender_compliant')

		i = 0

		for line in reader:
			# import every 200th element
			i += 1
			if i % 200 != 0:
				continue

			print "Processing data", line
			profile = Profile()
			profile.expiry_date = datetime.utcnow() + relativedelta(years=+1)	
			#profile.creation_date = datetime.utcnow()
			profile.save()
			
			# for reference
			# dataformat = ['Name','Address','City', 'St', 'Zip', 'County', 'Offense', 'Count', 'Compliant']

			fv = FieldValue()
			fv.field = last_name
			fv.value = line[0].split(',')[1] 
			fv.profile = profile
			fv.save()
			
			fv = FieldValue()
			fv.field = first_name
			fv.value = line[0].split(',')[0].rstrip(', ')
			fv.profile = profile
			fv.save()

			fv = FieldValue()
			fv.field = address
			address_value = ''
			for i in range(1, 6):
				address_value += line[i] + " "
			fv.value = address_value
			fv.profile = profile
			fv.save()

			fv = FieldValue()
			fv.field = sex_offense
			fv.value = line[6]
			fv.profile = profile
			fv.save()

			fv = FieldValue()
			fv.field = sex_offense_count
			fv.value = line[7]
			fv.profile = profile
			fv.save()

			fv = FieldValue()
			fv.field = sex_offender_complaint
			fv.value = line[8].strip(', ')
			fv.profile = profile
			fv.save()

			profile.save()

