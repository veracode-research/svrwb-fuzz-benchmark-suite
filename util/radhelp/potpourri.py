
#
# potpourri.py
#
# General helper routines not necessarily directly related to bugs.json
# or anything.
#
#

import os
import psutil
import signal

from .bugdata import bugdata_from_json

#
# shameless use of SO:
#   https://stackoverflow.com/questions/3332043/obtaining-pid-of-child-process
#
def kill_child_processes(parent_proc, sig=signal.SIGTERM, verbose=False):
	"""Attempts to send the sig signal to the chilren of the given
	process.

	Parameters
	----------
	parent_proc : multiprocessing.Process 
		The parent process for which we would like to send signals
		to the children of.
	sig=signal.SIGTERM : int
		Signal to send
	verbose=False : bool
		Enable verbose output; default is False.

	Returns
	-------
	void
	"""
	total_signals_sent = 0

	try:
		parent = psutil.Process(parent_proc.pid)
		children = parent.children(recursive=True)
		if verbose == True:
			print("parent_pid={} child_proc count={}".format(parent_proc.pid, len(children)))

		for process in children:
			if verbose == True:
				print("sending signal {} to child process {}".format(sig, process.pid))
			process.send_signal(sig)
	except psutil.NoSuchProcess:
		print("No such process for {}".format(parent_proc.pid))
		pass

	return

#
# The path is a directory and that dir contains the bugs.json file, usually.
# hokey path.join tho.
#
def case_has_app_built(rootpath, bugjson):
	bjpath = os.path.join(rootpath, bugjson)
	bdata = bugdata_from_json(bjpath)
	if bdata == None:
		return False

	app_path = os.path.join(rootpath, bdata.app_path())
	return os.path.isfile(app_path)
