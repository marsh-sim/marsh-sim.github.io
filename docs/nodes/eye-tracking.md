# Eye tracking

This article describes setup for eye tracking experiments using a wearable eye tracker (not VR helmet).

## Prerequisites

- Eye tracking device, we're using [Pupil Labs Core](https://pupil-labs.com/products/core)
- [Pupil Capture](https://github.com/pupil-labs/pupil) software on a computer with USB-C port to which the device will be connected
- [PureRef](https://www.pureref.com/) art reference program for showing marker overlay **on every computer showing a pilot screen**
- Download `.pur` files from [eye_tracking folder in `sim-nodes` repo](https://github.com/marsh-sim/sim-nodes/tree/main/eye_tracking) on computers with PureRef

## Usage

The PureRef scenes are prepared to display [AprilTags tag36h11 markers](https://github.com/AprilRobotics/apriltag-imgs/tree/master/tag36h11) in every corner of the screen.

Steps to use a scene on a given display.
The PureRef menu is opened by right clicking in the window, or any of the images when shown as overlay.

1. Open the `.pur` file
1. With no selection, click "Mode > Overlay Selection" and accept
1. Select **all four** images, can be done with `Ctrl+A` if some of them are off screen, drag and scale to fit the corners of the display
1. Check "Mode > Always On Top"
1. Check "Canvas > Lock Canvas"
1. Check "Mode > Transparent To Mouse" and accept

If you need to change anything after this point, you need to focus the PureRef window in a different way than clicking on it, for example from the taskbar.

## Defined screens

The following are provided as reference for what is in `.pur` files found in the repository, and to propose some consistent values for `surface_id` field of [EYE_TRACKING_DATA](../mavlink/marsh.md#EYE_TRACKING_DATA) message.

### Instruments

Surface id **1**, example: page `pfd` of [lidia](./instruments.md).

![diagram of AprilTags layout for instrument screen](./markers_instruments.svg)

### Outside view

Surface id **2** with a view outside the aircraft, or just the screen with visualisation

![diagram of AprilTags layout for outside view](./markers_outside_view.svg)

### Inceptors

Surface id **3** showing control positions, example: page `controls` of [lidia](./instruments.md).

![diagram of AprilTags layout for control positions](./markers_inceptors.svg)

### Drone control

Surface id **4** for controlling cooperating Unmanned Aerial Vehicles (UAVs), example: an instance of [QGroundControl](http://qgroundcontrol.com/)

![diagram of AprilTags layout for drone control](./markers_drone_control.svg)

## Creating new screens

The images in the AprilTags repository have a very small resolution, with pixels corresponding to marker features.
After loading them into PureRef and scaling to a a larger size they will look blurry.
To fix that, toggle image sampling on selected images to "nearest neighbor" with `Alt+T`, and/or set this sampling as default in the settings.

To keep a consistent size, open one of the reference images in full screen, and adjust one of the markers to match.
Once one marker in a scene has a correct size, select it first followed by any other, then right click and select "Images > Normalize > From first > Size".

Similarly, when an image is positioned in a desired corner, select the reference first, then an image you want to move and use "Images > Align > Left/Up, etc.", which can also be done with `Ctrl` and arrow keys.

!!! warning
    As of writing, the images cannot cover the task bar in Windows.
    It's suggested to align them with the taskbar instead, but when defining the surface in Pupil Capture, move the corner to corner of the display.

When finished, you can save the PureRef scene to `.pur` file using "Save > Save as" menu.
This file is self-contained, including the data of all used images.

With the overlay shown on screen, follow the instructions about [Surface Tracking in Pupil Capture documentation](https://docs.pupil-labs.com/core/software/pupil-capture/#surface-tracking).
For the [`pupil_eye_tracker`](https://github.com/marsh-sim/sim-nodes/blob/main/pupil_eye_tracker.py) script to correctly label the surfaces, name the surfaces same way as subsections in [Defined screens](#defined-screens).
