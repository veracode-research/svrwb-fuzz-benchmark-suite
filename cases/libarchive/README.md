# libarchive

## Sources

[https://github.com/libarchive/libarchive](https://github.com/libarchive/libarchiv)

Could use some more investigation to see if there is a version that
maximizes the number of vulns over the inputs we have available. 
Currently, use the `libarchive+81ce2c24f9fec640740de9bcea920ab71ef89059`
path with it's bugs.json

```
$  git checkout `git rev-list -1 --before="Jan 25 2015" master`
Note: checking out '81ce2c24f9fec640740de9bcea920ab71ef89059'.
...
```
