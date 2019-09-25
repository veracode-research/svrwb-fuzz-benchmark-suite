#
# bjdiff.py
#
# A weak attempt at diffing two bugs.json files. The primary focus is,
# of course, the bugs/crashes... otherwise, there is no sense in diffing
# the two, really.
#

import argparse
import radhelp

def diff_by_backtrace(aobj, bobj, arch):
	aset = set(aobj.get_all_bug_labels())
	bset = set(bobj.get_all_bug_labels())

	aminusb = list(aset - bset)
	bminusa = list(bset - aset)
	print("a - b: {}".format(aminusb))
	print("b - a: {}".format(aminusb))

	aset &= bset
	alist = list(aset)
	for cve in alist:
		traceA = aobj.get_parsed_trace(cve, arch)
		traceB = bobj.get_parsed_trace(cve, arch)

		if traceA == traceB:
			print("{}: SAME (-address) trace: {}".format(bobj.application(),
			  bobj.bd["bugs"][cve]["crash"][arch]["bt"]))
			continue

		print("{}: DIFF trace A: {}".format(cve, traceA))
		print("{}: DIFF trace B: {}".format(cve, traceB))
		print("----------------------------------------")

def diff_by_backtrace_no_pc(aobj, bobj, arch):

	aset = set(aobj.get_all_bug_labels())
	bset = set(bobj.get_all_bug_labels())

	aminusb = list(aset - bset)
	bminusa = list(bset - aset)
	print("a - b: {}".format(aminusb))
	print("b - a: {}".format(aminusb))

	aset &= bset
	alist = list(aset)
	for cve in alist:
		traceA = aobj.get_trace(cve, arch)
		traceB = bobj.get_trace(cve, arch)

		traceA = radhelp.parse_trace(traceA, 'llvm')
		traceA = [(x[0], x[2], x[3]) for x in traceA]
		traceB = radhelp.parse_trace(traceB, 'llvm')
		traceB = [(x[0], x[2], x[3]) for x in traceB]

		if traceA == traceB:
			print("{}: SAME (-address) trace: {}".format(bobj.application(),
			  bobj.bd["bugs"][cve]["crash"][arch]["bt"]))
			continue

		print("{}: DIFF trace A: {}".format(cve, traceA))
		print("{}: DIFF trace B: {}".format(cve, traceB))
		print("----------------------------------------")

def main():
	aparse = argparse.ArgumentParser(description="diff 2 bug.json files")
	aparse.add_argument('--arch', nargs="?",
	  default="x86_64-unknown-linux-gnu",
	  help='arch triple, e.g., x86_64-unknown-linux-gnu')
	uniq_group = aparse.add_mutually_exclusive_group(required=True)
	uniq_group.add_argument('--by-backtrace', action='store_true')
	uniq_group.add_argument('--by-backtrace-no-pc', action='store_true')
	aparse.add_argument('first', help='a.json')
	aparse.add_argument('second', help='b.json')
	args = aparse.parse_args()

	arch = args.arch
	print("Set arch to: {}".format(arch))

	ajson = args.first
	bjson = args.second

	aobj = radhelp.bugdata_from_json(ajson)
	bobj = radhelp.bugdata_from_json(bjson)

	if args.by_backtrace == True:
		diff_by_backtrace(aobj, bobj, arch)	
	elif args.by_backtrace_no_pc == True:
		diff_by_backtrace_no_pc(aobj, bobj, arch)	

if __name__ == '__main__':
	main()
