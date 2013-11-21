import json
import csv
import sys

__author__ = 'uolter'

OUT_CSV_FILE = 'courses.csv'

# tech categories a course should belong
cats={12:'cs-programming', 4: 'infotech', 5:'math' ,16:'stats', 11:'cs-systems', 15:'ee'}

def save_csv(topics):

	writer = csv.writer(open(OUT_CSV_FILE ,'w'))
	
	for t in topics:
		# consider only courses in the tech categoris.
		if topics[t].get('cats') and not set(topics[t]['cats']).isdisjoint(set(cats.keys())):
			row = []
			row.append(topics[t]['short_name'].encode("utf-8"))
			row.append(topics[t]['name'].encode("utf-8"))
			row.append(topics[t]['language'].encode("utf-8"))
			row.append('https://www.coursera.org/maestro/api/topic/information?topic-id=%s' 
				%topics[t]['short_name'].encode("utf-8"))
			writer.writerow(row)


def main():

	infile = sys.stdin	
	## Get the infile
	data = json.load(infile)

	topics = data['topics']
	save_csv(topics)


if __name__ == '__main__':

	main()
