# Controls

Also referred to as pilot inceptors, these nodes should send [MARSH_TYPE_CONTROLS](../mavlink/marsh.md#MARSH_TYPE_CONTROLS) in their [HEARTBEAT](../mavlink/minimal.md#HEARTBEAT) message, and send the pilot inputs in [MANUAL_CONTROL](../mavlink/common.md#MANUAL_CONTROL).

Currently the main implementation is [`joystick_controls.py`](https://github.com/marsh-sim/sim-nodes/blob/main/joystick_controls.py) for generic USB HID devices. Axis mapping can be adjusted with parameters, but it is already configured for:

- Thrustmaster T-Flight HOTAS X (make sure the switch is in PC position, not PS3)
- ATTILA-Sim controls using Arduino Leonardo
  
Alternatively there is [`labjack_controls.py`](https://github.com/marsh-sim/sim-nodes/blob/main/labjack_controls.py) for measuring analog sensors using [Labjack T4 board](https://labjack.com/products/labjack-t4).

## Roadmap

To support flight control systems as a node separate from flight models, the FCS will send [MANUAL_CONTROL](../mavlink/common.md#MANUAL_CONTROL) when used.
This means that all the control scripts here should be configurable to send [MANUAL_SETPOINT](../mavlink/common.md#MANUAL_SETPOINT) with `mode_switch` set to [MARSH_MANUAL_SETPOINT_MODE_DEFAULT](../mavlink/marsh.md#MARSH_MANUAL_SETPOINT_MODE_DEFAULT) to differentiate between controls before and after FCS.

To support control inputs sent from more than one device, the flight model implementations should be able to only update valid values from [MANUAL_CONTROL](../mavlink/common.md#MANUAL_CONTROL) messages.
Until that is the case, the recommended approach is to handle that by forwarding in the controls node, cf. `labjack_controls.py` with `--cyclic-port` argument.
