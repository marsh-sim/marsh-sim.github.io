# MATLAB analysis

!!! note
    Requires the "[UAV Toolbox](https://www.mathworks.com/products/uav.html)" to be installed

The `.tlog` files [saved by MARSH Manager](../manager/README.md#saving-data) can be loaded with [`mavlinktlog`](https://www.mathworks.com/help/uav/ref/mavlinktlog.html) function.
Example code:

```matlab
% This requires a local copy, which would typically be created by update_mavlink.py
dialect = mavlinkdialect("./mavlink_repo/message_definitions/v1.0/marsh.xml");
logimport = mavlinktlog("./data/YYYYMMDDTHHMMSS_comment.tlog", dialect);

sim_state_msgs = readmsg(logimport, 'MessageName', 'SIM_STATE');
sim_state_data = sim_state_msgs.Messages{1};
mps_msgs = readmsg(logimport, 'MessageName', 'MOTION_PLATFORM_STATE');
mps_data = mps_msgs.Messages{1};
```
