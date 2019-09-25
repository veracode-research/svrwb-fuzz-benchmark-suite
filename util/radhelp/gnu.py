#gdb --batch -x s ./test

import os
import re
import subprocess
import sys
import tempfile

from . import raddebugger


class GDBDebugger(raddebugger.RADDebugger):
	"""
	Implementation for RADDebugger for GDB (XXX: version?).
	Currently implemented as a subprocess invoke to gdb with a
	batch script that is generated for each run (:shrug:)

	It might be worthwhile to investigate the exploitable code
	from jfoote. One thing would be to add LLVM support to how it
	works, or just port. Another thing would be to add the
	exploitability data to the fuzzing benchmark suite.

	...

	Attributes
	----------

	Methods
	-------

	"""
	def __init__(self, executable, argv, env, arch, verbose=False):
		super().__init__(executable, argv, env, arch, verbose)

		self._gdb_path = "/usr/bin/gdb"
		self._gdb_dbg = None
		self._gdb_raw_bt = None
		self._gdb_parsed_bt = None
		self._gdb_fn_bt = None
		self._gdb_argv = argv
		self._gdb_script_path = None

	def did_error(self):
		raise NotImplementedError("GDBDebugger: did_error")

	def set_script_path(self, script_path):
		self._gdb_script_path = script_path

	def _write_batch_script(self):
		(fd, p) = tempfile.mkstemp()

		# be consistent with the lldb default for trace depth
		os.write(fd, b"set backtrace past-main on\n")

		# load a helper script to improve output
		if self._gdb_script_path is None:
			raise FileNotFoundError("GDB script path is not set.")
		if os.path.isabs(self._gdb_script_path) == False:
			raise FileNotFoundError("GDB script path is not absolute.")
		source_scr = bytes("source {}\n".format(self._gdb_script_path), "utf8")
		os.write(fd, source_scr)

		# formulate the run command line; we should never have no
		# arguments. xxx: add return checks
		if self._gdb_argv and len(self._gdb_argv) > 0:
			runner = "run {}\n".format(" ".join(self._gdb_argv))
			os.write(fd, bytes(runner, 'utf8'))
		else:
			os.write(fd, b"run\n")

		os.write(fd, b"quit\n")
		os.lseek(fd, 0, os.SEEK_SET)
		os.close(fd)
		return p

	def execute(self):
		p = self._write_batch_script()
		e = [ self._gdb_path, self.executable, "--batch", "-x", p ]
		cp = subprocess.run(e, universal_newlines=True, stdout=subprocess.PIPE,
		  stderr=subprocess.PIPE)
		os.unlink(p)

		self._gdb_raw_bt = cp.stdout
		#print(self._gdb_raw_bt)
		#print("----")
		matches = re.findall("^([0-9]+)\|(0x[0-9a-f]{1,16})\|(\w+)\|([0-9]+)$", self._gdb_raw_bt, re.M)

		self._gdb_parsed_bt = {} 
		self._gdb_parsed_bt["thd0"] = [] 
		for m in matches:
		#	print("m: {}".format(m))
			self._gdb_parsed_bt["thd0"].append("{}|{}|{}|{}".format(m[0], m[1], m[2], m[3]))

	def get_trace(self):
		return self._gdb_parsed_bt

	def get_trace_functions(self):
		return list([x.split("|")[2] for x in self._gdb_parsed_bt])


if __name__ == '__main__':
	G = GDBDebugger("/home/arr/tmp/test", [ "1", "2"], None, None, True)
	G.set_script_path("/home/arr/fuzz-benchmark-suite/util/fbs_gdb_helper.py")
	G.execute()
	print(G.get_trace())
	print(G.get_trace_functions())

