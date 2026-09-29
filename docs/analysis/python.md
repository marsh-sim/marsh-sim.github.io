# Python analysis

Requires `pymavlink` to be installed.
If you need to parse messages recently introduced to MARSH that are not part of `pymavlink` yet, you will need to generate the code to read them.
The script [`update_mavlink.py`](https://github.com/marsh-sim/sim-nodes/blob/main/update_mavlink.py) in `sim-nodes` repository can automatically download and generate the code for you.

```python
import mavlink_all as mavlink
from pymavlink import mavutil

log_file = "./data/YYYYMMDDTHHMMSS_comment.tlog"

# We'll output the data as CSV in this example
print("t,roll,pitch,yaw")

parameters: dict[str, float] = {}
mav = mavutil.mavlink_connection(log_file, dialect="all")
start_time: float | None = None
while message := mav.recv_msg():
    # Convert to relative time from first message for simplicity
    if start_time is None:
        start_time = message._timestamp
    t = message._timestamp - start_time + parsed_time

    if message.get_type() == "PARAM_VALUE":
        # Save parameters that were in this run
        parameters[message.param_id] = message.param_value
    elif message.get_type() == "SIM_STATE":
        # After checking the message type we know it has fields that we want
        print(f"{t},{message.roll},{message.pitch},{message.yaw}")
```

!!! tip
    For practical data analysis, the authors have also used and recommend [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [pandas](https://pandas.pydata.org/), [SciPy](https://scipy.org/) and [marimo](https://marimo.io/) packages.
    Consult these links for more information on their usage.

!!! warning
    If you want to parse custom messages that are not part of `pymavlink` you need to run this workaround once after installation:

```python
# Resolve problem with mavutil not using custom dialect
import pymavlink.dialects.v20.all as _file_pymavlink_all  # pyright:ignore[reportMissingTypeStubs]
import mavlink_all as _file_marsh_all
import shutil

# HACK: mavutil always loads the modules by name from pymavlink directory, have to replace
_ = shutil.copy(_file_marsh_all.__file__, _file_pymavlink_all.__file__)
```
