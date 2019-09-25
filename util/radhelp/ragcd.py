import lldb
import os
import sys

#
# XXXFIXME do standard function documentation
#
# Intended to be used by whatever will run a target with an input
# file that will cause a crash, so that we can collect crash data
# to (hopefully) differentiate between fuzzer-found crashes.
#
#
#	arch = "x86_64-*-linux"
#	arch = "x86_64-apple-macosx10.13.0"
#	arch = "x86_64-apple-macosx10.14.0"
def ragcd(executable, arch=lldb.LLDB_ARCH_DEFAULT, argv=None, env=None,
  verbose=False):
	if verbose == True:
		print("ragcd: executable='{}'".format(executable))
		print("ragcd: arch='{}'".format(arch))
		print("ragcd: argv='{}'".format(argv))
		print("ragcd: env={}".format(env))

	dbg = lldb.SBDebugger.Create()
	dbg.SetAsync(False)
	dbg.SetUseColor(False)

	sberr = lldb.SBError()


	print("ragcd: dbg.CreateTargetWithFileAndArch({}, {})".format(executable,
	  arch))
	target = dbg.CreateTargetWithFileAndArch(executable, arch)
#	target = dbg.CreateTargetWithFileAndTargetTriple(executable, arch)
#	target = dbg.CreateTarget(executable, arch, "host", False, sberr)
	if not target.IsValid() or not sberr.Success():
		print("ragcd: Unable to create target. Perhaps invalid arch?")
		return None


	thread_bt = {}

	print("ragcd: target.LaucnhSimple({}, {}, {})".format(argv, env,
	  os.getcwd()))

	proc = target.LaunchSimple(argv, env, os.getcwd())
	if proc:
		nthds = proc.GetNumThreads()
		if verbose == True:
			buf = proc.GetSTDOUT(4096)
#			print("ragcd: buf='{}'".format(buf))
#			print("ragcd: Thread count: {}".format(nthds))

		for tdi in range(nthds):
			td = proc.GetThreadAtIndex(tdi)
			td_map_key = "thd{}".format(tdi)
			thread_bt[td_map_key] = [] 
			nframes = td.GetNumFrames()
			print("ragcd: no. frames @ idx {}: {}".format(tdi, nframes))
			for i in range(nframes):
				fr = unicode("{}".format(td.GetFrameAtIndex(i)),
				  errors='replace')
				thread_bt[td_map_key].append(fr)
			
			# Keep things tidy
			if len(thread_bt[td_map_key]) == 0 or  \
			  (len(thread_bt[td_map_key]) == 1 and  \
			  thread_bt[td_map_key][0] == ''):
				del thread_bt[td_map_key]
		proc.Kill()

	# Return a None to be consistent when erroring out
	if len(thread_bt.keys()) == 0:
		if verbose == True:
			print("len(thread_bt.keys()) == 0")
		return None

	return thread_bt

#####
 #Launch (SBListener &listener, 
 #           char const **argv,
 #           char const **envp,
 #           const char *stdin_path,
 #           const char *stdout_path,
 #           const char *stderr_path,
 #           const char *working_directory,
 #           uint32_t launch_flags,   // See LaunchFlags
 #           bool stop_at_entry,
 #           lldb::SBError& error);
#	proc = target.Launch(dbg.GetListener(), None,
#	  None, None,
#	  '/tmp/foo.out', '/tmp/foo.out.err', os.getcwd(), 
#	  0, False, sberr)


def main():
	print("{}".format(ragcd(sys.argv[1], None)))

if __name__ == '__main__':
	main()
