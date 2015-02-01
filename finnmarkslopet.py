#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os 			# Files and folder manipulations
import re 			# Regular expressions
import csv 			# CSV file manipulations 
import pywikibot	# Wikidata interactions

class Race(object):
	"""An edition of the Finnmarkslopet."""
	
	def __init__(self,folder_name):
		self.folder_name	= folder_name
		self.year, self.fl	= re.match("(?P<year>[0-9]{4}) (?P<fl>(FL500|FL1000|FL Junior))", folder_name).group("year","fl")

		if self.fl == "FL500":
			self.classname = "Limited class"
		elif self.fl == "FL1000":
			self.classname = "Open class"
		else:
			self.classname = ""

	def list_mushers():



class Musher(object):
	"""A musher participating in an edition of the Finnmarkslopet"""
	def __init__(self,name, country, hometown):


def initial_checks():
	"""Perform a series of checks to be sure the race data is good."""
	print "{} race editions found.".format(len(race_editions))

	filecount_errors = 0
	for race in race_editions:
		files_count = len(os.listdir(race))
		if files_count != 5:
			print "The folder {} has {} files in it.".format(race,files_count)
			filecount_errors += 1
	if filecount_errors > 0:
		print "{} race folders don't have the expected number of files.".format(filecount_errors)
	else:
		print "All race folders have the expected number of files."


# running the app
root_dir = os.environ['HOME'] + "/Dropbox/finnmarkslopet/"
race_editions = filter(os.path.isdir, [os.path.join(root_dir, f) for f in os.listdir(root_dir)])

#initial_checks()


#extension = os.path.splitext(filename)[1]

#	if extension == ".csv":
#		full_filename = root_dir + filename


#**TEST** 
test_ride = Race("1990 FL500")
print test_ride.year
print test_ride.fl
print test_ride.classname


# Faire un CSV par course
#colonnes : numéro de dossard, nom du musher, classement final, lieu d'abandon le cas échéant, source

# http://www.finnmarkslopet.no/race/results/results.jsp?rid=3