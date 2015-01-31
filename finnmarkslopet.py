#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import csv
import pywikibot

root_dir = os.environ['HOME'] + "/Dropbox/finnmarkslopet/"
race_editions = filter(os.path.isdir, [os.path.join(root_dir, f) for f in os.listdir(root_dir)])

def initial_checks():
	print "{} race editions found.".format(len(race_editions))

	filecount_errors = 0
	for race in race_editions:
		files_count = len(os.listdir(race))
		if files_count != 5:
			print "The folder {} has {} files in it.".format(race,files_count)
			filecount_errors += 1
	if filecount_errors > 0:
		print "{} race folders don't have the expected number of files."
	else:
		print "All race folders have the expected number of files."







# running the app
initial_checks()



#extension = os.path.splitext(filename)[1]

#	if extension == ".csv":
#		full_filename = root_dir + filename


#**TEST** 
test_ride = "1990 FL500"


# Faire un CSV par course
#colonnes : numéro de dossard, nom du musher, classement final, lieu d'abandon le cas échéant, source

# http://www.finnmarkslopet.no/race/results/results.jsp?rid=3