import argparse
import os
import sys

import radhelp

application = "ytnef"
app_path = "ytnef-1.9.2/install/bin/ytnefprint"
app_version = "1.9.2"
app_source = "https://github.com/Yeraze/ytnef/tree/master/ytnef"


def main():
	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('outfile', help='path of generated JSON file')
        args = aparse.parse_args()

	out_file = args.outfile

	app_data = radhelp.Bugdata(application, app_path, None, None, source=app_source, version=app_version)
	# Adjust these as needed (i should just make it more stdin read)
	bugs = {}
	while True:
		print("CVE ID? PR ID? or similar?")
		line = sys.stdin.readline().strip()
		if line == '':
			break
		cve = line

#		print("Url to description?")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs[cve]["description"] = line
#		print("Arguments?")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs[cve]["args"] = line
#		bugs[cve]["args"] = None 
#		print("Url to testcase? ")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs[cve]["testcase_url"] = line
#		bugs[cve]["testcase_url"] = '' 
		print("testcase? ")
		line = sys.stdin.readline().strip()
		testcase = None
		if line != '':
			testcase = line

		description = "https://rt.perl.org/Public/Bug/Display.html?id={}".format(cve)

		app_data.add_bug(cve, {}, description, testcase)

	app_data.write_json(out_file)


if __name__ == '__main__':
	main()
