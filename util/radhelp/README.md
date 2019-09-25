
# RADHelp


## Random notes

- Using classes for the debugger mostly to just help separate the code rather than
for any OO reasons.
- I almost went with something like [Voltron](https://github.com/snar/voltron) or
expanding on jfoote's work in [exploitable](https://github.com/jfoote/exploitable/) but
wanted to keep it simple at first and will likely include *exploitable* after I port it
to LLVM. I am sure there are a number of other tools, as well, and I will try to do
well to re-use them, etc etc. Just don't hate me if I do not.
- The GDB side uses `--batch` mode and requires us, in easiest form, to write a GDB
script per target application/command line arguments pairs.

