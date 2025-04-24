# MARSH Manager

The `marsh-mgr` program is a graphical application for Linux and Windows that serves as the central node in the simulator architecture.

It is meant as a single tool to provide:

- Communicating data between simulator parts (nodes)
- Controlling the simulation execution and configuration
- Logging and replaying the simulation data

![diagram showing MARSH Manager as central element of the simulator](./simulator_variants_manager.svg)

## Installation

If your operating system or processor architecture do not have a release provided, you can build the application from source code using the [developer documentation](./development.md)

### Linux

Download the `.AppImage` file from the [Releases page](https://github.com/marsh-sim/marsh-manager/releases).
Make it executable, [using the GUI](https://docs.appimage.org/introduction/quickstart.html#using-the-gui), or with the following command:

```bash
chmod +x MARSH_Manager-x86_64.AppImage
```

If you haven't used AppImage files before you might need to install the FUSE library.
The command below was tested to work on Ubuntu 22.04, if you still have problems, see [AppImage documentation about FUSE](https://docs.appimage.org/user-guide/troubleshooting/fuse.html).

```bash
sudo apt install libfuse2
```

Run the program using GUI, or from terminal:

```bash
./MARSH_Manager-x86_64.AppImage
```

#### Optional: register as `marsh-mgr` command

It is [recommended](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html#variables) to put your own executables in `~/.local/bin`

```bash
mkdir -p ~/.local/bin
cp ./MARSH_Manager-x86_64.AppImage ~/.local/bin/marsh-mgr
```

If the command `marsh-mgr` is still not found at this point, this directory isn't in PATH variable, where system looks for executables (you can display it with `echo $PATH`).
An example fix for users of bash (default shell in Ubuntu):

```bash
echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Windows

Download and unpack the ZIP file for Windows from the [Releases page](https://github.com/marsh-sim/marsh-manager/releases).
Run `marsh-mgr.exe`.

!!! note
    This is a temporary solution, expect some changes.

## Usage

Start the application executable, dependent on your operating system may be the `marsh-mgr` command.
If other nodes are running on different computers, configure "manager address" to IP address of the computer running the manager.

![screenshot of MARSH Manager window](main_window.png)

### Saving data

The user can choose a folder to save the data, the files are named depending on the logging start time to avoid overwriting previous saves.
A "file comment" can be added which will be a part of the generated filename, but will also be saved as a [STATUSTEXT](../mavlink/common.md#STATUSTEXT) message at the start of the file.
The maximum length for file comment is 50 characters.

!!! tip
    You can use the file comment to help with your data processing afterwards: write test subject initials, short description of test case etc.

The data files saved are "MAVLink telemetry log", recognizable by `.tlog` extension.
This binary file format is a de facto standard between multiple UAV flight stacks, the file just contains MAVLink messages, each preceded by a timestamp in microseconds.

We have documentation for analysis in:

- [MATLAB](../analysis/matlab.md).

There are also multiple external tools available for viewing the logs, notable examples:

- [pymavlink library](https://github.com/ArduPilot/pymavlink) which is used for generating libraries and communication for Python also has [`mavlogdump.py` script](https://github.com/ArduPilot/pymavlink/blob/master/tools/mavlogdump.py)
- Some online tools like [UAV Log Viewer](https://plot.ardupilot.org/) can read `.tlog` files.
- ArduPilot's [MAVExplorer](https://ardupilot.org/dev/docs/using-mavexplorer-for-log-analysis.html) can be used for plots, filtering data and showing it on a map

## Roadmap

The following are already planned future features of MARSH Manager, approximately in the order of priority / expected implementation date:

- Emit parameters to log for nodes with [MARSH_MODE_SINGLE_MESSAGE](../mavlink/marsh.md#MARSH_MODE_SINGLE_MESSAGE)
- Distribution:
    - Automated builds and releases on GitHub
    - Windows package (with `windeployqt`)
- Connecting nodes on serial port
- Button to remove timed out nodes from network view
- Graph visualisation, considering these candidate solutions:
    - [NASA OpenMCT](https://github.com/nasa/openmct) or [Grafana](https://github.com/grafana/grafana)
        - Expect updates over WebSocket, see [mavlink2rest](https://github.com/mavlink/mavlink2rest)
    - In-app with [Qt Charts](https://doc.qt.io/qt-6.5/qtcharts-overview.html)
- Using full message definitions:
    - Displaying units of message fields
        - Displaying angular values sent as radians also as degrees
    - Showing text identifiers for enum values
        - Find length of common prefix from enum names
        - Show bitfields as a collection of flags
    - *Maybe later:* using tooltips to show descriptions for message fields and enum constants
- Extend support for [Parameter Protocol](https://mavlink.io/en/services/parameter.html):
    - Setting parameters of multiple components based on test matrix
    - Parameter descriptions with [Component Metadata Protocol](https://mavlink.io/en/services/component_information.html)
- Console showing [STATUSTEXT](../mavlink/common.md#STATUSTEXT) messages
- Replaying log files
- Allow unregistered clients to do *some* operations that would make sense for simple utility scripts, for example parameters

## Contributing

Contributions to [documentation](../documentation.md) and code are welcome.
The repository is on GitHub as [marsh-sim/marsh-manager](https://github.com/marsh-sim/marsh-manager).
If you notice a problem, or want to request a new feature, you can [create a new issue](https://github.com/marsh-sim/marsh-manager/issues)
Code contributions are expected as [Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to that repository.
See the [developer documentation](./development.md) to get started.

## Licenses

The code for MARSH Manager is licensed under [GNU General Public License v3.0](https://github.com/marsh-sim/marsh-manager/blob/main/LICENSE.txt).

General application structure provided by [Qt Framework](https://www.qt.io/product) under terms of the [GNU Lesser General Public License (LGPL)](https://doc.qt.io/qt-6/lgpl.html).

Communication between components with [MAVLink](https://mavlink.io/en/) using generated code under [MIT License](https://github.com/mavlink/mavlink/blob/master/COPYING).
