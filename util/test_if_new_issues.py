
import argparse
import json
import os
import sys

import radhelp

def main():
	#arch = "x86_64-apple-macosx10.14.0"
	#arch = "x86_64-*-linux"
	#arch = "x86_64-*-linux*"
	arch = "x86_64-unknown-linux-gnu"

	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--verbose', help='enable verbose output',
	  action="store_true")
	aparse.add_argument('--compare',
	  help='enable JSON generation for the input', action="store_true")
	aparse.add_argument('root', help='path to test case root')
	aparse.add_argument('injson', help='input bugs.json file')
	aparse.add_argument('file_list', help='a file that contains a list of intended inputs')
	cargs = aparse.parse_args()

	verbose = cargs.verbose
	docompare = cargs.compare
	rootcase = cargs.root
	bugsjson = cargs.injson
	file_list = cargs.file_list
	files_to_attempt = []

	with open(file_list, 'r') as oh:
		files_to_attempt = [x.strip() for x in oh.readlines()]
	

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

	already_have = []
	new_to_us = []
	all_crashes = bdata.get_crashes(arch)

	for tt in files_to_attempt:
		args = bdata.args()
		args = args.replace("@@", tt) 
		args = args.split(" ")

		o = radhelp.run(conj, args, evars, arch, kind="llvm")
		if "thd0" not in o.keys():
		#	print("{} no crash".format(tt))
			continue
		o = o["thd0"]

		# For any of the crashes we already know of, does this cause a knew one?
		for x in all_crashes:
			if len(x.keys()) == 0:
				continue

			x = x["thd0"]

			# different size trace? assume not the same
			if len(x) != len(o):
				continue

			# same trace size
			if len(x) == len(o):
				if len(x) == 0:
					continue

				same = True
				for z in range(len(x)):
					if x[z] != o[z]:
						same = False
						break
				if same:
					already_have.append(tt)
					break
	already_have = list(set(already_have))	
	new_to_us = list(set(files_to_attempt)-set(already_have))

	print("already have:\n{}\n".format("\n".join(already_have)))
	print("new to use:\n{}\n".format("\n".join(new_to_us)))
	
if __name__ == '__main__':
	main()
