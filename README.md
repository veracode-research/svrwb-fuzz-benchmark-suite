# Single Version, Real World (Dead) Bug Fuzzer Benchmark Suite

Note: This is a **Work in Progress**.

Prior to going into any details, I will note that I have mixed opinions
on how to do benchmarking of fuzzers and whether or not that is a good
thing (for various purposes). What I do believe is that no benchmarking seems
like a not-great path to go down. There are a few ways of analyzing fuzzers
(see some twitter discussions with S. Heelan and B. Falk around 9/24/19, for
example) and this can be one of them. As for this suite, there is no notion
of the types of bugs one should (?) find with this, just that they are bugs
from some popular and some less than popular OSS... I digress.

...

This is a collection of some real world, open source software and proof of
concept inputs that cause the applications to crash. There is just a single
version being looked at for each application and typically only one 
entry point (and configuration) used. The goal is to provide a set of real
world applications with a set of known bugs to have ground truth. Hopefully
this can be useful as a benchmark to help compare applications. While Google's
FTS has more applications, there are less bugs per app they want you to find,
but perhaps more variety than this.

## Test cases

| Application     | Version  | number of issues* |
| ----------------|:---------|:------------------|
| audiofile       | 0.3.6    | 11                |
| ImageWorsener   | 1.3.0    |  8                |
| jasper          | 1.701.0  | 20                |
| LAME            | 3.99.5   |  9                |
| libarchive      | 81ce2c24f9fec640740de9bcea920ab71ef89059 | 12      |
| Perl            | 5.21.7   | 20                |
| sqlite          | 3.8.7.4  | 18                |
| TCPDump         | 4.9.0    | 34                |
| WavPack         | 5.0.0    |  5                |
| ytnef           | 1.9.2    | 11                | 


*Obviously number of issues is likely incomplete, but hopefully providing
a reasonable number of bugs.

## Work to be done

- Additional test applications
- Process for adding new bugs found after analysis (improve quality)
- Suss out duplicates
- List descriptions of kinds of bugs in each application
- Patches that add labels to the code for where the bug is


# Compilation 

There are bash scripts that manage invoking the various makefiles
for each of the applications. An important script to look at is
`cases/config.sh` as it is really where you can modify CFLAGS, CC, CXX 
etc. The `cases/build.sh` file actually iterates through the subdirectories
and invokes their own build.sh files. It is these app-level build.sh files
that will run configure, make, etc.

The build binaries are typically going to be in cases/app/app/install/bin/ 
or something similar. 


## Requirements

You will want LLVM >=5 and/or GCC >= 7.x installed in order to build
these applications. In addition, some the applications have other needs
which include:

- automake
- libtool
- tclsh
- tk-dev
- (f)lex
- bison/yacc
- libasound2-dev
