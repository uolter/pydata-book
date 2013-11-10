#!/usr/bin/python

import csv
import sys
import matplotlib.pyplot as plt
from pandas import Series

__author__ = 'uolter'


def count():

	courses = csv.reader(sys.stdin)

	lang_counter = {}

	for c in courses:
		languages = c[2]
		for l in languages.split(','):
			l = l.replace(" ", "").lower()
			lang_counter.setdefault(l, [])
			lang_counter[l].append(c[1])

	return lang_counter


def show_graph(lang_count):

	tot = [t[1] for t in lang_count]

	index = [i[0] for i in lang_count]

	series =Series(tot, index= index)
	series.sort()
	Series.plot(series, kind='bar')

	plt.show()


def main():
	lang_count = count()

	for l in lang_count: print l, len(lang_count[l])

	show_graph(
		[(l, len(lang_count[l])) for l in lang_count ]
		)

if __name__ == '__main__':
	main()
