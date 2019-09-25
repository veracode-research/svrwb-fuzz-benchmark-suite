#
# make_csv_from_aflcrashes.py
#
# This is intended to create label,file CSV listing from AFL crashes
# directory. If you specify a another directory, they will be copied
# that location. If you use the optional rename flag, it will replace
# all like :,+-, etc with _'s. The label will be prefixed "afl" unless
# the prefix name is given. There is also no suffix, unless one is
# supplied
#

import argparse
import csv
import os
import shutil
import sys


def main():
	aparse = argparse.ArgumentParser(description="")
	aparse.add_argument('--prefix', nargs='?', help='prefix for labels')
	aparse.add_argument('--suffix', nargs='?', help='suffix for files')
	aparse.add_argument('--newpath', nargs='?', help='new path for files')
	aparse.add_argument('crashes_path', help='AFL crashes/ dir')
	aparse.add_argument('out_csv', help='output CSV')
	cargs = aparse.parse_args()

	label_prefix = 'afl'
	file_suffix = ''
	if cargs.prefix:
		label_prefix = cargs.prefix
	if cargs.suffix:
		file_suffix = cargs.suffix

	crashes_path = cargs.crashes_path
	outcsv = cargs.out_csv

	crash_data = {}
	for cf in os.listdir(crashes_path):
		print(cf)
		if "README" in cf:
			continue
		id_label = cf.split(',')[0]
		id_label = id_label.split(':')[1]
		id_label = "{}{}{}".format(label_prefix, id_label, file_suffix)
		cf_path = os.path.join(crashes_path, cf)
		print(cf_path)
		if cargs.newpath:
			nf_path = os.path.join(cargs.newpath, id_label)
			shutil.copyfile(cf_path, nf_path)
			cf_path = nf_path
		crash_data[id_label] = cf_path

	with open(outcsv, 'w+') as csvfile:
		wrtr = csv.writer(csvfile, delimiter=',',
	 	  quoting=csv.QUOTE_NONE)
		for kk in crash_data.keys():
			try:
				wrtr.writerow([kk, crash_data[kk]])
			except Exception:
				pass
		

	sys.exit(0)
			

if __name__ == '__main__':
	main()
