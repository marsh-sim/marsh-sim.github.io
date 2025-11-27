# MARSH Dialect

This page documents all extensions to MAVLink that were required for the simulator.

The definitions are in the [marsh.xml file](https://github.com/marsh-sim/mavlink/blob/dialect/message_definitions/v1.0/marsh.xml) on the [`dialect` branch](https://github.com/marsh-sim/mavlink/tree/dialect) in our fork of main [MAVLink repository](https://github.com/mavlink/mavlink).
All other projects need to generate and appropriate libraries, following the [mavlink.io – Generating MAVLink Libraries](https://mavlink.io/en/getting_started/generate_libraries.html) documentation.

When in need of a definition for a given functionality which is not covered here, first consult the Common Message Set, both [our subset](./common.md) and [full list](https://mavlink.io/en/messages/common.html).
If a new definition is actually needed, follow the original guide on [how to define MAVLink Messages & Enums](https://mavlink.io/en/guide/define_xml_element.html).

Changing message definitions (id, field names, types, order) breaks over-the-wire compatibility by design.
Thus it's **strongly** recommended to avoid doing that.
Also, if a functionality can be achieved just by defining some new enums or commands, this means that the code will be able to use upstream MAVLink libraries without modifications.

!!! note
    The ids of all messages have been changed in [commit 3621719](https://github.com/marsh-sim/mavlink/commit/36217197c05040c41e6a427cb4908ca40106d83e) on 2025-05-16 for inclusion in the upstream MAVLink repository.
    Custom messages saved in `.tlog` files before that change will not be recognised by newer code.
    The `pymavlink` library includes [`mavtranslatelog.py`](https://github.com/ArduPilot/pymavlink/blob/master/tools/mavtranslatelog.py) tool which was written to resolve that.

<!-- markdownlint-disable -->
<!-- AUTO-GENERATED PART BELOW, DO NOT MODIFY BY HAND -->

## Definition list

Generated on 2024-06-26T16:15:45 from commit [c0d8d14](https://github.com/marsh-sim/mavlink/tree/c0d8d14c0c71a1b78d1471b89d2652bb106a8d4e)

<ul>
 <li><a href="#enums">Enums</a><ul>
  <li><a href="#MARSH_COMPONENT">MARSH_COMPONENT</a></li>
  <li><a href="#MARSH_MODE_FLAGS">MARSH_MODE_FLAGS</a></li>
  <li><a href="#CONTROL_AXIS">CONTROL_AXIS</a></li>
  <li><a href="#MOTION_PLATFORM_MODE">MOTION_PLATFORM_MODE</a></li>
  <li><a href="#MOTION_PLATFORM_HEALTH">MOTION_PLATFORM_HEALTH</a></li>
  <li><a href="#REXROTH_MOTION_PLATFORM_ERROR">REXROTH_MOTION_PLATFORM_ERROR</a></li>
 </ul></li>
 <li><a href="#mav_commands">Mav Commands</a><ul>
 </ul></li>
 <li><a href="#messages">Messages</a><ul>
  <li><a href="#CONTROL_LOADING_AXIS">CONTROL_LOADING_AXIS</a></li>
  <li><a href="#MOTION_PLATFORM_STATE">MOTION_PLATFORM_STATE</a></li>
  <li><a href="#REXROTH_MOTION_PLATFORM">REXROTH_MOTION_PLATFORM</a></li>
  <li><a href="#MOTION_CUE_EXTRA">MOTION_CUE_EXTRA</a></li>
  <li><a href="#EYE_TRACKING_DATA">EYE_TRACKING_DATA</a></li>
 </ul></li>
</ul>
<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="https://mavlink.io/en/messages/common.html">common.xml</a>
  </p>
  <h2>MAVLink Protocol Version</h2>
  <p>The current MAVLink version is 2.3. The minor version numbers (after the dot) range from 1-255.</p>
  <p>This file has protocol dialect: 2.</p>
  <h2 id="enums">MAVLink Type Enumerations</h2>
  <h3 id="MARSH_COMPONENT">MARSH_COMPONENT</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>Component ids (values) for different nodes of the simulator network (flight model, controls, visualisation etc.). Components will always receive messages from the Manager relevant for their ID. Only the first component in a network with a given system ID and component ID will have its messages forwarded by the Manager, all other ones will only be treated as output (will be shadowed). This enum is a redefinition of MAV_COMP_ID_USER# messages from <a href="#MAV_COMPONENT">MAV_COMPONENT</a> documented at https://mavlink.io/en/messages/common.html#MAV_COMPONENT</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MARSH_COMP_ID_MANAGER">
     <td>25</td>
     <td>
      <a href="#MARSH_COMP_ID_MANAGER">MARSH_COMP_ID_MANAGER</a>
     </td>
     <td>The simulation manager responsible for routing packets between different nodes. Typically MARSH Manager, see https://marsh-sim.github.io/manager.html</td>
    </tr>
    <tr id="MARSH_COMP_ID_FLIGHT_MODEL">
     <td>26</td>
     <td>
      <a href="#MARSH_COMP_ID_FLIGHT_MODEL">MARSH_COMP_ID_FLIGHT_MODEL</a>
     </td>
     <td>Component simulating flight dynamics of the aircraft.</td>
    </tr>
    <tr id="MARSH_COMP_ID_CONTROLS">
     <td>27</td>
     <td>
      <a href="#MARSH_COMP_ID_CONTROLS">MARSH_COMP_ID_CONTROLS</a>
     </td>
     <td>Component providing pilot control inputs.</td>
    </tr>
    <tr id="MARSH_COMP_ID_VISUALISATION">
     <td>28</td>
     <td>
      <a href="#MARSH_COMP_ID_VISUALISATION">MARSH_COMP_ID_VISUALISATION</a>
     </td>
     <td>Component showing the visual situation to the pilot.</td>
    </tr>
    <tr id="MARSH_COMP_ID_INSTRUMENTS">
     <td>29</td>
     <td>
      <a href="#MARSH_COMP_ID_INSTRUMENTS">MARSH_COMP_ID_INSTRUMENTS</a>
     </td>
     <td>Component implementing pilot instrument panel.</td>
    </tr>
    <tr id="MARSH_COMP_ID_MOTION_PLATFORM">
     <td>30</td>
     <td>
      <a href="#MARSH_COMP_ID_MOTION_PLATFORM">MARSH_COMP_ID_MOTION_PLATFORM</a>
     </td>
     <td>Component that moves the entire cockpit for motion cueing.</td>
    </tr>
    <tr id="MARSH_COMP_ID_GSEAT">
     <td>31</td>
     <td>
      <a href="#MARSH_COMP_ID_GSEAT">MARSH_COMP_ID_GSEAT</a>
     </td>
     <td>Component for in-seat motion cueing.</td>
    </tr>
    <tr id="MARSH_COMP_ID_EYE_TRACKER">
     <td>32</td>
     <td>
      <a href="#MARSH_COMP_ID_EYE_TRACKER">MARSH_COMP_ID_EYE_TRACKER</a>
     </td>
     <td>Component providing gaze data of pilot eyes.</td>
    </tr>
    <tr id="MARSH_COMP_ID_CONTROL_LOADING">
     <td>33</td>
     <td>
      <a href="#MARSH_COMP_ID_CONTROL_LOADING">MARSH_COMP_ID_CONTROL_LOADING</a>
     </td>
     <td>Component measuring and actuating forces on pilot control inputs.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="MARSH_MODE_FLAGS">MARSH_MODE_FLAGS</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>These values are MARSH-specific modes intended to be sent in custom_mode field of HEARTBEAT message.
        Prefer defining values in the most significant byte (between 2^24 and 2^31) to leave the lower three bytes to contain a message id</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MARSH_MODE_SINGLE_MESSAGE">
     <td>0x1000000</td>
     <td>
      <a href="#MARSH_MODE_SINGLE_MESSAGE">MARSH_MODE_SINGLE_MESSAGE</a>
     </td>
     <td>Request Manager to only send one specific message, advised for very resource limited nodes or with control flow limitations like Simulink.
          That message id should be in the lower three bytes of the mode, which can be done by adding it to the flags.</td>
    </tr>
    <tr id="MARSH_MODE_ALL_MESSAGES">
     <td>0x2000000</td>
     <td>
      <a href="#MARSH_MODE_ALL_MESSAGES">MARSH_MODE_ALL_MESSAGES</a>
     </td>
     <td>Request Manager to send every message going out to any of the clients.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="CONTROL_AXIS">CONTROL_AXIS</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>Specific axis of pilot control inputs, with order corresponding to x, y, z, r fields in <a href="#MANUAL_CONTROL">MANUAL_CONTROL</a> message.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="CONTROL_AXIS_PITCH">
     <td>0</td>
     <td>
      <a href="#CONTROL_AXIS_PITCH">CONTROL_AXIS_PITCH</a>
     </td>
     <td>Pitch axis, with positive values corresponding to stick forward movement, causing the vehicle to move nose down. For helicopters this is longitudinal cyclic.</td>
    </tr>
    <tr id="CONTROL_AXIS_ROLL">
     <td>1</td>
     <td>
      <a href="#CONTROL_AXIS_ROLL">CONTROL_AXIS_ROLL</a>
     </td>
     <td>Roll axis, with positive values corresponding to stick right movement, causing the vehicle to roll right. For helicopters this is lateral cyclic.</td>
    </tr>
    <tr id="CONTROL_AXIS_THRUST">
     <td>2</td>
     <td>
      <a href="#CONTROL_AXIS_THRUST">CONTROL_AXIS_THRUST</a>
     </td>
     <td>Main thrust, with positive values corresponding to going faster and higher. For helicopters this is collective.</td>
    </tr>
    <tr id="CONTROL_AXIS_YAW">
     <td>3</td>
     <td>
      <a href="#CONTROL_AXIS_YAW">CONTROL_AXIS_YAW</a>
     </td>
     <td>Yaw axis, with positive values corresponding to pushing right pedal, causing the vehicle to face right direction. For helicopters this is tail collective.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="MOTION_PLATFORM_MODE">MOTION_PLATFORM_MODE</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>Mode of a motion platform system.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MOTION_PLATFORM_MODE_UNKNOWN">
     <td>0</td>
     <td>
      <a href="#MOTION_PLATFORM_MODE_UNKNOWN">MOTION_PLATFORM_MODE_UNKNOWN</a>
     </td>
     <td>Mode information is unsupported on this device.</td>
    </tr>
    <tr id="MOTION_PLATFORM_MODE_UNINITIALIZED">
     <td>1</td>
     <td>
      <a href="#MOTION_PLATFORM_MODE_UNINITIALIZED">MOTION_PLATFORM_MODE_UNINITIALIZED</a>
     </td>
     <td>Mode is currently not available, but may be in different condition.</td>
    </tr>
    <tr id="MOTION_PLATFORM_MODE_OFF">
     <td>2</td>
     <td>
      <a href="#MOTION_PLATFORM_MODE_OFF">MOTION_PLATFORM_MODE_OFF</a>
     </td>
     <td>Platform actuators are turned off, but control system is responsive.</td>
    </tr>
    <tr id="MOTION_PLATFORM_MODE_SETTLED">
     <td>3</td>
     <td>
      <a href="#MOTION_PLATFORM_MODE_SETTLED">MOTION_PLATFORM_MODE_SETTLED</a>
     </td>
     <td>Platform is in the lowest position and/or locked, appropriate for personnel entry.</td>
    </tr>
    <tr id="MOTION_PLATFORM_MODE_NEUTRAL">
     <td>4</td>
     <td>
      <a href="#MOTION_PLATFORM_MODE_NEUTRAL">MOTION_PLATFORM_MODE_NEUTRAL</a>
     </td>
     <td>Platform is in a neutral reference position, not accepting movement commands.</td>
    </tr>
    <tr id="MOTION_PLATFORM_MODE_FROZEN">
     <td>5</td>
     <td>
      <a href="#MOTION_PLATFORM_MODE_FROZEN">MOTION_PLATFORM_MODE_FROZEN</a>
     </td>
     <td>Platform is stopped in any position, not accepting movement commands.</td>
    </tr>
    <tr id="MOTION_PLATFORM_MODE_ENGAGED">
     <td>6</td>
     <td>
      <a href="#MOTION_PLATFORM_MODE_ENGAGED">MOTION_PLATFORM_MODE_ENGAGED</a>
     </td>
     <td>Platform is in any position, accepting movement commands.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="MOTION_PLATFORM_HEALTH">MOTION_PLATFORM_HEALTH</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>General error state of a motion platform system.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MOTION_PLATFORM_HEALTH_OK">
     <td>0</td>
     <td>
      <a href="#MOTION_PLATFORM_HEALTH_OK">MOTION_PLATFORM_HEALTH_OK</a>
     </td>
     <td>System is operating correctly.</td>
    </tr>
    <tr id="MOTION_PLATFORM_HEALTH_WARNING">
     <td>1</td>
     <td>
      <a href="#MOTION_PLATFORM_HEALTH_WARNING">MOTION_PLATFORM_HEALTH_WARNING</a>
     </td>
     <td>There is at least one warning present, but operation can be continued.</td>
    </tr>
    <tr id="MOTION_PLATFORM_HEALTH_ERROR">
     <td>2</td>
     <td>
      <a href="#MOTION_PLATFORM_HEALTH_ERROR">MOTION_PLATFORM_HEALTH_ERROR</a>
     </td>
     <td>There is a failure or misconfiguration that requires operator's attention for correct operation.</td>
    </tr>
    <tr id="MOTION_PLATFORM_HEALTH_CRITICAL">
     <td>3</td>
     <td>
      <a href="#MOTION_PLATFORM_HEALTH_CRITICAL">MOTION_PLATFORM_HEALTH_CRITICAL</a>
     </td>
     <td>There is a major failure that requires immediate operator action to maintain safety.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="REXROTH_MOTION_PLATFORM_ERROR">REXROTH_MOTION_PLATFORM_ERROR</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>Error codes specific to eMotion Motion System from Bosch Rexroth. Details described in GENERIC-02-30-7100-IML-0700 document.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="REXROTH_ERR_OK">
     <td>0</td>
     <td>
      <a href="#REXROTH_ERR_OK">REXROTH_ERR_OK</a>
     </td>
     <td>No error.</td>
    </tr>
    <tr id="REXROTH_ERR_WA_EXCESSIVE_TORQUE_DIFFERENCE">
     <td>59</td>
     <td>
      <a href="#REXROTH_ERR_WA_EXCESSIVE_TORQUE_DIFFERENCE">REXROTH_ERR_WA_EXCESSIVE_TORQUE_DIFFERENCE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_REMOTE_ACCESS_ACTIVE">
     <td>60</td>
     <td>
      <a href="#REXROTH_ERR_WA_REMOTE_ACCESS_ACTIVE">REXROTH_ERR_WA_REMOTE_ACCESS_ACTIVE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_NON_CRITICAL_CIRCUIT_BREAKER">
     <td>61</td>
     <td>
      <a href="#REXROTH_ERR_WA_NON_CRITICAL_CIRCUIT_BREAKER">REXROTH_ERR_WA_NON_CRITICAL_CIRCUIT_BREAKER</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_SEAL_CHECK_POSITION_HIGH">
     <td>62</td>
     <td>
      <a href="#REXROTH_ERR_WA_SEAL_CHECK_POSITION_HIGH">REXROTH_ERR_WA_SEAL_CHECK_POSITION_HIGH</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_SEAL_CHECK_POSITION_LOW">
     <td>63</td>
     <td>
      <a href="#REXROTH_ERR_WA_SEAL_CHECK_POSITION_LOW">REXROTH_ERR_WA_SEAL_CHECK_POSITION_LOW</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_FRAMECOUNTER_FAIL">
     <td>64</td>
     <td>
      <a href="#REXROTH_ERR_WA_FRAMECOUNTER_FAIL">REXROTH_ERR_WA_FRAMECOUNTER_FAIL</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_UNEXPECTED_STARTUP">
     <td>65</td>
     <td>
      <a href="#REXROTH_ERR_WA_UNEXPECTED_STARTUP">REXROTH_ERR_WA_UNEXPECTED_STARTUP</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_UPS_BATTERY_FAIL">
     <td>75</td>
     <td>
      <a href="#REXROTH_ERR_WA_UPS_BATTERY_FAIL">REXROTH_ERR_WA_UPS_BATTERY_FAIL</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_PLATFORM_SETTLE_ERROR">
     <td>77</td>
     <td>
      <a href="#REXROTH_ERR_WA_PLATFORM_SETTLE_ERROR">REXROTH_ERR_WA_PLATFORM_SETTLE_ERROR</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_BLEEDER_TEMPERATURE">
     <td>88</td>
     <td>
      <a href="#REXROTH_ERR_WA_BLEEDER_TEMPERATURE">REXROTH_ERR_WA_BLEEDER_TEMPERATURE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_PRESSURE_HIGH">
     <td>92</td>
     <td>
      <a href="#REXROTH_ERR_WA_PRESSURE_HIGH">REXROTH_ERR_WA_PRESSURE_HIGH</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_PRESSURE_LOW">
     <td>93</td>
     <td>
      <a href="#REXROTH_ERR_WA_PRESSURE_LOW">REXROTH_ERR_WA_PRESSURE_LOW</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_BRAKE_UPS_POWER_WARNING">
     <td>94</td>
     <td>
      <a href="#REXROTH_ERR_WA_BRAKE_UPS_POWER_WARNING">REXROTH_ERR_WA_BRAKE_UPS_POWER_WARNING</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_WA_MOTOR_TEMPERATURE_WARNING">
     <td>95</td>
     <td>
      <a href="#REXROTH_ERR_WA_MOTOR_TEMPERATURE_WARNING">REXROTH_ERR_WA_MOTOR_TEMPERATURE_WARNING</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_FORCED_DISENGAGE_CIRCUIT_OPENED">
     <td>96</td>
     <td>
      <a href="#REXROTH_ERR_FD_FORCED_DISENGAGE_CIRCUIT_OPENED">REXROTH_ERR_FD_FORCED_DISENGAGE_CIRCUIT_OPENED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_INVALID_MODE">
     <td>97</td>
     <td>
      <a href="#REXROTH_ERR_FD_INVALID_MODE">REXROTH_ERR_FD_INVALID_MODE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_HOST_DATA_TIME_OUT">
     <td>98</td>
     <td>
      <a href="#REXROTH_ERR_FD_HOST_DATA_TIME_OUT">REXROTH_ERR_FD_HOST_DATA_TIME_OUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_FRAMECOUNTER_FAIL">
     <td>99</td>
     <td>
      <a href="#REXROTH_ERR_FD_FRAMECOUNTER_FAIL">REXROTH_ERR_FD_FRAMECOUNTER_FAIL</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_DOORS_AND_PADS_CIRCUIT_OPENED">
     <td>101</td>
     <td>
      <a href="#REXROTH_ERR_FD_DOORS_AND_PADS_CIRCUIT_OPENED">REXROTH_ERR_FD_DOORS_AND_PADS_CIRCUIT_OPENED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_LOADCHECK_SYSTEM_OVERLOAD">
     <td>102</td>
     <td>
      <a href="#REXROTH_ERR_FD_LOADCHECK_SYSTEM_OVERLOAD">REXROTH_ERR_FD_LOADCHECK_SYSTEM_OVERLOAD</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_LOADCHECK_ACTUATOR_OVERLOAD">
     <td>103</td>
     <td>
      <a href="#REXROTH_ERR_FD_LOADCHECK_ACTUATOR_OVERLOAD">REXROTH_ERR_FD_LOADCHECK_ACTUATOR_OVERLOAD</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_BRAKE_UPS_POWER_ERROR">
     <td>104</td>
     <td>
      <a href="#REXROTH_ERR_FD_BRAKE_UPS_POWER_ERROR">REXROTH_ERR_FD_BRAKE_UPS_POWER_ERROR</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_MOTOR_TEMPERATURE_ERROR">
     <td>105</td>
     <td>
      <a href="#REXROTH_ERR_FD_MOTOR_TEMPERATURE_ERROR">REXROTH_ERR_FD_MOTOR_TEMPERATURE_ERROR</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_MOTION_ENABLE_CIRCUIT_OPENED">
     <td>107</td>
     <td>
      <a href="#REXROTH_ERR_FD_MOTION_ENABLE_CIRCUIT_OPENED">REXROTH_ERR_FD_MOTION_ENABLE_CIRCUIT_OPENED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_HOST_DATA_INVALID">
     <td>110</td>
     <td>
      <a href="#REXROTH_ERR_FD_HOST_DATA_INVALID">REXROTH_ERR_FD_HOST_DATA_INVALID</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_LOADCHECK_ACTUATOR_UNDERLOAD">
     <td>113</td>
     <td>
      <a href="#REXROTH_ERR_FD_LOADCHECK_ACTUATOR_UNDERLOAD">REXROTH_ERR_FD_LOADCHECK_ACTUATOR_UNDERLOAD</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_SEAL_CHECK_POSITION_TOO_HIGH">
     <td>115</td>
     <td>
      <a href="#REXROTH_ERR_FD_SEAL_CHECK_POSITION_TOO_HIGH">REXROTH_ERR_FD_SEAL_CHECK_POSITION_TOO_HIGH</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_SEAL_CHECK_POSITION_TOO_LOW">
     <td>116</td>
     <td>
      <a href="#REXROTH_ERR_FD_SEAL_CHECK_POSITION_TOO_LOW">REXROTH_ERR_FD_SEAL_CHECK_POSITION_TOO_LOW</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_RAMP_NOT_UP">
     <td>117</td>
     <td>
      <a href="#REXROTH_ERR_FD_RAMP_NOT_UP">REXROTH_ERR_FD_RAMP_NOT_UP</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_DRIVE_WARNING">
     <td>120</td>
     <td>
      <a href="#REXROTH_ERR_FD_DRIVE_WARNING">REXROTH_ERR_FD_DRIVE_WARNING</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_PRESSURE_TOO_HIGH">
     <td>123</td>
     <td>
      <a href="#REXROTH_ERR_FD_PRESSURE_TOO_HIGH">REXROTH_ERR_FD_PRESSURE_TOO_HIGH</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_PRESSURE_TOO_LOW">
     <td>124</td>
     <td>
      <a href="#REXROTH_ERR_FD_PRESSURE_TOO_LOW">REXROTH_ERR_FD_PRESSURE_TOO_LOW</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_ACTUATOR_POSITION_DOES_NOT_MATCH_SWITCH_POSITION">
     <td>125</td>
     <td>
      <a href="#REXROTH_ERR_FD_ACTUATOR_POSITION_DOES_NOT_MATCH_SWITCH_POSITION">REXROTH_ERR_FD_ACTUATOR_POSITION_DOES_NOT_MATCH_SWITCH_POSITION</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_SETTLED_SWITCH_NOT_DETECTED_BY_SAFETY_HOMING_PROCEDURE">
     <td>126</td>
     <td>
      <a href="#REXROTH_ERR_FD_SETTLED_SWITCH_NOT_DETECTED_BY_SAFETY_HOMING_PROCEDURE">REXROTH_ERR_FD_SETTLED_SWITCH_NOT_DETECTED_BY_SAFETY_HOMING_PROCEDURE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FD_POWER_OFF_LINE_FAILURE">
     <td>127</td>
     <td>
      <a href="#REXROTH_ERR_FD_POWER_OFF_LINE_FAILURE">REXROTH_ERR_FD_POWER_OFF_LINE_FAILURE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_MOTION_ENABLE_CIRCUIT_OPENED">
     <td>100</td>
     <td>
      <a href="#REXROTH_ERR_ES_MOTION_ENABLE_CIRCUIT_OPENED">REXROTH_ERR_ES_MOTION_ENABLE_CIRCUIT_OPENED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_EMERGENCY_STOP_CIRCUIT_OPENED">
     <td>160</td>
     <td>
      <a href="#REXROTH_ERR_ES_EMERGENCY_STOP_CIRCUIT_OPENED">REXROTH_ERR_ES_EMERGENCY_STOP_CIRCUIT_OPENED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_RAMP_NOT_UP">
     <td>164</td>
     <td>
      <a href="#REXROTH_ERR_ES_RAMP_NOT_UP">REXROTH_ERR_ES_RAMP_NOT_UP</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_MOVE_RAMP_UP_TIMEOUT">
     <td>172</td>
     <td>
      <a href="#REXROTH_ERR_ES_MOVE_RAMP_UP_TIMEOUT">REXROTH_ERR_ES_MOVE_RAMP_UP_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_MOVE_RAMP_DOWN_TIMEOUT">
     <td>173</td>
     <td>
      <a href="#REXROTH_ERR_ES_MOVE_RAMP_DOWN_TIMEOUT">REXROTH_ERR_ES_MOVE_RAMP_DOWN_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_MOVE_PLATFORM_UP_TIMEOUT">
     <td>174</td>
     <td>
      <a href="#REXROTH_ERR_ES_MOVE_PLATFORM_UP_TIMEOUT">REXROTH_ERR_ES_MOVE_PLATFORM_UP_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_MOVE_PLATFORM_DOWN_TIMEOUT">
     <td>175</td>
     <td>
      <a href="#REXROTH_ERR_ES_MOVE_PLATFORM_DOWN_TIMEOUT">REXROTH_ERR_ES_MOVE_PLATFORM_DOWN_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_CIRCUIT_BREAKER">
     <td>184</td>
     <td>
      <a href="#REXROTH_ERR_ES_CIRCUIT_BREAKER">REXROTH_ERR_ES_CIRCUIT_BREAKER</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_YAW_TABLE_POSITION_LIMIT_ACTIVE">
     <td>185</td>
     <td>
      <a href="#REXROTH_ERR_ES_YAW_TABLE_POSITION_LIMIT_ACTIVE">REXROTH_ERR_ES_YAW_TABLE_POSITION_LIMIT_ACTIVE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_XY_CUSHION">
     <td>186</td>
     <td>
      <a href="#REXROTH_ERR_ES_XY_CUSHION">REXROTH_ERR_ES_XY_CUSHION</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_EXCESSIVE_POSITION_DIFFERENCE">
     <td>193</td>
     <td>
      <a href="#REXROTH_ERR_ES_EXCESSIVE_POSITION_DIFFERENCE">REXROTH_ERR_ES_EXCESSIVE_POSITION_DIFFERENCE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_BRAKE_POWER_FAIL">
     <td>194</td>
     <td>
      <a href="#REXROTH_ERR_ES_BRAKE_POWER_FAIL">REXROTH_ERR_ES_BRAKE_POWER_FAIL</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_MANUAL_BRAKE_RELEASE">
     <td>195</td>
     <td>
      <a href="#REXROTH_ERR_ES_MANUAL_BRAKE_RELEASE">REXROTH_ERR_ES_MANUAL_BRAKE_RELEASE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_RAMP_SWITCH_FAILURE">
     <td>206</td>
     <td>
      <a href="#REXROTH_ERR_ES_RAMP_SWITCH_FAILURE">REXROTH_ERR_ES_RAMP_SWITCH_FAILURE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_BUFFER_CHECK_TIMEOUT">
     <td>207</td>
     <td>
      <a href="#REXROTH_ERR_ES_BUFFER_CHECK_TIMEOUT">REXROTH_ERR_ES_BUFFER_CHECK_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_BUFFER_CHECK_ERROR">
     <td>208</td>
     <td>
      <a href="#REXROTH_ERR_ES_BUFFER_CHECK_ERROR">REXROTH_ERR_ES_BUFFER_CHECK_ERROR</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_ACTUATOR_POSITION_DOES_NOT_MATCH_SWITCH_POSITION">
     <td>209</td>
     <td>
      <a href="#REXROTH_ERR_ES_ACTUATOR_POSITION_DOES_NOT_MATCH_SWITCH_POSITION">REXROTH_ERR_ES_ACTUATOR_POSITION_DOES_NOT_MATCH_SWITCH_POSITION</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_BB_CONTACT_DRIVE_OPEN">
     <td>222</td>
     <td>
      <a href="#REXROTH_ERR_ES_BB_CONTACT_DRIVE_OPEN">REXROTH_ERR_ES_BB_CONTACT_DRIVE_OPEN</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_DRIVE_ERROR">
     <td>223</td>
     <td>
      <a href="#REXROTH_ERR_ES_DRIVE_ERROR">REXROTH_ERR_ES_DRIVE_ERROR</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_POWER_ON_TIMEOUT">
     <td>225</td>
     <td>
      <a href="#REXROTH_ERR_ES_POWER_ON_TIMEOUT">REXROTH_ERR_ES_POWER_ON_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_POWER_OFF_TIMEOUT">
     <td>226</td>
     <td>
      <a href="#REXROTH_ERR_ES_POWER_OFF_TIMEOUT">REXROTH_ERR_ES_POWER_OFF_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_BB_CONTACT_BLEEDER_OPEN">
     <td>230</td>
     <td>
      <a href="#REXROTH_ERR_ES_BB_CONTACT_BLEEDER_OPEN">REXROTH_ERR_ES_BB_CONTACT_BLEEDER_OPEN</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_BB_CONTACT_POWER_SUPPLY_OPEN">
     <td>231</td>
     <td>
      <a href="#REXROTH_ERR_ES_BB_CONTACT_POWER_SUPPLY_OPEN">REXROTH_ERR_ES_BB_CONTACT_POWER_SUPPLY_OPEN</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_DRIVE_ON_TIMEOUT">
     <td>235</td>
     <td>
      <a href="#REXROTH_ERR_ES_DRIVE_ON_TIMEOUT">REXROTH_ERR_ES_DRIVE_ON_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_DRIVE_OFF_TIMEOUT">
     <td>236</td>
     <td>
      <a href="#REXROTH_ERR_ES_DRIVE_OFF_TIMEOUT">REXROTH_ERR_ES_DRIVE_OFF_TIMEOUT</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_SMOKE_OR_FIRE_DETECTED">
     <td>237</td>
     <td>
      <a href="#REXROTH_ERR_ES_SMOKE_OR_FIRE_DETECTED">REXROTH_ERR_ES_SMOKE_OR_FIRE_DETECTED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_ACTUAL_TORQUE_LIMIT_INVALID">
     <td>238</td>
     <td>
      <a href="#REXROTH_ERR_ES_ACTUAL_TORQUE_LIMIT_INVALID">REXROTH_ERR_ES_ACTUAL_TORQUE_LIMIT_INVALID</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_ABSOLUTE_ENCODER_NOT_IN_REFERENCE">
     <td>239</td>
     <td>
      <a href="#REXROTH_ERR_ES_ABSOLUTE_ENCODER_NOT_IN_REFERENCE">REXROTH_ERR_ES_ABSOLUTE_ENCODER_NOT_IN_REFERENCE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_ES_SOFTWARE_CRASHED">
     <td>250</td>
     <td>
      <a href="#REXROTH_ERR_ES_SOFTWARE_CRASHED">REXROTH_ERR_ES_SOFTWARE_CRASHED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FB_FD_DRIVE_ERROR">
     <td>224</td>
     <td>
      <a href="#REXROTH_ERR_FB_FD_DRIVE_ERROR">REXROTH_ERR_FB_FD_DRIVE_ERROR</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FB_SERCOS_BUS">
     <td>240</td>
     <td>
      <a href="#REXROTH_ERR_FB_SERCOS_BUS">REXROTH_ERR_FB_SERCOS_BUS</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_FB_SERCOS_SLAVE">
     <td>241</td>
     <td>
      <a href="#REXROTH_ERR_FB_SERCOS_SLAVE">REXROTH_ERR_FB_SERCOS_SLAVE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="REXROTH_ERR_EPO_LINE_FAILURE">
     <td>255</td>
     <td>
      <a href="#REXROTH_ERR_EPO_LINE_FAILURE">REXROTH_ERR_EPO_LINE_FAILURE</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <a id="MAV_CMD">
  </a>
  <h2 id="mav_commands">MAVLink Commands (<a href="#mav_commands">MAV_CMD</a>)</h2>
  <blockquote class="alert alert-info clearfix">
   <strong class="fa fa-2x fa-edit">
   </strong>
   <p>MAVLink commands (<a href="#mav_commands">MAV_CMD</a>) and messages are different! These commands define the values of up to 7 parameters that are packaged INSIDE specific messages used in the Mission Protocol and Command Protocol. Use commands for actions in missions or if you need acknowledgment and/or retry logic from a request. Otherwise use messages.</p>
  </blockquote>
  <h2 id="messages">MAVLink Messages</h2>
  <h3 id="CONTROL_LOADING_AXIS">CONTROL_LOADING_AXIS (<a href="#CONTROL_LOADING_AXIS">
    #24401
   </a>
   )
  </h3>
  <p style="color:red">
   <strong>WORK IN PROGRESS:</strong> Do not use in stable production environments (it may change).</p>
  <p>
   <a href="#messages">
    [Message]
   </a>
   <strong>
    (MAVLink 2)
   </strong>Send data about a control axis from a control loading system. This is the primary message for logging data from <a href="#MARSH_COMP_ID_CONTROL_LOADING">MARSH_COMP_ID_CONTROL_LOADING</a>.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>time_boot_ms</td>
     <td>uint32_t</td>
     <td>ms</td>
     <td>
     </td>
     <td>Timestamp (time since system boot).</td>
    </tr>
    <tr>
     <td>axis</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#CONTROL_AXIS">CONTROL_AXIS</a>
     </td>
     <td>Control axis on which the measurements were taken.</td>
    </tr>
    <tr>
     <td>position</td>
     <td>float</td>
     <td>deg</td>
     <td>
     </td>
     <td>Axis position</td>
    </tr>
    <tr>
     <td>velocity</td>
     <td>float</td>
     <td>deg/s</td>
     <td>
     </td>
     <td>Axis velocity</td>
    </tr>
    <tr>
     <td>force</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
     <td>Force applied in the pilot in the direction of movement axis (not gripping force), measured at the position of pilot's third finger (ring). Unit N (Newton), currently not part of mavschema.xsd</td>
    </tr>
   </tbody>
  </table>
  <h3 id="MOTION_PLATFORM_STATE">MOTION_PLATFORM_STATE (<a href="#MOTION_PLATFORM_STATE">
    #24402
   </a>
   )
  </h3>
  <p style="color:red">
   <strong>WORK IN PROGRESS:</strong> Do not use in stable production environments (it may change).</p>
  <p>
   <a href="#messages">
    [Message]
   </a>
   <strong>
    (MAVLink 2)
   </strong>State report for motion platform used for moving the cockpit with the pilot for motion cueing. This is the primary message for MARSH_COMP_ID_MOTION_PLATFORM</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>time_boot_ms</td>
     <td>uint32_t</td>
     <td>ms</td>
     <td>
     </td>
     <td>Timestamp (time since system boot).</td>
    </tr>
    <tr>
     <td>health</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#MOTION_PLATFORM_HEALTH">MOTION_PLATFORM_HEALTH</a>
     </td>
     <td>Generic system health (error and warning) status.</td>
    </tr>
    <tr>
     <td>mode</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#MOTION_PLATFORM_MODE">MOTION_PLATFORM_MODE</a>
     </td>
     <td>Generic system operating mode.</td>
    </tr>
    <tr>
     <td>x</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>X axis (surge) position, positive forward.</td>
    </tr>
    <tr>
     <td>y</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Y axis (sway) position, positive right.</td>
    </tr>
    <tr>
     <td>z</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Z axis (heave) position, positive down.</td>
    </tr>
    <tr>
     <td>pitch</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Pitch position, positive nose up.</td>
    </tr>
    <tr>
     <td>roll</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Roll position, positive right.</td>
    </tr>
    <tr>
     <td>yaw</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Yaw position, positive right.</td>
    </tr>
    <tr>
     <td>vel_x</td>
     <td>float</td>
     <td>m/s</td>
     <td>
     </td>
     <td>X axis (surge) velocity, positive forward.</td>
    </tr>
    <tr>
     <td>vel_y</td>
     <td>float</td>
     <td>m/s</td>
     <td>
     </td>
     <td>Y axis (sway) velocity, positive right.</td>
    </tr>
    <tr>
     <td>vel_z</td>
     <td>float</td>
     <td>m/s</td>
     <td>
     </td>
     <td>Z axis (heave) velocity, positive down.</td>
    </tr>
    <tr>
     <td>vel_pitch</td>
     <td>float</td>
     <td>rad/s</td>
     <td>
     </td>
     <td>Pitch velocity, positive nose up.</td>
    </tr>
    <tr>
     <td>vel_roll</td>
     <td>float</td>
     <td>rad/s</td>
     <td>
     </td>
     <td>Roll velocity, positive right.</td>
    </tr>
    <tr>
     <td>vel_yaw</td>
     <td>float</td>
     <td>rad/s</td>
     <td>
     </td>
     <td>Yaw velocity, positive right.</td>
    </tr>
    <tr>
     <td>acc_x</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>
     </td>
     <td>X axis (surge) acceleration, positive forward.</td>
    </tr>
    <tr>
     <td>acc_y</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>
     </td>
     <td>Y axis (sway) acceleration, positive right.</td>
    </tr>
    <tr>
     <td>acc_z</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>
     </td>
     <td>Z axis (heave) acceleration, positive down.</td>
    </tr>
    <tr>
     <td>acc_pitch</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
     <td>Pitch acceleration, positive nose up. Unit rad/s/s, currently not part of mavschema.xsd</td>
    </tr>
    <tr>
     <td>acc_roll</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
     <td>Roll acceleration, positive right. Unit rad/s/s, currently not part of mavschema.xsd</td>
    </tr>
    <tr>
     <td>acc_yaw</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
     <td>Yaw acceleration, positive right. Unit rad/s/s, currently not part of mavschema.xsd</td>
    </tr>
   </tbody>
  </table>
  <h3 id="REXROTH_MOTION_PLATFORM">REXROTH_MOTION_PLATFORM (<a href="#REXROTH_MOTION_PLATFORM">
    #24403
   </a>
   )
  </h3>
  <p style="color:red">
   <strong>WORK IN PROGRESS:</strong> Do not use in stable production environments (it may change).</p>
  <p>
   <a href="#messages">
    [Message]
   </a>
   <strong>
    (MAVLink 2)
   </strong>State report specific for eMotion Motion System by Bosch Rexroth B.V. Values applicable to motion platforms in general are sent in <a href="#MOTION_PLATFORM_STATE">MOTION_PLATFORM_STATE</a> with the same timestamp. Actuators are numbered in a clockwise direction when looking from above, starting from the front right. Actuator position is 0 when actuator is in mid-stroke.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>time_boot_ms</td>
     <td>uint32_t</td>
     <td>ms</td>
     <td>
     </td>
     <td>Timestamp (time since system boot).</td>
    </tr>
    <tr>
     <td>frame_count</td>
     <td>uint32_t</td>
     <td>
     </td>
     <td>
     </td>
     <td>Number of message as sent by the Motion System.</td>
    </tr>
    <tr>
     <td>motion_status</td>
     <td>uint32_t</td>
     <td>
     </td>
     <td>
     </td>
     <td>Motion Status variable as sent by the system.</td>
    </tr>
    <tr>
     <td>error_code</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#REXROTH_MOTION_PLATFORM_ERROR">REXROTH_MOTION_PLATFORM_ERROR</a>
     </td>
     <td>Error code extracted from motion status.</td>
    </tr>
    <tr>
     <td>actuator1</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Current actuator 1 position.</td>
    </tr>
    <tr>
     <td>actuator2</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Current actuator 2 position.</td>
    </tr>
    <tr>
     <td>actuator3</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Current actuator 3 position.</td>
    </tr>
    <tr>
     <td>actuator4</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Current actuator 4 position.</td>
    </tr>
    <tr>
     <td>actuator5</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Current actuator 5 position.</td>
    </tr>
    <tr>
     <td>actuator6</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Current actuator 6 position.</td>
    </tr>
    <tr>
     <td>platform_setpoint_x</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>X axis (surge) platform setpoint, positive forward.</td>
    </tr>
    <tr>
     <td>platform_setpoint_y</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Y axis (sway) platform setpoint, positive right.</td>
    </tr>
    <tr>
     <td>platform_setpoint_z</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Z axis (heave) platform setpoint, positive down.</td>
    </tr>
    <tr>
     <td>platform_setpoint_pitch</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Pitch platform setpoint, positive nose up.</td>
    </tr>
    <tr>
     <td>platform_setpoint_roll</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Roll platform setpoint, positive right.</td>
    </tr>
    <tr>
     <td>platform_setpoint_yaw</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Yaw platform setpoint, positive right.</td>
    </tr>
    <tr>
     <td>effect_setpoint_x</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>X axis (surge) special effect setpoint, positive forward.</td>
    </tr>
    <tr>
     <td>effect_setpoint_y</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Y axis (sway) special effect setpoint, positive right.</td>
    </tr>
    <tr>
     <td>effect_setpoint_z</td>
     <td>float</td>
     <td>m</td>
     <td>
     </td>
     <td>Z axis (heave) special effect setpoint, positive down.</td>
    </tr>
    <tr>
     <td>effect_setpoint_pitch</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Pitch special effect setpoint, positive nose up.</td>
    </tr>
    <tr>
     <td>effect_setpoint_roll</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Roll special effect setpoint, positive right.</td>
    </tr>
    <tr>
     <td>effect_setpoint_yaw</td>
     <td>float</td>
     <td>rad</td>
     <td>
     </td>
     <td>Yaw special effect setpoint, positive right.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="MOTION_CUE_EXTRA">MOTION_CUE_EXTRA (<a href="#MOTION_CUE_EXTRA">
    #24404
   </a>
   )
  </h3>
  <p style="color:red">
   <strong>WORK IN PROGRESS:</strong> Do not use in stable production environments (it may change).</p>
  <p>
   <a href="#messages">
    [Message]
   </a>
   <strong>
    (MAVLink 2)
   </strong>These values are an extra cue that should be added to accelerations and rotations etc. resulting from aircraft state, with the resulting cue being the sum of the latest aircraft and extra values. An example use case would be a cockpit shaker.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>time_boot_ms</td>
     <td>uint32_t</td>
     <td>ms</td>
     <td>Timestamp (time since system boot).</td>
    </tr>
    <tr>
     <td>vel_pitch</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Pitch velocity, positive nose up.</td>
    </tr>
    <tr>
     <td>vel_roll</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Roll velocity, positive right.</td>
    </tr>
    <tr>
     <td>vel_yaw</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Yaw velocity, positive right.</td>
    </tr>
    <tr>
     <td>acc_x</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>X axis (surge) acceleration, positive forward.</td>
    </tr>
    <tr>
     <td>acc_y</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>Y axis (sway) acceleration, positive right.</td>
    </tr>
    <tr>
     <td>acc_z</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>Z axis (heave) acceleration, positive down.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="EYE_TRACKING_DATA">EYE_TRACKING_DATA (<a href="#EYE_TRACKING_DATA">
    #24405
   </a>
   )
  </h3>
  <p style="color:red">
   <strong>WORK IN PROGRESS:</strong> Do not use in stable production environments (it may change).</p>
  <p>
   <a href="#messages">
    [Message]
   </a>
   <strong>
    (MAVLink 2)
   </strong>Data for tracking of pilot eye gaze. In multi-crew situations, additional trackers should connect with different system id.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>time_usec</td>
     <td>uint64_t</td>
     <td>us</td>
     <td>Timestamp (time since system boot).</td>
    </tr>
    <tr>
     <td>gaze_origin_x</td>
     <td>float</td>
     <td>m</td>
     <td>X axis of gaze origin point, NaN if unknown. The reference system depends on specific application.</td>
    </tr>
    <tr>
     <td>gaze_origin_y</td>
     <td>float</td>
     <td>m</td>
     <td>Y axis of gaze origin point, NaN if unknown. The reference system depends on specific application.</td>
    </tr>
    <tr>
     <td>gaze_origin_z</td>
     <td>float</td>
     <td>m</td>
     <td>Z axis of gaze origin point, NaN if unknown. The reference system depends on specific application.</td>
    </tr>
    <tr>
     <td>gaze_direction_x</td>
     <td>float</td>
     <td>
     </td>
     <td>X axis of gaze direction vector, expected to be normalized to unit magnitude, NaN if unknown. The reference system should match origin point.</td>
    </tr>
    <tr>
     <td>gaze_direction_y</td>
     <td>float</td>
     <td>
     </td>
     <td>Y axis of gaze direction vector, expected to be normalized to unit magnitude, NaN if unknown. The reference system should match origin point.</td>
    </tr>
    <tr>
     <td>gaze_direction_z</td>
     <td>float</td>
     <td>
     </td>
     <td>Z axis of gaze direction vector, expected to be normalized to unit magnitude, NaN if unknown. The reference system should match origin point.</td>
    </tr>
    <tr>
     <td>video_gaze_x</td>
     <td>float</td>
     <td>
     </td>
     <td>Gaze focal point on video feed x value (normalized 0..1, 0 is left, 1 is right), NaN if unknown</td>
    </tr>
    <tr>
     <td>video_gaze_y</td>
     <td>float</td>
     <td>
     </td>
     <td>Gaze focal point on video feed y value (normalized 0..1, 0 is top, 1 is bottom), NaN if unknown</td>
    </tr>
    <tr>
     <td>surface_id</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Identifier of surface for 2D gaze point, or an identified region when surface point is invalid. Set to zero if unknown/unused.</td>
    </tr>
    <tr>
     <td>surface_gaze_x</td>
     <td>float</td>
     <td>
     </td>
     <td>Gaze focal point on surface x value (normalized 0..1, 0 is left, 1 is right), NaN if unknown</td>
    </tr>
    <tr>
     <td>surface_gaze_y</td>
     <td>float</td>
     <td>
     </td>
     <td>Gaze focal point on surface y value (normalized 0..1, 0 is top, 1 is bottom), NaN if unknown</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>
