import argparse
import os
import sys

import radhelp

def main():
	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--verbose')
	aparse.add_argument('path', help='path to test-case root')
	aparse.add_argument('bugjson', help='input bugs.json file')
	cargs = aparse.parse_args()

	rootpath = cargs.path
	bjson = cargs.bugjson
	if radhelp.potpourri.case_has_app_built(rootpath, bjson) == True:
		if cargs.verbose:
			print("built")
		sys.exit(0)
	if cargs.verbose:
		print("not built")
	sys.exit(-1)

if __name__ == '__main__':
	main()

