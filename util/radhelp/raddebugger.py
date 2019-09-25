import re

class RADDebugger(object):
	"""
	A base class for running FBS apps under a debugger.

	...

	Attributes
	----------

	executable : str
		path to the executable to be launched
	argv : list of str
		arguments to the executable
	env : list of str
		environment variables to be injected for execution
	arch : str
		the architecture triple of the executable
	verbose : bool
		verbose output (default=False)

	Methods
	-------

	did_error()
		Determines if there was an error raised by a prior call
	execute()
		Actually run the program with arguments and environment vars
	get_trace():
		Return the dict() of results
	get_trace_parsed()
		return a subset of the results
	get_trace_functions()
		return only the functions in the trace
	"""
	
	def __init__(self, executable, argv, env, arch, verbose=False):
		self.executable = executable
		self.argv = argv
		self.env = env
		self.arch = arch
		self.verbose = verbose

		if verbose == True:
			print("ragcd: executable='{}'".format(executable))
			print("ragcd: argv='{}'".format(argv))
			print("ragcd: arch='{}'".format(arch))
			print("ragcd: env={}".format(env))

		return

	def did_error(self):
		return False

	def execute(self):
		return

	def get_trace(self):
		return None

	def get_trace_parsed(self):
		return None

	# Return only the functions invoked found in trace
	def get_trace_functions(self):
		return None

from .llvm import LLDBDebugger
from .gnu import GDBDebugger

def run(exe, argv, env, arch, kind):
	if kind == "llvm":
		return run_with_lldb(exe, argv, env, arch)
	elif kind == "gdb":
		return run_with_gdb(exe, argv, env, arch)

	raise NotImplementedError("run(kind={})".format(kind))

def run_with_lldb(exe, argv, env, arch):
	l = LLDBDebugger(exe, argv, env, arch, verbose=True)
	if l.did_error() == True:
		print("run_with_lldb: unable to initialize lldb")
		return None
	l.execute()
	return l.get_trace()

def run_with_gdb(exe, argv, env, arch):
	g = radhelp.gdb.GDBDebugger(exe, argv, env, arch, verbose=True)
	if g.did_error() == True:
		print("run_with_gdb: unable to initialize gdb")
		return None
	g.execute()
	return g.get_trace()

#
# Return a list of tuples (address, function, file, line/offset)?
#
def parse_trace(bt, kind):
	parsed = []
	if kind == 'llvm':
		for frame in bt:
			#print(frame)
#frame #0: 0x000000000049c1b0 sfconvert`::AsanDie() at asan_rtl.cc:42
#			m = re.search(r'frame #(\d+): (0x[0-9a-f]{16}) ([_.`\w]+).* (\d+)', frame)
#			m = re.search(r'frame #(\d+): (0x[0-9a-f]{16}) ([_.`\w]+) at (\d+)', frame)
			m = re.search(r'(\d+)\|(0x[0-9a-f]{16})\|([_.`\w\(\):~]+)\|(\d+)', frame)
#			print("what: {}".format(m))
			if m:
				f = (m.group(1), m.group(2), m.group(3), m.group(4))
				parsed.append(f)
	elif kind == 'gnu':
		return None
	else:
		return None
	return parsed
