# Simulator nodes

The purpose of nodes is to maintain the [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) principle.
In short, if each node has a single responsibility, it is easier to reuse them in new ways and avoid repeating work (see&nbsp;[rationale](../rationale.md)).

![diagram highlighting nodes in the structure of the simulator](./simulator_variants_nodes.png)

When ran as a command, nodes should accept the IP MARSH Manager with `-m` and `--manager` option.

Nodes created so far have been collected in the [marsh-sim/sim-nodes repository](https://github.com/marsh-sim/sim-nodes).
You are welcome to ask questions, report bugs and contribute new scripts there.

## Lidia instruments

Python package [`lidia`](https://pypi.org/project/lidia/) can be used with MARSH starting with version 0.10 to provide instrument visualisation.
It can be installed using the `pip` command:

```bash
pip install lidia
```

The package has multiple sources of data to choose from, in this case start it like this:

```bash
lidia marsh
```
