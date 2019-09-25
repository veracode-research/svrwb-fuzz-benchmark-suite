#
# Helper script to dump the execution string one
# would use based on the bugs.json file.
#
# ENV_VARS... APP ARGS...
#
#

import argparse
import json
import sys

import radhelp

def main():
	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('json', help='bugs.json file')

	cargs = aparse.parse_args()
	bd = radhelp.bugdata_from_json(cargs.json)

	app_path = bd.app_path()
	evars = bd.evars()
	args = bd.args()
	
	ev = "" 
	if evars:	
		for k in evars.keys():
			ev = ev + "{}={} ".format(k, evars[k])
	print("{} {} {}".format(ev, app_path, args))

	sys.exit(0)


if __name__ == '__main__':
	main()
