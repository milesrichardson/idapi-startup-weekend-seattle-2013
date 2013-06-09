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
Download [msor.csv](http://dl.dropboxusercontent.com/u/27627620/id/msor.csv) and put it in the folder above your git folder

	usage: mo\_sexoffender.py [-h] [--firstname [FIRSTNAME]]
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


