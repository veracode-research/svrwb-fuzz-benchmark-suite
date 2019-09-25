import json
import os
import sys




issue_samples =[  "CVE-2017-12804.data",
  "CVE-2017-7452.data",
  "CVE-2017-7453.data",
  "CVE-2017-7454.data",
  "CVE-2017-7623.data",
  "CVE-2017-7624.data",
  "CVE-2017-7939.data",
  "CVE-2017-7940.data",
  "CVE-2017-7962.data",
  "CVE-2017-8325.data",
  "CVE-2017-8326.data",
  "CVE-2017-8327.data",
  "CVE-2017-9093.data",
  "CVE-2017-9094.data",
  "CVE-2017-9201.data",
  "CVE-2017-9202.data",
  "CVE-2017-9203.data",
  "CVE-2017-9204.data",
  "CVE-2017-9205.data",
  "CVE-2017-9206.data",
  "CVE-2017-9207.data",
  "CVE-2018-16782.data",
  "CVE-2018-5252.data" ]

def main():
	out_file = 'bugs.json'

	# Adjust these as needed (i should just make it more stdin read)
	bd = { }
	bd["application"] = "imagew"
	bd["apppath"] = "imagew-1.3.0/install/bin/imagew"
	bd["known_vuln_count"] = 0
	bd["version"] = "1.3.0"
	bd["source"] = "https://github.com/jsummers/imageworsener"
	bd["cve"] = ""

	bugs = {}
	for badboi in issue_samples:
		cve = badboi.split(".")[0]
		bugs[cve] = {}
		bugs[cve]["crash"] = {}
		bugs[cve]["description"] = "https://www.cvedetails.com/cve-details.php?t=1&cve_id={}".format(cve)
		bugs[cve]["testcase"] = badboi
		bugs[cve]["args"] = "@@ foo.png"

	bd["bugs"] = bugs	
	with open(out_file, "w+") as nh:
		json.dump(bd, nh, indent=4, separators=(',', ': '), sort_keys=True)


if __name__ == '__main__':
	main()
