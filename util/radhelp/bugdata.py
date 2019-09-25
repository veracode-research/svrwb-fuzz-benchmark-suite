#
# bugdata.py
#
# Side notes:
# - Someone could go through and make this more pythonic
# - The location of utf-8 en/decode is wonky.. solidify
#

import json
import os
import re

def bugdata_from_json(jpath):
	json_dict = None

	try:
		oh = open(jpath, 'r')
		jpath_data = oh.read()
		json_dict = json.loads(jpath_data, encoding='utf8')
	except Exception as e:
		print("bugdata_from_json: loader exception: {}".format(e))
		return None

	# i need to filter verbosity properly
	if json_dict is None:
		print("bugdata_from_json: unable to load\n")
		return None

	if type(json_dict) is not dict: 
		print("bugdata_from_json: unable to load: not a dict\n")
		return None

	# icky; pythoners hate me im sure
	keez = [u"application", u"apppath", u"evars", u"source", u"version",
	  u"bugs", u"args"]
	ikeez = lambda x: x in json_dict.keys()
	if all(list(map(ikeez, keez))) == False:
		print("bugdata_from_json: lambda/map magic failed\n")
		return None

	# Is that ok to pass? the bugs, that is.
	bd = BugData(json_dict["application"],
	  json_dict["apppath"],
	  json_dict["args"],
	  json_dict["evars"],
	  json_dict["source"],
	  json_dict["version"])

	for k in json_dict["bugs"].keys():
		bd.add_bug(k,
		  json_dict["bugs"][k]["crash"],
		  json_dict["bugs"][k]["description"],
		  json_dict["bugs"][k]["testcase"])
	return bd

class BugData:
	"""
	Represents an application, arguments, and various inputs that will
	cause the application to crash. It keeps traces in here as well.

	...

	Attributes
	----------
	application : str
		name of the application related to the bugs
	app_path : str
		path to the actual built application
	args : str
		string version of the arguments to the application
	env : list of str
		the environment various to use
	source : str
		Link to the source of the application being used
	version : str
		Version of the application being used

	Methods
	-------
	dupe(include_bugs=False)
		Duplicate this object and return the copy
	get_all_bug_labels():
		Return a list of the bug labels (usually CVEs)
	has_bug(cve):
		Return bool on whether the given CVE is in this BugData
	has_crash(cve, arch):
		Determines if there is an existing crash for the CVE & arch
        def add_bug(self, cve, crash=None, description=None, testcase=None)
		Insert the given CVE with bug information
	get_trace(cve, arch)
		Return the traces for the CVE and the given architecture
	remove_bug(cve)
		Remove the bug information related to the CVE
	remove_all_bugs()
        application()
        app_path()
        evars()
        bugs()
        version()
        source()
        testcase(cve)
        args()
		The above are just method accessors to attributes
        write_json(out_path):
		Write the BugData to JSON file

	"""
	def __init__(self, application, app_path, args, env, source, version):
		self.bd = {}
		self.bd["application"] = application
		self.bd["apppath"] = app_path
		self.bd["args"] = args
		self.bd["evars"] = env
		self.bd["source"] = source
		self.bd["version"] = version
		self.bd["bugs"] = {}

		self._parsed_trace = None

	def dupe(self, include_bugs=False):
		bd = BugData(self.application(), self.app_path(), self.evars(),
		  self.source(), self.version())
		 
		if include_bugs == True:
			bd.bd["bugs"] = self.bd["bugs"]
		return bd

	def get_all_bug_labels(self):
		return self.bd["bugs"].keys()

	def has_bug(self, cve):
		return cve in self.bd["bugs"].keys()

	def has_crash(self, cve, arch):
		#print("self.bd[bugs]:\n{}\n".format(self.bd["bugs"]))
		if cve not in self.bd["bugs"].keys():
			print("has_crash: cve not in bugs list")
			return False

		if "crash" not in self.bd["bugs"][cve].keys():
			print("has_crash: no key: {}".format(self.bd["bugs"][cve].keys()))
			return False

		if self.bd["bugs"][cve]["crash"] is None:
			print("crash None: cve={} crash entry: {}".format(cve,
			  self.bd["bugs"][cve]["crash"]))
			return False

		if arch not in self.bd["bugs"][cve]["crash"].keys():
			print("has_crash: arch {} not found".format(arch))
			return False

		if "bt" not in self.bd["bugs"][cve]["crash"][arch].keys():
			return False

		if self.bd["bugs"][cve]["crash"][arch]["bt"] is None:
			return False

		if "thd0" not in self.bd["bugs"][cve]["crash"][arch]["bt"].keys():
			return False

		return True

	# Assumes the CVE is not in the dict
	def add_bug(self, cve, crash=None, description=None, testcase=None):
		self.bd["bugs"][cve] = {}
		self.bd["bugs"][cve]["crash"] = crash 
		self.bd["bugs"][cve]["description"] = description
		self.bd["bugs"][cve]["testcase"] = testcase

	def get_trace(self, cve, arch):
		if cve not in self.bd["bugs"].keys():
			return None

		if self.bd["bugs"][cve]["crash"] is None:
			return None

		if arch not in self.bd["bugs"][cve]["crash"].keys():
			return None

		if "bt" not in self.bd["bugs"][cve]["crash"][arch].keys():
			return None

		if self.bd["bugs"][cve]["crash"][arch]["bt"] is None:
			return None

		if "thd0" not in self.bd["bugs"][cve]["crash"][arch]["bt"].keys():
			return None

		return self.bd["bugs"][cve]["crash"][arch]["bt"]["thd0"]

	def get_crashes(self, arch):
		"""Retrieve all crashes under the given architecture
		"""
		ckeys = self.bd["bugs"].keys()
		crashes = []
		for x in ckeys:
			if arch in self.bd["bugs"][x]["crash"].keys():
				if self.bd["bugs"][x]["crash"][arch]["bt"] is not None:
					crashes.append(self.bd["bugs"][x]["crash"][arch]["bt"])
		if len(crashes) == 0:
			return None
		return crashes

	def remove_bug(self, cve):
		if self.has_bug(cve) == False:
			return
		del self.bd["bugs"][cve]

	def remove_all_bugs(self):
		ke = list(self.bd["bugs"].keys())
		for k in ke:
			self.remove_bug(k)
		return

	def application(self):
		return self.bd["application"]

	def app_path(self):
		return self.bd["apppath"]

	def evars(self):
		return self.bd["evars"]

	def bugs(self):
		return self.bd["bugs"]

	def version(self):
		return self.bd["version"]

	def source(self):
		return self.bd["source"]

	def write_json(self, out_path):
	#	print(self.bd)
		with open(out_path, "w+") as nh:
			json.dump(self.bd, nh, indent=4,
			  separators=(',', ': '), sort_keys=True)

	def args(self):
		return self.bd["args"]

	def testcase(self, cve):
		assert cve in self.bd["bugs"].keys(),  \
		  "{} is not in the bug list".format(cve)
		return self.bd["bugs"][cve]["testcase"]
		
