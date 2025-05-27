# Node development

Every component of the simulator should be a separate node. The nodes have to publish a [HEARTBEAT](https://mavlink.io/en/messages/common.html#HEARTBEAT) message according to [Heartbeat/Connection Protocol](https://mavlink.io/en/services/heartbeat.html).
There are additional simulator-specific values defined for `type` field, in the [MARSH_TYPE](../mavlink/marsh.md#MARSH_TYPE) enum.

!!! warning
    Historically the component id was also used to determine the component type. New code must not make any assumption about the type from the id used (type is determined from `HEARTBEAT.type`). - quoted from [MAVLink documentaton](https://mavlink.io/en/services/heartbeat.html#component-identity)

With that in mind, the *default* component id is still determined from the type to reduce the risk of collisions, according to this formula:

```
component_id = MAV_COMP_ID_USER1 + (marsh_type - MARSH_TYPE_MANAGER)
```

This assigns consecutive `USER#` definitions, and is used throughout the authors' code.
If someone were to make a mistake and use `MARSH_TYPE` directly as component id, they would show up as `CAMERA` to `CAMERA6`

## Example repository

There are multiple examples of ready-made nodes and utility functions in the [marsh-sim/sim-nodes repository](https://github.com/marsh-sim/sim-nodes).

The names of scripts should hint at the type of component from [MARSH_TYPE](../mavlink/marsh.md#MARSH_TYPE).
These are at the end of the name, and the beginning something unique, to make running a given script easier from terminal with Tab-completion.

## Message choice

For communicating any node-specific feature the workflow is as follows:

1. Check if there is already a relevant convention for a feature in [Microservices](https://mavlink.io/en/services/) section of Dev Guide
    - If nothing was found, search the [Common Message Set](https://mavlink.io/en/messages/common.html)
2. Read documentation for the service: e.g. [Parameter Protocol](https://mavlink.io/en/services/parameter.html)
3. Read documentation for specific messages: e.g. [SIM_STATE (#108)](https://mavlink.io/en/messages/common.html#SIM_STATE)
