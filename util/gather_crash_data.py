# 
#
# gather_crash_data.py
#
# This will attempt to use a target application's bugs.json file to
# execute the app with each of the supposed crash-causing input files
# listed in the "bugs" field. If the input causes a crash, a stack
# trace is saved for any available threads.
# 
# You may have to point PYTHONPATH to where lldb and psutil modules are
# to be found.
#
# example use
#  PYTHONPATH=/p/to/llvm/lib/python3.7/site-packages python3  \
#     gather_crash_data.py ../cases/audiofile+0.3.6 bugs.json new.json
#
#


import argparse
import json
import multiprocessing as mp
import os
import signal
import sys
import time

import radhelp


# XXX if for some reason we need to run serially. 
def crash_worker(conj, arch, args, evars, resq):
	o = radhelp.run(conj, args, evars, arch, kind="llvm")
	resq.put(o)
	return

def main():
	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--verbose', action="store_true")
	aparse.add_argument('rootcase', help='path to case files')
	aparse.add_argument('infile', help='input bugs.json file')
	aparse.add_argument('outfile',help='output bugs.json file')
	cargs = aparse.parse_args()

	rootcase = cargs.rootcase
	oldjson = cargs.infile
	newjson = cargs.outfile
	verbose = cargs.verbose

	#arch = "x86_64-apple-macosx10.14.0"
	#arch = "x86_64-*-linux"
	#arch = "x86_64-*-linux*"
	arch = "x86_64-unknown-linux-gnu"

	#
	# bdata will contain the old json contents
	# and be updated with run data
	#
	bdata = None
	bugjson = os.path.join(rootcase, oldjson)

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

#		evars.append("{}={}".format(k.encode("utf-8"), bdata_evars[k].encode("utf-8", 'ignore')))
	print("evars: {}".format(evars))
#	evars = ["{}={}".format(k.encode("utf-8"),
#	  v.encode("utf-8", 'ignore')) for k,v in bdata_evars] 

	# You could spawn these all off, i think, but i worrie
	# about an app that only wants to be run one time by a user at a time.
	count = 0
	timesum = 0

	args = bdata.args()
	for cve in bdata.get_all_bug_labels():

		cinput = bdata.testcase(cve)

		testcase = os.path.join(rootcase, cinput)
		testcase = os.path.abspath(testcase)
		xargs = args
		xargs = xargs.replace("@@", testcase)
		xargs = xargs.split(" ")

		if verbose:
			print("Targeting {} using test case {} input to: app {}".format(cve, cinput, conj))


		# XXX: Am I really ok? 2 at the same time is ok, eh?
		resq = mp.Queue()
		p = mp.Process(target=crash_worker,
		  args=(conj, arch, xargs, evars, resq))
		p.start()
		t0 = time.time()
		p.join(15)
		t1 = time.time()

		tdiff = int(t1-t0)
		timesum = timesum + tdiff      
		count = count + 1
		if verbose:
			print("rough exec time: {} avg now: {}".format(tdiff, timesum/float(count)))

		# possibly make this deletion an argument (i.e., reset all
		# results switch)
		#del bdata["bugs"][cve]["crash"][arch]

		if bdata.bd["bugs"][cve]["crash"] is None:
			bdata.bd["bugs"][cve]["crash"] = {}
		bdata.bd["bugs"][cve]["crash"][arch] = {}
		if resq.empty():
			if verbose:
				print("results queue is empty, empty output for {}".format(cve))
			bdata.bd["bugs"][cve]["crash"][arch]["bt"] = None
		else:
			out = resq.get()
			bdata.bd["bugs"][cve]["crash"][arch]["bt"] = out

		radhelp.kill_child_processes(p, sig=signal.SIGTERM)	
		p.terminate()

		try:
			os.unlink("/tmp/ignorethis")	
		except Exception:
			pass

	bdata.write_json(newjson)


if __name__ == '__main__':
	main()
