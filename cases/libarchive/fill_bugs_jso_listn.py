import json
import os
import sys



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

issue_samples = [ "CVE-2018-1000877.rar",
  "CVE-2018-1000878.rar",
  "CVE-2018-1000879.rar",
  "CVE-2018-1000880.rar",
  "CVE-2019-1000019.7z",
  "LIBARCHIVE-1016.zip",
  "LIBARCHIVE-508.tar",
  "LIBARCHIVE-705-1.cpio",
  "LIBARCHIVE-705-2.cpio",
  "LIBARCHIVE-705-3.cpio",
  "LIBARCHIVE-866.zip",
  "OSSFUZZ-10071.data.rar",
  "OSSFUZZ-10843.data.rar",
  "OSSFUZZ-1097.data.rar",
  "OSSFUZZ-11011.data.rar",
  "OSSFUZZ-11058.data.rar",
  "OSSFUZZ-11196.data.rar",
  "OSSFUZZ-12466.data.rar",
  "OSSFUZZ-12593.data.rar",
  "OSSFUZZ-12600.data.rar",
  "OSSFUZZ-12601.data.rar",
  "OSSFUZZ-12817.data.rar",
  "OSSFUZZ-12999.data.rar",
  "OSSFUZZ-13029.data.rar",
  "OSSFUZZ-13144.data.rar",
  "OSSFUZZ-13435.data.rar",
  "OSSFUZZ-13478.data.rar",
  "OSSFUZZ-13490.data.rar",
  "OSSFUZZ-13965.data.rar",
  "OSSFUZZ-139.data.rar",
  "OSSFUZZ-14331.data.rar",
  "OSSFUZZ-14373.data.rar",
  "OSSFUZZ-14393.data.rar",
  "OSSFUZZ-14416.data.rar",
  "OSSFUZZ-14470.data.rar",
  "OSSFUZZ-14490.data.rar",
  "OSSFUZZ-14491.data.rar",
  "OSSFUZZ-14537.data.rar",
  "OSSFUZZ-14555.data.rar",
  "OSSFUZZ-14574.data.rar",
  "OSSFUZZ-145.data.rar",
  "OSSFUZZ-14677.data.rar",
  "OSSFUZZ-14689.data.rar",
  "OSSFUZZ-14.data.rar",
  "OSSFUZZ-15120.data.rar",
  "OSSFUZZ-15278.data.rar",
  "OSSFUZZ-152.data.rar",
  "OSSFUZZ-15431.data.rar",
  "OSSFUZZ-15.data.rar",
  "OSSFUZZ-1627.data.rar",
  "OSSFUZZ-190.data.rar",
  "OSSFUZZ-191.data.rar",
  "OSSFUZZ-220.data.rar",
  "OSSFUZZ-227.data.rar",
  "OSSFUZZ-230.data.rar",
  "OSSFUZZ-232.data.rar",
  "OSSFUZZ-234.data.rar",
  "OSSFUZZ-235.data.rar",
  "OSSFUZZ-237.data.rar",
  "OSSFUZZ-2394.data.rar",
  "OSSFUZZ-239.data.rar",
  "OSSFUZZ-2582.data.rar",
  "OSSFUZZ-286.data.rar",
  "OSSFUZZ-335.data.rar",
  "OSSFUZZ-359.data.rar",
  "OSSFUZZ-421.data.rar",
  "OSSFUZZ-422.data.rar",
  "OSSFUZZ-443.data.rar",
  "OSSFUZZ-451.data.rar",
  "OSSFUZZ-453.data.rar",
  "OSSFUZZ-458.data.rar",
  "OSSFUZZ-485.data.rar",
  "OSSFUZZ-4969.data.rar",
  "OSSFUZZ-497.data.rar",
  "OSSFUZZ-504.data.rar",
  "OSSFUZZ-511.data.rar",
  "OSSFUZZ-526.data.rar",
  "OSSFUZZ-527.data.rar",
  "OSSFUZZ-528.data.rar",
  "OSSFUZZ-532.data.rar",
  "OSSFUZZ-538.data.rar",
  "OSSFUZZ-551.data.rar",
  "OSSFUZZ-552.data.rar",
  "OSSFUZZ-556.data.rar",
  "OSSFUZZ-573.data.rar",
  "OSSFUZZ-577.data.rar",
  "OSSFUZZ-745.data.rar",
  "OSSFUZZ-7837.data.rar",
  "OSSFUZZ-806.data.rar",
  "OSSFUZZ-862.data.rar",
  "OSSFUZZ-9521.data.rar" ]

def main():
	out_file = 'bugs.json'

	# Adjust these as needed (i should just make it more stdin read)
	bd = { }
	bd["application"] = "libarchive"
	bd["apppath"] = "libarchive+81ce2c24f9fec640740de9bcea920ab71ef89059/install/bin/bsdtar"
	bd["known_vuln_count"] = 0
	bd["version"] = "1.9.2"
	bd["source"] = "https://github.com/Yeraze/ytnef/tree/master/ytnef"
	bd["cve"] = ""

	bugs = {}
	for badboi in issue_samples:
		cve = badboi.split(".")[0]
		bugs[cve] = {}
		bugs[cve]["crash"] = {}
		bugs[cve]["description"] = "https://www.cvedetails.com/cve-details.php?t=1&cve_id={}".format(cve)
		bugs[cve]["testcase"] = badboi
		bugs[cve]["args"] = "tv @@"

	bd["bugs"] = bugs	
	with open(out_file, "w+") as nh:
		json.dump(bd, nh, indent=4, separators=(',', ': '), sort_keys=True)


if __name__ == '__main__':
	main()
