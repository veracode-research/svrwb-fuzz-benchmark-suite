import sys
import os
import json
from shutil import copyfile


with open("bugs.json", "r") as rh:
	in_map = json.load(rh)
	rm_keys = []
	for CVE in in_map["bugs"].keys():
		if os.path.exists("tcpdump-4.9.1/tests/{}".format(in_map["bugs"][CVE]["testcase"])) == False:
			print("{} !E {}".format(CVE, in_map["bugs"][CVE]["testcase"]))
			rm_keys.append(CVE)
	for X in rm_keys:
		del in_map["bugs"][X]
	for CVE in in_map["bugs"].keys():
		new_case = "{}.pcap".format(CVE)
		print("{} ~ {} now: {}".format(CVE, in_map["bugs"][CVE]["testcase"], new_case))
		# :DXXX
		copyfile("tcpdump-4.9.1/tests/{}".format(in_map["bugs"][CVE]["testcase"]), new_case)
		in_map["bugs"][CVE]["testcase"] = new_case

	with open("new.json", "w+") as wh:
		json.dump(in_map, wh, sort_keys=True, indent=4, separators=(',', ': '))
		
