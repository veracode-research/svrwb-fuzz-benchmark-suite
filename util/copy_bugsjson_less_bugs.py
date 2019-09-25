# 
# copy_bugs_less_json.py
#
# Copy a bugs.json but do not include any of the bugs, just the application
# specific metadata.
#


import argparse
import json
import os
import sys

import radhelp


def main():
	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--verbose', help='verbose', action="store_true")
	aparse.add_argument('infile', help='path to input bugs.json file')
	aparse.add_argument('outfile', help='output json file w/o crashes')
	cargs = aparse.parse_args()

	verbose = cargs.verbose
	bugsjson = cargs.infile
	outjson = cargs.outfile

	bdata = None
	bdata = radhelp.bugdata_from_json(bugsjson)
	if bdata == None:
		print("JSON file failed to load")
		return
	bdata.remove_all_bugs()
	bdata.write_json(outjson)
	sys.exit(0)
			

if __name__ == '__main__':
	main()
