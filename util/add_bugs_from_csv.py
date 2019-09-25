# 
# add_bugs_from_csv.py
#
# Supply a, currently, 2 part CSV file with bug_label,file_name as
# the rows. These will then be added to a BugData object to be
# written out to JSON file.
#
# ...should make this more flexible, but so it goes...
#


import argparse
import csv
import json
import os
import sys

import radhelp


def main():
	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--verbose', help='verbose', action="store_true")
	aparse.add_argument('in_bugs_json', help='path to input bugs.json file')
	aparse.add_argument('in_csv', help='bugname,bugfile CSV listing')
	aparse.add_argument('out_bugs_json', help='output json file w/ bugs')
	cargs = aparse.parse_args()

	verbose = cargs.verbose
	bugsjson = cargs.in_bugs_json
	bugscsv = cargs.in_csv
	outjson = cargs.out_bugs_json

	bdata = None
	bdata = radhelp.bugdata_from_json(bugsjson)
	if bdata == None:
		print("JSON file failed to load")
		return

	with open(bugscsv, 'r') as ch:
		rdr = csv.reader(ch)
		for row in rdr:
			if len(row) != 2:
				continue
			cve_label = row[0]
			test_input_sample = row[1]
			bdata.add_bug(cve_label, crash=None, description=None,
			  testcase=test_input_sample)
	bdata.write_json(outjson)
	sys.exit(0)
			

if __name__ == '__main__':
	main()
