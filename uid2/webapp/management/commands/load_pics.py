from datetime import datetime
from webapp.models import Profile, FieldValue, Field
from django.conf import settings
from subprocess import call
from django.core.management.base import CommandError, NoArgsCommand
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.utils.timezone import utc
from dateutil.relativedelta import relativedelta
import os
import csv
import json
from subprocess import call
import criminal_scrape

class Command(NoArgsCommand):
	#@transaction.commit_manually
    help = 'load in data from csv'
    def handle_noargs(self, **options):
        # load in each of the rows of csv data and populate the database.

		query = 'Donaldson'
		results = criminal_scrape.get_results(firstname='', lastname=query, offline=False)
		results = json.loads(results)
		#keys = ['status', 'next_page', 'current_page', 'records', 'total_records', 'msg'	# for reference
		results = results['records']

		fields = ['last_name', 'first_name', 'sex_offense', 'mugshot_url']
		"""
		for fieldname in fields:
			field = Field()
			field.name = fieldname
			field.save()

		field = Field()
		field.name = 'mugshot_url'
		field.save()
		"""

		user = User.objects.get(id=1)

		last_name = Field.objects.get(name='last_name')
		first_name = Field.objects.get(name='first_name')
		sex_offense = Field.objects.get(name='sex_offense')	 #TODO - not actualy sex offense; change to general crimes
		mugshot_url = Field.objects.get(name='mugshot_url')

		for result in results:
			profile = Profile()
			profile.expiry_date = datetime.utcnow().replace(tzinfo=utc) + relativedelta(years=+1)	
			#profile.creation_date = datetime.utcnow()
			profile.save()

			fullname = str(result['name'])
			sex_offenses = result['charges']
			sex_offense = result['charges'][0]
			mugshot = str(result['mugshot'])

			print '\n'.join([fullname, sex_offense, mugshot])
			print ""

			fv = FieldValue()
			fv.field = last_name
			fv.value = fullname.split()[0]
			fv.save()

			fv = FieldValue()
			fv.field = first_name
			fv.value = fullname.split()[-1]
			fv.save()

			fv = FieldValue()
			fv.field = sex_offense
			fv.value = str(result['charges'][0])
			fv.save()

			fv = FieldValue()
			fv.field = mugshot_url
			fv.value = mugshot
			fv.save()

			profile.save()

