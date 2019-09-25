import os
import sys
from struct import *

#
# some people seem to want to distribute binary data files as
# hexdumps, for some reason... so... parse this and create the
# data file :shrug:. it's not well written.
#
#
# this is for format like:
#
# areiter@~/cases_to_add/libarchive$ cat double-free.rar.txt
# 00000000: 5261 7221 1a07 005b 6573 0100 0d00 1500  Rar!...[es......
# 00000010: 2201 0000 2dd7 7403 842f 0020 0000 0000  "...-.t../. ....
# ...
#
# versus a kind like:
#
# 00000000  52 61 72 21 1a 07 00 5b  65 73 01 00 0d 00 15 00  |Rar!...[es......|
#
# Note the ':', the extra ' ' and the '|'s. So.. that sucks :D
#
#
def main():

	if len(sys.argv) != 3:
		print("usage: hexdump2data.py <in> <out>")
		sys.exit(1)

	hd = sys.argv[1]
	of = sys.argv[2]

	oh = open(of, 'wb+')
	ih = open(hd, 'r')
	in_line = ih.readline()
	while in_line != '':
		in_line = in_line.strip()

		one = in_line.split('  ')[0].strip()
		two = one.split(':')[1].strip()
		data_fields = two.split(' ')

#		print("{}".format(data_fields))

		for d in data_fields:
			d = d.strip() # shouldn't be needed
			# hack: could be done relatively, but whatever
			d = '0x{}'.format(d)
			dval = int(d, base=16)
			bval = None
			if len(d) == 6:
				bval = pack(">H", dval)
			elif len(d) == 4:
				bval = pack("B", dval)
			else:
				print("length issue: {} = len({})".format(len(d), d))
				sys.exit(-1)
			oh.write(bval)

		in_line = ih.readline()
	ih.close()
	oh.close()
	sys.exit(0)


if __name__ == '__main__':
	main()
