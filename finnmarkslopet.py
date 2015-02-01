#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os 			# Files and folder manipulations
import re 			# Regular expressions
import csv 			# CSV file manipulations 
import pywikibot	# Wikidata interactions

class Race(object):
	"""An edition of the Finnmarkslopet."""

	# Faire un CSV par course
	#colonnes : numéro de dossard, nom du musher, classement final, lieu d'abandon le cas échéant, source
	
	mushers = {}
	
	def __init__(self,folder_name):
		self.folder_name	= folder_name
		self.year, self.fl	= re.match("(?P<year>[0-9]{4}) (?P<fl>(FL500|FL1000|FL Junior))", folder_name).group("year","fl")

		if self.fl == "FL500":
			self.classname = "Limited class"
			self.fullracename = self.folder_name + " - " + self.classname
		elif self.fl == "FL1000":
			self.classname = "Open class"
			self.fullracename = self.folder_name + " - " + self.classname
		else:
			self.classname = ""
			self.fullracename = self.folder_name

		self.qid = race_qids[self.folder_name]['qid'] # Qid on Wikidata
		self.rid = race_qids[self.folder_name]['rid'] # race id on the official site

	def list_mushers(self):
		"""Lists the mushers who have entered a race and puts them in a dictionary with their """
		with open(root_dir + self.folder_name + "/" + self.fullracename + " entrants.csv", 'r') as csv_race_entrants:
			reader = csv.DictReader(csv_race_entrants)

			for row in reader:
				this_musher = Musher(row['Name'], row['Country'], row['Hometown'])
				self.mushers.update({ int(re.match(r'\d+', row['Nr']).group()): this_musher})

		csv_race_entrants.closed

class Musher(object):
	"""A musher participating in an edition of the Finnmarkslopet"""
	def __init__(self,name, country, hometown):
		self.name = name
		self.country = country
		self.hometown = hometown

		if self.name in musher_qids and len(musher_qids[self.name]):
			self.qid = musher_qids[self.name]
			old_mushers.update({self.qid: self.name})
		else:
			if self.name not in new_mushers:
				new_mushers.append(self.name)

def initial_checks():
	"""Perform a series of checks to be sure the race data is good."""
	print("{} race editions found.".format(len(race_editions)))

	filecount_errors = 0
	for race in race_editions:
		files_count = len(os.listdir(race))
		if files_count != 5:
			print("The folder {} has {} files in it.".format(race,files_count))
			filecount_errors += 1
	if filecount_errors > 0:
		print("{} race folders don't have the expected number of files.".format(filecount_errors))
	else:
		print("All race folders have the expected number of files.")

def import_ids():
	"""
	1. Import the ids of the races on Wikidata and on the official site.
	2. Import the qids of the mushers on Wikidata
	"""
	with open(root_dir + 'finnmarkslopet-qid.csv', 'r') as csv_race_ids:
		reader = csv.DictReader(csv_race_ids)
		for row in reader:
			race_qids[row['race']] = { 'rid': row['rid'], 'qid': row['qid'] }

	csv_race_ids.closed

	with open (root_dir + 'mushers-qid.csv', 'r') as csv_musher_ids:
		reader = csv.DictReader(csv_musher_ids)
		for row in reader:
			musher_qids.update({row['label']: row['qid'] })

	csv_musher_ids.closed

def list_new_mushers():
	"""Writes down the mushers without Qid in a text file."""
	with open (root_dir + 'new_mushers.txt', 'w') as txt:
		for m in new_mushers:
			txt.write(m + "\n")
	txt.closed

# running the app
root_dir = os.environ['HOME'] + "/Dropbox/finnmarkslopet/"
race_editions = filter(os.path.isdir, [os.path.join(root_dir, f) for f in os.listdir(root_dir)])
race_qids = {}
musher_qids = {}

new_mushers = []
old_mushers = {}

#initial_checks()
import_ids()

#**TEST** 
"""
test_ride = Race("1990 FL500")

test_ride.list_mushers()

print(test_ride.mushers)
print(test_ride.mushers[17].name)

#"""

for race in race_editions:
	this_race = Race(os.path.basename(race))
	this_race.list_mushers()

new_mushers.sort()
list_new_mushers()

#print old_mushers
#print len(old_mushers)

# http://www.finnmarkslopet.no/race/results/results.jsp?lang=en&rid=3