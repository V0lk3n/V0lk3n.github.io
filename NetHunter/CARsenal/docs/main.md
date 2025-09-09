---
title: NetHunter CARsenal : Main
description: Configure your CAN interfaces and decode your VIN identification number.
icon:
weight:
author: ["v0lk3n",]
---

## Main

Configure your CAN interfaces and decode your VIN identification number.

<p style="text-align: center"><img src="../assets/main.gif" width="350" alt="CARsenal Main"></p>

### Main : CAN Interfaces

***Start CAN Interface - Settings Prerequisite :***

Set "CAN Interface", "CAN Type" in Inteface. And optionally enable 'MTU' and 'txqueulen to set custom value'.

```bash
# For VCAN Type : create interface first
sudo ip link add dev <caniface> type vcan

# If MTU or txqueuelen value specified
sudo ip link set <caniface> mtu <Value>
sudo ip link set <caniface> txqueuelen <Value>

# Brought UP interface
sudo ip link set <caniface> up
```

***Reset Interface - Used command :***

It execute the <a href="https://raw.githubusercontent.com/V0lk3n/NetHunter-CarArsenal/refs/heads/main/can_reset.sh" target="_blank">following script</a> to reset interfaces.


### Main : Services

<p style="text-align: center"><img src="../assets/main-services.gif" width="350" alt="CARsenal Main Services"></p>

> You can customize services commands, by long pressing oranges buttons.

Interface section is used to Configure your CAN interfaces. You may specify interface name in Settings, and optionally set a custom MTU and txqueuelen value.

You also may enable some Daemon/services which are :

- slcand : Daemon for Serial CAN devices.
- hlcand : Fork of slcand made for ELM327 microcontroller.
- socketcand : Daemon to bridge CAN interfaces.
- slcan_attach : Attach your serial CAN device.
- ldattach : Attach your device.
- RFCOMM
    - bind : Bind bluetooth to your device.
    - connect : Connect the RFCOMM device to the remote Bluetooth device


### VIN Info

VIN Info is used to decode VIN identifier and check checksum.

```bash
vininfo show <vinNumber>
vininfo check <vinNumber>
```
