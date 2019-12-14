# Benchmark Application Cases

## Applications 

Directory layout is essentially

```
cases/SomeApplication/
    ...              /bugs.json
    ...              /build.sh
    ...              /clean.sh
    ...              /<various inputs that result in crashes>
    ...              /SomeApplication-version/
    ......                                   /<source>

and after build something like:

    ......                                   /install/bin/SomeApplication

```

## Build

Since each application has their own build system, the way we wrap that is
just with bash scripts. First look at the `config.sh` file and adjust things
as you need. You should just be able to run `build.sh` and it will enter 
each of the application directories and run a local build.sh. 


