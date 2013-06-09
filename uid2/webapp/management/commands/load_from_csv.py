import os
from datetime import datetime
from peteear.models import UserProfile
from django.conf import settings
from peteear.utils import deleteSong
from subprocess import call
from django.core.management.base import CommandError, NoArgsCommand
from dateutil.relativedelta import relativedelta
from time import sleep

class Command(NoArgsCommand):
    help = 'load in data from csv'
    def handle_noargs(self, **options):
        # load in each of the rows of csv data and populate the database.
