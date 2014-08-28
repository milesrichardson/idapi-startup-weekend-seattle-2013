WHAT IS THIS?
===================
This was the result of Startup Weekend Seattle, Summer 2013, hosted at Redfin offices. We built (the beginnings of) an API for background checks. The model was pretty much the same as www.checkr.io (recent YC company). 

We won 1st place for pitches, but did not place in final voting with the judges, who saw the business model as non-defensible.

untitled-identity-2-
====================

Jon Jia, Alan Ni, Miles Richardson, Michael Zhao

Change this later.


scrape.py
=========
Run `./scrape.py` and it defaults to a search of John Smith in California

OR

Run `./scrape.py --firstname John --lastname Smith --statecode CA` to explicitly specify a person


mo\_sexoffender.py
===================
Look up sex offenders in Missouri by first and/or last name and narrow down results by 'all', 'address', 'offense'

Download [msor.csv](http://dl.dropboxusercontent.com/u/27627620/id/msor.csv) and put it in your git folder

	usage: mo_sexoffender.py [-h] [--firstname [FIRSTNAME]]
							 [--lastname [LASTNAME]] [--selector [SELECTOR]]

	Get Missouri Sex Offender Report

	optional arguments:
	  -h, --help            show this help message and exit
	  --firstname [FIRSTNAME], -first [FIRSTNAME]
							First Name of Person
	  --lastname [LASTNAME], -last [LASTNAME]
							Last Name of Person
	  --selector [SELECTOR], -selector [SELECTOR]
							Type of data: all, address, or offense


criminal\_scrape.py
====================
Look up national criminal records. Specify data source yourself or check all sources


	usage: criminal_scrape.py [-h] [--firstname [FIRSTNAME]]
							  [--lastname [LASTNAME]] [--source [SOURCE]]

	Get Criminal Records

	optional arguments:
	  -h, --help            show this help message and exit
	  --firstname [FIRSTNAME], -first [FIRSTNAME]
							First Name of Person
	  --lastname [LASTNAME], -last [LASTNAME]
							Last Name of Person
	  --source [SOURCE], -source [SOURCE]
							Search all 167 sources (max of 1 request per second)
	  --viewsources, -viewsources
							View data sources for criminal checks

