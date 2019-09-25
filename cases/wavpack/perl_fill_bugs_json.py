import json
import os
import sys

cves = [
    "CVE-2016-10169.wv",
    "CVE-2016-10170.wv",
    "CVE-2016-10171.wv",
    "CVE-2016-10172.wv"
]

#{
#    "application": "audiofile",
#    "apppath": "audiofile-0.3.6/sfcommand/sfinfo",
#    "bugs": {
#        "CVE-2017-6827" : {
#           "args" : null,
#           "crash" : {},
#           "description" : "",
#           "testcase" : ""
#        }
#    }

def main():
	out_file = 'bugs.json'

	# Adjust these as needed (i should just make it more stdin read)
	bd = { }
	bd["application"] = "wvunpack"
	bd["apppath"] = "install/bin/wvunpack"
	bd["known_vuln_count"] = 0
	bd["version"] = "5.0.0"
	bd["source"] = "https://github.com/dbry/WavPack"
	bd["cve"] = "https://github.com/dbry/WavPack/commit/4bc05fc490b66ef2d45b1de26abf1455b486b0dc"

	bugs = {}
	for k in cves:
		f = k
		f = f.replace(".wv", "")
		cve = f	
		bugs[cve] = {}
		bugs[cve]["crash"] = {}
		bugs[cve]["description"] = "https://www.cvedetails.com/cve-details.php?t=1&cve_id={}".format(cve)
#		print("Url to description?")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs[cve]["description"] = line
#		print("Arguments?")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs[cve]["args"] = line
		bugs[cve]["args"] = None 
#		print("Url to testcase? ")
#		line = sys.stdin.readline().strip()
#		if line != '':
#			bugs[cve]["testcase_url"] = line
		bugs[cve]["testcase_url"] = '' 
		print("testcase? ")
		bugs[cve]["testcase"] = k 

	bd["bugs"] = bugs	
	with open(out_file, "w+") as nh:
		json.dump(bd, nh, indent=4, separators=(',', ': '), sort_keys=True)


if __name__ == '__main__':
	main()
