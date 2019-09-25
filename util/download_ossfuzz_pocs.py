
#
# This uses Selenium to help search OSS-Fuzz PRs and download the 
# PoC input files. I did not see a quick way to interact with their
# system w/o an account or reversing the API, so I figured this
# would do. So far, it does seem to sometimes miss a few files that
# are there ... might do to increase page load waiting time.
#
# XXXInvestigate:
# Fix the query to only produce the ID's.. this will reduce the parsing
# and I think that is all we care about from here?
#
# Generalize and fix a few things:
#  - currently you start up a bunch of chromes and don't re-use
#  - currently you start up chromes and don't stop them! :(
#  - make modular or whatever
#


import argparse
import requests
import sys

from multiprocessing.pool import ThreadPool
from random import shuffle
from selenium import webdriver
from time import time as timer


dummy_chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def get_bug_list_url(project_name):
	#as one column: "https://bugs.chromium.org/p/oss-fuzz/issues/list?colspec=ID&q=-status%3AWontFix%2CDuplicate%20-Infra%20proj%3A{}%20-type%3ABuild-Failure&can=1"
	url = "https://bugs.chromium.org/p/oss-fuzz/issues/list?colspec=ID%20Type%20Component%20Status%20Proj%20Reported%20Owner%20Summary&q=-status%3AWontFix%2CDuplicate%20-Infra%20proj%3A{}%20-type%3ABuild-Failure&can=1".format(project_name)
	return url

def get_bug_info_url(bug_id):
	url = "https://bugs.chromium.org/p/oss-fuzz/issues/detail_ezt?id={}".format(bug_id)
	return url
	

# mostly ripped from
#   https://markhneedham.com/blog/2018/07/15/python-parallel-download-files-requests/
#
def fetch_url(entry):
	bug_id, uri = entry
	if uri is None:
		return None

	if 'http' not in uri:
		print("uri does not contain http -- {}".format(uri))
		return None

	fn = "{}-{}.data".format("OSSFUZZ", bug_id)
	print("request: {}".format(uri))
	try:
		r = requests.get(uri, stream=True)
		if r.status_code == 200:
			with open("{}-{}.data".format("OSSFUZZ", bug_id), 'wb') as f:
				for chunk in r:
					f.write(chunk)
	except:
		print("Exception: uri failure? {} {}".format(type(uri), uri))
		return None
	return bug_id 



def main():

	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--chrome', type=str, nargs='?', help='path to Chrome executable')
	aparse.add_argument('project', help='project name')
	args = aparse.parse_args()

	proj = args.project

	options = webdriver.ChromeOptions()
	if args.chrome:
		options.binary_location = args.chrome
	else:
		options.binary_location = dummy_chrome_path
	options.add_argument('headless')
	driver = webdriver.Chrome(chrome_options=options)

	bug_list_url = get_bug_list_url(proj)
	driver.get(bug_list_url)
	driver.implicitly_wait(15)

	w = driver.find_element_by_id('resultstable')
	table_text = w.text.encode('utf-8', errors='ignore')
	text_rows = [x.strip() for x in table_text.split('\n')[1:]]
	
	m = {}

	# realize: min(duration) > len(text_rows) * perbug_wait minimum 
	perbug_wait = 10
	
	shuffle(text_rows)
	for t in text_rows:
		bug_id = t.split(' ')[0].strip()
		#driver2 = webdriver.Chrome(chrome_options=options)
		#driver2.get(get_bug_info_url(bug_id))
		#driver2.implicitly_wait(perbug_wait)
		
		driver.get(get_bug_info_url(bug_id))
		driver.implicitly_wait(perbug_wait)

		#w = driver2.find_element_by_id('issue-main')
		w = driver.find_element_by_id('issue-main')

		wt = w.text.encode('utf-8', errors='ignore')
	
	#	print(w.text)
		wl = [x.strip() for x in wt.split('\n')]
		caser = None
		dload = False

		# Bad hack.. clean up or at least name things nicely
		for ll in wl:
			if dload == True:
				dload = False
				if 'Download' in ll:
					caser = ll
					caser = caser.split(':')[1]
					caser = caser.strip()
				else:
					print("Parsing error for bug_id {}".format(bug_id))
					caser = None
					break
			if 'Testcase' in ll:
				caser = ll
				caser = caser.split(': ')
				if len(caser) != 2:
					dload = True
					continue
				caser = caser[1]
				caser = caser.strip()
				break
		if caser is None:
			m[str(bug_id)] = None
			continue

	
		url = caser
		m[str(bug_id)] = url
	
	driver.quit()
	urls = []
	for k in m.keys():
		print("{},{}".format(k, m[k]))
		urls.append((k, m[k]))

		
	results = ThreadPool(8).imap_unordered(fetch_url, urls)
	for b_id in results:
	    print(b_id)
	sys.exit(0)

	

if __name__ == '__main__':
	main()
