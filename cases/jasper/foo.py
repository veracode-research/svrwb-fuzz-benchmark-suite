import json
import sys

X = [ "CVE-2016-2116.jp2",
   "CVE-2016-8880.jp2",
   "CVE-2016-9557.jpg",
   "GITJASPER-31.jpg",
   "CVE-2016-8881.jp2",
   "CVE-2016-9262.jp2",
   "CVE-2016-9387.jp2",
   "CVE-2017-13747.jp2",
   "CVE-2017-13750.jp2",
   "CVE-2017-13751.jp2",
   "CVE-2017-13752.jp2",
   "CVE-2017-5498.jp2",
   "CVE-2017-5499.jp2",
   "CVE-2017-5500.jp2",
   "CVE-2017-5501.jp2",
   "CVE-2017-5502.jp2",
   "CVE-2017-5503.jp2",
   "CVE-2017-5504.jp2",
   "CVE-2017-5505.jp2",
   "CVE-2017-6850.jp2",
   "CVE-2017-6851.jp2",
   "CVE-2017-6852.jp2",
   "CVE-2018-18873.jp2",
   "CVE-2018-19139.jp2",
   "CVE-2018-19539.jp2",
   "CVE-2018-19540.jp2",
   "CVE-2018-19541.jp2",
   "CVE-2018-19542.jp2",
   "CVE-2018-19543.jp2",
   "CVE-2018-20570.jp2",
   "CVE-2018-9055.jp2",
   "CVE-2018-9154.jp2",
   "CVE-2018-9252.jp2",
   "GITJASPER-182-10.jp2",
   "GITJASPER-182-6.jp2",
   "GITJASPER-182-7.jp2",
   "GITJASPER-182-8.jp2",
   "GITJASPER-182-9.jp2",
   "GITJASPER-30.jp2",
   "GITJASPER-32.jp2",
   "NOTINBUGSJSON-CVE-2016-9560.jp2"]

with open("bugs.json", "r") as ih:
	m = json.load(ih)
	X = set(X)
	tc = []
	for k in m["bugs"].keys():
		tc.append(m["bugs"][k]["testcase"])
	tc = set(tc)

	print("x - tc: {}".format(X - tc))
	print("tc - x: {}".format(tc - X))
