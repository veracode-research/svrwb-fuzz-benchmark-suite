# FBS Helper Scripts

The majority of these scripts here have been for helping with adding to the
benchmark suite. If there starts to add more analysis, comparison, or graph
generation tools, then we should re-think what goes where.

## What's here:

- bjdiff.py: diff bugs.json files (well, their bugs sections)
- check_crash_uniqueness.py: check the crashes in a bug.json to see if 
there are any duplicates under some definition of equality
- fill_bugs_json.py: use this to bootstrap adding a new bugs.json for an app
- fill_bugs_json_list.py: similar to above, if you have a list of labels or
files already to help.
- radhelp: this is a python module to help with running an app with input
under lldb and gdb.
- gather_crash_data.py: uses a bug.json and runs an app under a debugger
and gathers any crash information if any of the listed inputs cause crash
- copy_bugsjson_less.bugs.py: as it says
- add_bugs_from_csv.py: typically meant for after the above script. the csv
is a buglabel,file tuple
- contrib: random 3rd party stuff
- download_ossfuzz_pocs.py: uses selenium to try to scrape the oss-fuzz 
problem reports
- make_csv_from_aflcrashes.py: create a CSV from a out/crashes directory
from a fuzzing campain using AFL. this is intended to be used by the 
add_bugs_from_csv.py script
- Attic: old stuff, should delete
