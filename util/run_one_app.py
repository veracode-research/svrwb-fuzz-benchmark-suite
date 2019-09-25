# 
#
# run_one_app.py
#
# This will attempt to run an application under a given bugs.json
# with the input supplied by the user of this script. It will then
# optionally compare it with the existing cases, to see if it is
# new. It will print the JSON formatting, as well.
#


import argparse
import json
import os
import sys

import radhelp



def main():
	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--verbose', verbose output', action="store_true")
	aparse.add_argument('--compare', action="store_true")
	aparse.add_argument('root', help='path to test case root')
	aparse.add_argument('infile', help='input bugs.json file')
	aparse.add_argument('appinput', help='input file you want to test')
	cargs = aparse.parse_args()

	verbose = cargs.verbose
	docompare = cargs.compare
	rootcase = cargs.root
	bugsjson = cargs.infile
	test_input = cargs.appinput

	
	#arch = "x86_64-apple-macosx10.14.0"
	#arch = "x86_64-*-linux"
	#arch = "x86_64-*-linux*"
	arch = "x86_64-unknown-linux-gnu"

	#
	# bdata will contain the old json contents
	# and be updated with run data
	#
	bdata = None
	bugjson = os.path.join(rootcase, bugsjson)

	bdata = radhelp.bugdata_from_json(bugjson)
	if bdata == None:
		print("JSON file failed to load")
		return

	

	#conj = os.path.join(rootcase, bdata.app_path().decode('utf8', errors='ignore'))
	conj = os.path.join(rootcase, bdata.app_path())
	bdata_evars = bdata.evars()
	evars = []
	for k in bdata_evars.keys():
		evars.append("{}={}".format(k, bdata_evars[k]))

	if verbose == True:
		print("evars: {}".format(evars))


	# You could spawn these all off, i think, but i worrie
	# about an app that only wants to be run one time by a user at a time.
	count = 0
	timesum = 0

	args = bdata.args()
	args = args.replace("@@", test_input) 
	args = args.split(" ")
	o = radhelp.run(conj, args, evars, arch, kind="llvm")

	if "thd0" not in o.keys():
		print("No 'thd0' in the results... total 'o' is {}".format(o))
		sys.exit(0)

	o = o["thd0"]
	all_crashes = bdata.get_crashes(arch)
	for x in all_crashes:
		if len(x.keys()) == 0:
			continue
		x = x["thd0"]
		if len(x) != len(o):
			continue
		if len(x) == len(o):
			same = True
			for z in range(len(x)):
				if x[z] != o[z]:
					same = False
					break
			if same:
				sys.exit(1)
	sys.exit(2)
			

if __name__ == '__main__':
	main()
