import argparse
import json
import os
import sys

import radhelp


application = "perl5.21.7"
app_path = "install/usr/local/bin/perl5.21.7"
app_version = "5.21.8"
app_source = "https://www.cpan.org/src/5.0/perl-5.21.7.tar.bz2"


def main():
        aparse = argparse.ArgumentParser(description="")
        aparse.add_argument('outfile', help='path of generated JSON file')
        aparse.add_argument('buglist', help='file with list of ids')
        args = aparse.parse_args()
	out_file = args.outfile
	buglist_file = args.buglist

	rtps = []
	with open(buglist_file, 'r') as ih:
		rtps = [x.strip() for x in ih.readlines()]
		
	app_data = radhelp.Bugdata(application, app_path, None, None, source=app_source, version=app_version)
	bugs = {}
	for k in rtps:
		f = k
		f = f.replace("rtp_", "RTP-")
		cve = f	
		description = "https://rt.perl.org/Public/Bug/Display.html?id={}".format(cve.replace("RTP-", ""))
#		print("Url to description?")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs[cve]["description"] = line
#		print("Arguments?")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs["args"] = line
#		bugs[cve]["args"] = None 
#		print("Url to testcase? ")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs[cve]["testcase_url"] = line
		bugs[cve]["testcase_url"] = '' 
		print("testcase? ")
		testcase = k 
                app_data.add_bug(cve, {}, description, testcase)

	app_data.write_json(out_file)


if __name__ == '__main__':
	main()
