---
title: NetHunter CARsenal : Tools
description: Unleash the power of can-utils suite, diagnose your car using Freediag and transfer CAN frames between two machines using Cannelloni.
icon:
weight:
author: ["v0lk3n",]
---

<img src="../assets/tools.gif" width="350" alt="CARsenal Tools">

> Commands are updated when configuring settings. You can long press on orange buttons to edit commands as well.

### Tools : Provided tools

- <a href="https://github.com/linux-can/can-utils" target="_blank">can-utils</a> : SocketCAN userspace utilities and tools.
    - <a href="https://manpages.debian.org/trixie/can-utils/cangen.1.en.html" target="_blank">cangen</a> : CAN frames generator for testing purposes.
    - <a href="https://manpages.debian.org/trixie/can-utils/cansniffer.1.en.html" target="_blank">cansniffer</a> : Volatile CAN content visualizer.
    - <a href="https://manpages.debian.org/trixie/can-utils/candump.1.en.html" target="_blank">candump</a> : Dump CAN bus traffic.
    - <a href="https://manpages.debian.org/trixie/can-utils/cansend.1.en.html" target="_blank">cansend</a> : Send CAN-frames via CAN_RAW sockets.
    - <a href="https://manpages.debian.org/trixie/can-utils/canplayer.1.en.html" target="_blank">canplayer</a> : Replay a compact CAN frame logfile to CAN devices.
    - <a href="https://manpages.debian.org/trixie/can-utils/asc2log.1.en.html" target="_blank">asc2log</a> : Convert ASC logfile to compact CAN frame logfile.
    - <a href="https://manpages.debian.org/trixie/can-utils/log2asc.1.en.html" target="_blank">log2asc</a> : Convert compact CAN frame logfile to ASC logfile.

- <a href="https://github.com/fenugrec/freediag" target="_blank">freediag</a> : Access your car diagnostic system.
    - <a href="https://github.com/fenugrec/freediag" target="_blank">diagtest</a> : Standalone program from Freediag, used to exercise code paths.

- <a href="https://github.com/mguentner/cannelloni" target="_blank">cannelloni</a> : Uses UDP, TCP or SCTP to transfer CAN frames between two machines.

- <a href="https://raw.githubusercontent.com/V0lk3n/NetHunter-CarArsenal/refs/heads/main/sequence_finder.sh">sequence_finder</a> : Custom script that split a log files, replay theses with CanPlayer until finding the exact sequence of the desired action. Finally it replay it using CanSend.

