# Project rationale

The following section is mostly excerpts from the presentations done in the design phase of the system:

- [Proposed options for the simulator architecture](rationale/Proposed%20options%20for%20simulator%20architecture.pdf)
- [Simulator architecture comparison](rationale/Simulator%20architecture%20comparison.pdf)
- [Standard selection for simulator integration](rationale/Standard%20selection%20for%20simulator%20integration.pdf)

## Objectives

Integrate available hardware and software resources to provide flight
simulation for the following projects:

- Rotorcraft-Pilot Coupling
- Manned-UnManned Teaming (MUM-T)
- G-Seat motion cueing
- Probable future research, not yet defined

The requirements expressed as [user stories](https://en.wikipedia.org/wiki/User_story)

### High level goals

- **As a** researcher **I can** add new flight models, measurement devices and cueing systems, **so that** the simulator is useful for my research.
- **As a** project leader **I can** use the simulator for commercial purposes without paying for any licenses, **so that** I can involve collaborators from industry environment.
- **As a** project leader **I can** use the simulator without relying on any external service **so that** I am sure the simulator will work in the future, regardless of an external company
- **As a** professor **I can** easily introduce students to the facility, **so that** they do practical projects.
- **As a** student **I can** use widespread solutions, standards and libraries, **so that** I get practical experience for my career after graduating.

### Conducting studies

- **As a** publication or thesis author **I can** easily gather all trial data into a single entity, **so that** they can be analyzed and presented in a written work.
- **As a** user conducting trials **I can** control the whole simulator on my own using a single application, **so that** there are less people to schedule for a trial with a test subject, and I can iterate on my own.
- **As a** human factors researcher **I can** see simulated view with an imperceptible delay, **so that** a human-in-the-loop piloting is viable.
- **As a** human factors researcher **I can** use the motion platform in closed loop mode, **so that** the simulation realism for the pilot is increased.

### Compatibility

- **As a** RPC project participant **I can** use Simulink and MBDyn models, **so that** I can reuse work already done in the project.
- **As a** human factors researcher **I can** connect the simulation infrastructure to other flight simulation software eg. FlightGear or X-Plane, **so that** off-the-shelf visual models of cockpit and aircraft can be used.
- **As a** user working on UAV support for HEMS missions (eg. MUM-T) **I can** communicate multiple aircraft (including unmanned) simultaneously, **so that** I can run shared simulations.
- **As a** user of UAVs **I can** connect PX4 simulation, **so that** I can collaborate with the drone lab and industrial partners.
- **As a** user of G-Seat **I can** connect the same simulator to moving platform and other cueing devices, **so that** a comparative study can be performed

### Developer experience

- **As a** simulator developer **I can** reuse common elements in different configurations, **so that** there is less work repeated to prepare the simulator for a new study.
- **As a** user adding a new device or flight model **I can** read a well-written and detailed documentation, **so that** the development process is feasible.
- **As a** simulator developer **I can** divide functionality into smaller components, **so that** parts of the program are easier to reason about.
- **As a** simulator user **I can** inspect information flowing inside the simulator, **so that** it is easy to troubleshoot the right part of the system.

## Standard selection

The most common feedback among reviewers was that using an estabilished solution is really important to not depend on the author to on-board every user. Also online search and chatbots will work much better.

![xkcd webcomic](https://imgs.xkcd.com/comics/standards.png)

*Fig: [xkcd "Standards" webcomic](https://xkcd.com/927/), under [CC-BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/) license*

A minimal comparison was made between the suggested libraries, see the [comm-library-comparison](https://github.com/marsh-sim/comm-library-comparison) repository:

- MQTT
- Data Distribution Service
- ZeroMQ
- MAVLink

The minimal prototype was implementing a trivial flight model using MATLAB Simulink and/or Python, and MAVLink proved to have by far the best support in the former.

## Similar solutions in academia

After the initial round of comparison and developent, some examples were found in the academic environment:

- [SIMONA](http://www.simona.tudelft.nl/) at TU Delft, comparison based only on public documentation:
    - Provides strong real-time guarantees
    - Has already been used for multiple simulators
    - More opinionated about the modules structure, should be written in C++
        - Partial support for Python; Simulink models through C++ code generation
    - Logs data to [HDF5](https://www.hdfgroup.org/solutions/hdf5/) which seems to be more widely used and more fit for the purpose format
- [Extended Reality Flight Simulation and Control Lab](https://umbertosaetti.com/#lab) at University of Maryland
    - Very similar objective of swapping between different models and cueing
    - *Anegdotally:* Moved over from UDP to a differend transport because of performance
