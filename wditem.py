#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pywikibot	# Wikidata interactions - https://www.mediawiki.org/wiki/Manual:Pywikibot/Wikidata

class WDitem(object):
	"""A wikidata item"""

	latin_languages = ["af", "an", "ast", "bar", "bm", "br", "ca", "co", "cs", "cy", "da", "de", "de-at", "de-ch", "en",
	 				   "en-ca", "en-gb", "eo", "es", "et", "eu", "fi", "fr", "frc", "frp", "fur", "ga", "gd", "gl",
	 				   "gsw", "hr", "hu", "ia", "id", "ie", "io", "it", "jam", "kab", "kg", "la", "lb", "li", "lij",
	 				   "lt", "lv", "mg", "nap", "nb", "nds", "nds-nl", "nl", "nn", "nrm", "min", "ms", "oc", "pap",
	 				   "pcd", "pl", "pms", "prg", "pt", "pt-br", "rgn", "rm", "ro", "sc", "scn", "sco", "sk", "sr-el",
	 				   "sv", "sw", "tr", "vec", "vi", "vls", "vmf", "vo", "wa", "wo", "zu"]

	def __init__(self,qid):
		self.qid = qid.upper()

		self.wd_item = pywikibot.ItemPage(repo, self.qid)
		self.wd_item.get()

	def check_latin_labels(self):
		""" Checks if all labels in languages that use the latin alphabet are the same"""
		self.latin_labels =  { k:v for (k,v) in self.wd_item.labels.items() if k in self.latin_languages }
		
		if len(set(self.latin_labels.values()))==1:
			return True
		else:
			print("== {} has different label values in latin languages ==".format(self.qid))
			print(self.wd_item.labels)
			print("Total : {}".format(len(self.wd_item.labels)))
			return False