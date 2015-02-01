#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Create a CSV with each race since 1990, with the rid and the Wikidata qid.
"""

import os
import requests
from bs4 import BeautifulSoup
import re
import csv

race_qids= {}

root_dir = os.environ['HOME'] + "/Dropbox/finnmarkslopet/"
with open(root_dir + 'finnmarkslopet-qid-temp.csv', 'r') as csv_in:
	reader = csv.reader(csv_in)
	for row in reader:
		race_qids[row[1]] = row[0]

csv_in.closed

root_url = 'http://www.finnmarkslopet.no'
index_url = root_url + '/rhist/results.jsp?lang=en'


response = requests.get(index_url)
soup = BeautifulSoup(response.text)

table = soup.select('.winners tr')
table.pop(0)

with open(root_dir + 'finnmarkslopet-qid.csv', 'w') as csv_out:
	fieldnames = ["race", "rid", "qid"]
	writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
	writer.writeheader()

	for row in table:
		year = row.strong.string
		links = row.find_all("a")

		writer.writerow({
			'race': year + ' FL1000',
			'rid': re.search("openRaceWnd\('(?P<id>[0-9]*)'\)", links[0].get('href')).group("id"),
			'qid':race_qids[year + " FL1000"]
		});

		if len(links) > 1:
			writer.writerow({
				'race': year + ' FL500',
				'rid': re.search("openRaceWnd\('(?P<id>[0-9]*)'\)", links[1].get('href')).group("id"),
				'qid':race_qids[year + " FL500"]
			});

		if len(links) == 3:
			writer.writerow({
				'race': year + ' FL Junior',
				'rid': re.search("openRaceWnd\('(?P<id>[0-9]*)'\)", links[2].get('href')).group("id"),
				'qid':race_qids[year + " FL Junior"]
			});

csv_out.closed