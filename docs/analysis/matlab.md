# MATLAB analysis

!!! note
    Requires the "[UAV Toolbox](https://www.mathworks.com/products/uav.html)" to be installed

The `.tlog` files [saved by MARSH Manager](../manager/README.md#saving-data) can be loaded with [`mavlinktlog`](https://www.mathworks.com/help/uav/ref/mavlinktlog.html) function.
However, the implementation of [`mavlinkdialect`](https://it.mathworks.com/help/uav/ref/mavlinkdialect.html) has the following errors that make reading custom messages more complicated than it would seem from the documentation:

- The parser crashes with "Dot indexing is not supported for variables of this type." when it encounters a message field that does not have a `<description>` element containing text, which prevents us from loading `all.xml`
- Seems to ignore the `<include>common.xml</include>` line in dialect file

To work around this, the messages can be extracted in multiple steps with separate dialect definitions:

```matlab
dialect_common = mavlinkdialect("common.xml");
logimport_common= mavlinktlog("./data/YYMMDDTHHMMSS_comment.tlog", dialect_common);

sim_state_msgs = readmsg(logimport_common, 'MessageName', 'SIM_STATE');
sim_state_data = sim_state_msgs.Messages{1};

% This requires a local copy, which would typically be created by update_mavlink.py
dialect_marsh = mavlinkdialect("./mavlink_repo/message_definitions/v1.0/marsh.xml");
logimport_marsh = mavlinktlog("./data/YYMMDDTHHMMSS_comment.tlog", dialect_marsh);

mps_msgs = readmsg(logimport,'MessageName','MOTION_PLATFORM_STATE');
mps_data = mps_msgs.Messages{1};
```
