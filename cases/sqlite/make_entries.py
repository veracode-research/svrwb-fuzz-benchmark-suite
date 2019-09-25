import json
#                "AFL-001": {",
#            "args": "-bail foo @@",",
#            "crash": { },",
#            "description": "from afl",",
#            "testcase": "sample-005.sql"",
#        },",

def pr(f):
	print("{}".format(json.dumps(f, sort_keys=True, indent=8,
	  separators=(',', ': '))))

entries =[   "sqlite-bad-free.sql",
   "sqlite-bad-ptr2.sql",
   "sqlite-bad-ptr3.sql",
   "sqlite-bad-ptr.sql",
   "sqlite-heap-overflow.sql",
   "sqlite-heap-overwrite.sql",
   "sqlite-negative-memset.sql",
   "sqlite-null-ptr10.sql",
   "sqlite-null-ptr11.sql",
   "sqlite-null-ptr12.sql",
   "sqlite-null-ptr13.sql",
   "sqlite-null-ptr14.sql",
   "sqlite-null-ptr15.sql",
   "sqlite-null-ptr1.sql",
   "sqlite-null-ptr2.sql",
   "sqlite-null-ptr3.sql",
   "sqlite-null-ptr4.sql",
   "sqlite-null-ptr5.sql",
   "sqlite-null-ptr6.sql",
   "sqlite-null-ptr7.sql",
   "sqlite-null-ptr8.sql",
   "sqlite-null-ptr9.sql",
   "sqlite-oob-read.sql",
   "sqlite-oob-write.sql",
   "sqlite-stack-buf-overflow.sql",
   "sqlite-stack-exhaustion.sql",
   "sqlite-unint-mem.sql",
   "sqlite-use-after-free.sql"]

k = 0
foo = {}
for j in entries:
	ae = "AFL-{:03d}".format(k)
	foo[ae] = {}
	foo[ae]["args"] = "-bail :memory: -init @@"
	foo[ae]["crash"] = {}
	foo[ae]["description"] = "from afl"
	foo[ae]["testcase"] = j
	k = k + 1

pr(foo)
