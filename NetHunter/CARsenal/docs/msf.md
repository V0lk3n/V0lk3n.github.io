---
title: NetHunter CARsenal : MSF Automotive
description: Use Metasploit Framework Automotives modules.
icon:
weight:
author: ["v0lk3n",]
---

<img src="../assets/msf.gif" alt="CARsenal MSF Automotive">

### How to?

First you need to press on 'start msfconsole', it use screen to dettach and reattach msf session to be able to run the module in the same instance. 

Once msf is started, select your module and use "Info" to read module information, "Set" to configure module, and finally "Run" to execute it.

> Note : Actually, we can't automatically close the terminal window, so keep in mind that previous terminal window will still be opened but killed.

### Hardware Tools : ELM327 Relay 

- <a href="https://raw.githubusercontent.com/rapid7/metasploit-framework/refs/heads/master/tools/hardware/elm327_relay.rb" target="_blank">elm327_relay</a> : This module requires a connected ELM327 or STN1100 is connected to the machines serial. Sets up a basic RESTful web server to communicate

### Auxiliary Modules

- <a href="https://www.rapid7.com/db/modules/auxiliary/server/local_hwbridge/" target="_blank">local_hwbridge</a> : Sets up a web server to bridge communications between Metasploit and physically attached hardware.
- <a href="https://www.rapid7.com/db/modules/auxiliary/client/hwbridge/connect/" target="_blank">connect</a> : Connect the physical HWBridge which  
will start an interactive hwbridge session (local_hwbridge should be running).

### Post Modules
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/can_flood/" target="_blank">can_flood</a> : Floods a CAN interface with supplied frames.
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/canprobe/" target="_blank">canprobe</a> : Scans between two CAN IDs and writes data at each byte position.
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/diagnostic_state/" target="_blank">diagnostic_state</a> : Keep the vehicle in a diagnostic state on rounds by sending tester present packet.
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/ecu_hard_reset/" target="_blank">ecu_hard_reset</a> : Performs hard reset in the ECU Reset Service Identifier (0x11).
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/getvinfo/" target="_blank">getvinfo</a> : This module queries DTCs, some common engine info, and vehicle information.
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/identifymodules/" target="_blank">identifymodules</a> : Scan the CAN bus for any modules that can respond to UDS DSC queries.
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/malibu_overheat/" target="_blank">malibu_overheat</a> : Simple sample temp flood for the 2006 Malibu.
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/mazda_ic_mover/" target="_blank">mazda_ic_mover</a> : Moves the needle of the accelorometer and speedometer of the Mazda 2 instrument cluster.
- <a href="https://www.rapid7.com/db/modules/post/hardware/automotive/pdt/" target="_blank">pdt</a> : Acting in the role of a Pyrotechnical Device Deployment Tool (PDT)
