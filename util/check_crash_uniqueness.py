#
# check_crash_uniqueness.py
#
# For some differening definitions of equal, supply some methods for
# determining which crashes in a bugs.json are unique versus duplicates.
#
#

import argparse
import json
import sys

import radhelp

vvv = False

def remove_no_crashes(bdata, arch):
	removals = []
	for cve in bdata.get_all_bug_labels():
		if bdata.has_crash(cve, arch) == False:
			if vvv:
				print("No crash: {} on {}".format(cve, arch))
			removals.append(cve)
	for x in removals:
		bdata.remove_bug(x)
	return bdata

def uniq_by_backtrace_no_pc(bdata, arch):
	global_dupes = []
	for label in bdata.get_all_bug_labels():
		trace1 = bdata.get_trace(label, arch)
		assert(trace1 is not None), "lost trace1 after deletion"

		# it's a known duplicate, don't uniq it
		if label in global_dupes:
			continue

		trace1 = radhelp.parse_trace(trace1, 'llvm')
		trace1 = [(x[0], x[2], x[3]) for x in trace1]


		tr1set = set(trace1)
		iter_dupe = False
		dupes = []
		for label_2 in bdata.get_all_bug_labels():
			if label == label_2:
				continue

			trace2 = bdata.get_trace(label_2, arch)
			assert(trace2 is not None), "lost trace2 after deletion"

			trace2 = radhelp.parse_trace(trace2, 'llvm')
			trace2 = [(x[0], x[2], x[3]) for x in trace2]

			# Different trace length => not same bt
			if len(trace1) != len(trace2):
				continue

			tr2set = set(trace2)

			sumdiff = list(tr1set - tr2set) + list(tr2set - tr1set)

			if len(sumdiff) == 0:
				dupes.append(label_2)
				iter_dupe = True
				continue
		global_dupes.extend(dupes)
		global_dpes = list(set(global_dupes))
		if iter_dupe == False:
			print("unique: {}".format(label))
		else:
			print("dupes: {}, dupes: {}".format(label, dupes))

def uniq_by_backtrace(bdata, arch):
	global_dupes = []
	for label in bdata.get_all_bug_labels():
		trace1 = bdata.get_trace(label, arch)
		assert(trace1 is not None), "lost trace1 after deletion"

		# it's a known duplicate, don't uniq it
		if label in global_dupes:
			continue

		tr1set = set(trace1)
		iter_dupe = False
		dupes = []
		for label_2 in bdata.get_all_bug_labels():
			if label == label_2:
				continue

			trace2 = bdata.get_trace(label_2, arch)
			assert(trace2 is not None), "lost trace2 after deletion"

			# Different trace length => not same bt
			if len(trace1) != len(trace2):
				continue

			tr2set = set(trace2)

			sumdiff = list(tr1set - tr2set) + list(tr2set - tr1set)
			if len(sumdiff) == 0:
				dupes.append(label_2)
				iter_dupe = True
				continue
		global_dupes.extend(dupes)
		global_dpes = list(set(global_dupes))
		if iter_dupe == False:
			print("unique: {}".format(label))
		else:
			print("dupes: {}, dupes: {}".format(label, dupes))


def main():

	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--verbose', default=False, action='store_true')
	aparse.add_argument('bugsjson', help='path to bugs.json file')

	uniq_group = aparse.add_mutually_exclusive_group(required=True)
	uniq_group.add_argument('--by-backtrace', action='store_true')	
	uniq_group.add_argument('--by-backtrace-no-pc', action='store_true')
	args = aparse.parse_args()

	bugjson = args.bugsjson
	vvv = args.verbose

	#arch = "x86_64-apple-macosx10.14.0"
	arch ="x86_64-unknown-linux-gnu"

	bdata = radhelp.bugdata_from_json(bugjson)
	if bdata is None:
		print("Failed to load the json: {}".format(bugjson))
		sys.exit(1)

	# if it did not crash, then we have nothing to go on
	bdata = remove_no_crashes(bdata, arch)

	if args.by_backtrace == True:
		uniq_by_backtrace(bdata, arch)
	elif args.by_backtrace_no_pc == True:
		uniq_by_backtrace_no_pc(bdata, arch)

	sys.exit(0)


if __name__ == '__main__':
	main()
