#!/usr/bin/python

__author__ = 'uolter'

CSV_OUT_LANG_BY_COURSE = 'course_lang.csv'


prog_lang = set(['java', 'c++', 'perl', 'c', 'javascript', 'scala', 'actionscript',' bash','c#', 'clojure',' coffeescript', 'dart', 'delphi', 'emacscript',
				'erlang','f','f#','haskell', 'lisp', 'lua', 'objective-c', 'perl', 'php', 'python', 'r', 'ruby', 'smalltalk'])

import urllib2
import json
import re
import csv
import sys

def get_prog_lng(url):

	req = urllib2.Request(url)
	opener = urllib2.build_opener()
	try:
		f = opener.open(req)
		_json = json.loads(f.read())
		text = ' ' + _json['about_the_course']
		text += _json['short_description']
		text += ' ' + _json['course_format']
		text += ' ' + _json['recommended_background']
		text = text.lower()

		wintext = set(re.findall(r"[\w']+", text))
	
		return list(prog_lang & wintext)
	except ValueError, e:
		print 'Error calling %s: %s' %(url, e)
	

def save_csv(data, file_name):
	writer = csv.writer(open(file_name, "wb"))
	writer.writerows(data)

def all_acourses(courses):

	for c in courses:
		lang = get_prog_lng(c[3])
		if lang:
			row = []
			row.append(c[0])
			row.append(c[1])
			row.append(', '.join(lang))
			
			yield row

def main():
	
	# courses = csv.reader(open(CSV_COURSES_FILE, "rb"))
	courses = csv.reader(sys.stdin)
	
	course_lang = (c for c in all_acourses(courses))
	
	save_csv(course_lang, CSV_OUT_LANG_BY_COURSE)
		



if __name__ == '__main__':

	main()