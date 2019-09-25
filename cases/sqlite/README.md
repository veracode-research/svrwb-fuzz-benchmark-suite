
Build things with runtime disabled ASAN. Some of the build stuff
has memory leaks so it will error out.

```
ASAN_OPTIONS=detect_leaks=0 ./build.sh
```

This is verion 3.8.7.4 which is downloaded by `https://www.sqlite.org/src/tarball/sqlite.tar.gz?r=version-3.8.7.4`.

```
https://www.sqlite.org/src/doc/trunk/README.md
```

