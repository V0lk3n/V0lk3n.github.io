---
title: NetHunter CARsenal : Simulator
description: Instrument Cluster Simulator for SocketCAN (ICSim) and Unified Diagnostic Services Simulator (UDSim)
icon:
weight:
author: ["v0lk3n",]
---

<p style="text-align: center"><img src="../assets/simulator.gif" width="350" alt="CARsenal Simulator"></p>

> Once simulator is running. You can make ICSim/UDSim floatable for a better control. You may also Enable/Disable Controls WebView.

### How it work?

While starting simulator we use display 3 to 5 to avoid issue if kex or something else is running.

- Display 3 : ICSim
- Display 4 : Controls
- Display 5 : UDSim

Then it start a virtual framebuffer (Xvfb) on each display, run fluxbox as window manager and start x11vnc as VNC Server.

Once done, it run the simulator in each VNC display and start noVNC to have access to it in the browser.

Finally, Nethunter App will load the webview of noVNC to provide display.


### ICSim

ICSim documentation can be <a href="https://github.com/zombieCraig/ICSim" target="_blank">found here</a>.

ICSim is started/stopped through <a href="https://raw.githubusercontent.com/V0lk3n/NetHunter-CARsenal/refs/heads/main/icsim_service.sh"> the following script</a>.

### UDSim

UDSim documentation can be <a href="https://github.com/zombieCraig/UDSim" target="_blank">found here</a>.

UDSim is started/stopped through <a href="https://raw.githubusercontent.com/V0lk3n/NetHunter-CARsenal/refs/heads/main/udsim_service.sh"> the following script</a>.
