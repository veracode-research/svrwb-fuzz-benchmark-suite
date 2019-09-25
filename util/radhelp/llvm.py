
# arch = "x86_64-*-linux"
# arch = "x86_64-apple-macosx10.13.0"
# arch = "x86_64-apple-macosx10.14.0"
# arch = lldb.LLDB_ARCH_DEFAULT

import lldb
import os
import re

from . import raddebugger

class LLDBDebugger(raddebugger.RADDebugger):
	"""
	Implementation of RADDebugger for lldb.

	...

	Attributes
	----------

	Methods
	-------

	"""
	def __init__(self, executable, argv, env, arch, verbose=False):
		super().__init__(executable, argv, env, arch, verbose)

		self._lldb_dbg = lldb.SBDebugger.Create()
		self._lldb_dbg.SetAsync(False)
		self._lldb_dbg.SetUseColor(False)
		self._lldb_sberr = lldb.SBError()

		if verbose == True:
			print("_lldb_dbg dir: {}".format(dir(self._lldb_dbg)))
			print("interpreter dir: {}".format(dir(self._lldb_dbg.GetCommandInterpreter())))
			print("ragcd: dbg.CreateTargetWithFileAndArch({}, {})".format(executable, arch))

		# Initialize here, but launch in execute()
		self._lldb_target = self._lldb_dbg.CreateTargetWithFileAndArch(self.executable, self.arch)

		self._lldb_proc = None
		self._lldb_raw_bt = None
		self._lldb_parsed_bt = None

	def did_error(self):
		if self._lldb_target.IsValid() == False:
			print("ragcd: invalid llvm target")
			return True

		if self._lldb_sberr.Success() == False:
			print("ragcd: sberror not success")
			return True

		return False

	def execute(self):

		self._lldb_raw_bt = {}
		if self.verbose == True:
			print("ragcd: target.LaunchSimple({}, {}, {})".format(self.argv, self.env,
			  os.getcwd()))

		self._lldb_proc = self._lldb_target.LaunchSimple(self.argv, self.env, os.getcwd())

		# Disp frame format that has the information we need and is easy to parse from string
		result = lldb.SBCommandReturnObject()
		interp = self._lldb_dbg.GetCommandInterpreter()
		interp.HandleCommand("settings set frame-format ${frame.index}|${frame.pc}|${module.file.basename}`${function.name}|${function.pc-offset}\n", result)
#		interp.HandleCommand("settings set frame-format ${frame.index}|${module.file.basename}`${function.name}|${function.pc-offset}\n", result)

		#
		# May want to change this. We process the crash here instead of at another point.
		# ...and then we kill the process. The function implies we would just execute...
		# so may be worth adjusting
		#
		if self._lldb_proc:
			nthds = self._lldb_proc.GetNumThreads()

			if self.verbose == True:
				buf = self._lldb_proc.GetSTDOUT(4096)
				print("ragcd: #tds={} buf='{}'".format(nthds, buf))

			self._lldb_parsed_bt = {}
			for tdi in range(nthds):

				td_map_key = "thd{}".format(tdi)
				self._lldb_raw_bt[td_map_key] = []
				self._lldb_parsed_bt[td_map_key] = []

				td = self._lldb_proc.GetThreadAtIndex(tdi)
				nframes = td.GetNumFrames()

				if self.verbose == True:
					print("ragcd: no. frames @ idx {}: {}".format(tdi, nframes))

				for i in range(nframes):
					r_fr = str(td.GetFrameAtIndex(i))
					#if self.verbose == True:
					#	print(r_fr)

					piece = r_fr.split(" + ")
				#	if self.verbose == True:
				#		print(len(piece))

					if len(piece) != 2:
						continue
					r_fr = "{}{}".format(r_fr.split(" + ")[0], r_fr.split(" + ")[1])
					self._lldb_raw_bt[td_map_key].append(r_fr)

				# Keep things tidy
				if len(self._lldb_raw_bt[td_map_key]) == 0 or  \
				  (len(self._lldb_raw_bt[td_map_key]) == 1 and  \
				  self._lldb_raw_bt[td_map_key][0] == ''):
					del self._lldb_raw_bt[td_map_key]
					del self._lldb_parsed_bt[td_map_key]
			self._lldb_proc.Kill()

	def get_trace(self):
		if self._lldb_raw_bt == None:
			if self.verbose == True:
				print("ragcd: raw LLVM trace has no keys")
			return None

		# Not this simple.
		return self._lldb_raw_bt

	def get_parsed_trace(self):
		if self._lldb_parsed_bt == None:
			if self.verbose == True:
				print("ragcd: parsedLLVM trace has no keys")
			return None

		# Not this simple.
		return self._lldb_parsed_bt


if __name__ == '__main__':
	G = LLDBDebugger("/home/arr/tmp/test", [ "1", "2"], None, None, True)
	G.execute()
	print(G.get_trace())
