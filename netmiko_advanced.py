#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""netmiko_code Console Script.

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

import sys
import click
from netmiko import ConnectHandler
import random
import pandas as pd
import re

__author__ = "Christina Skoglund"
__email__ = "cskoglun@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"




@click.command()
@click.option('--vlan','-vlan')



def main(vlan):
    """netmiko_code Console Script."""

    devices = {
        "device_type": "cisco_xe",
        "ip": "10.100.83.100",
        "username": "cisco",
        "password": "cisco"
    }

    def never_used_if():
        """ use netmiko to get last input status of all interfaces """
        net_connect = ConnectHandler(**devices)
        output = net_connect.send_command("Sh int | inc Gig|Last input")

        """ divide string in lines """
        output_ = output.split("GigabitEthernet")

        """ define function to extract word after string """
        def after(value, a):
            # Find and validate first part.
            pos_a = value.rfind(a)
            if pos_a == -1:
                return ""
            # Returns chars after the found string.
            adjusted_pos_a = pos_a + len(a)
            if adjusted_pos_a >= len(value):
                return ""
            return value[adjusted_pos_a:]


        """ loop over the lines to extract info """
        dict_upper = {}
        for line in output_:
            line = line.replace("\n", "")
            dict_lower = {}
            dict_lower["Status"] = (
                after(line, f"{line.split(' ')[0]} is ").split(" ")[0].replace(",", "")
            )
            dict_lower["Line protocol"] = (
                after(line, "line protocol is ").split(" ")[0].replace(",", "")
            )
            dict_lower["Last input"] = after(line, "Last input ").split(" ")[0].replace(",", "")
            dict_lower["Last output"] = (
                after(line, f"Last input {dict_lower['Last input']}, output ")
                .split(" ")[0]
                .replace(",", "")
            )
            dict_lower["Output hang"] = (
                after(line, "output hang ").split(" ")[0].replace(",", "")
            )
            dict_upper[f"GigabitEthernet{line.split(' ')[0]}"] = dict_lower


        """ find the gigabitinterfaces that never been used """
        never_used_interfaces = []
        for i in dict_upper.keys():
            if dict_upper[i]["Last input"] == "never":
                never_used_interfaces.append(i)
            
        return never_used_interfaces



    """ choose and configure interface """
    never_used_interface_list = never_used_if()
    interface = random.choice(never_used_interface_list)

    config = [
        "vlan {}".format(vlan),
        "int {}".format(interface),
        "switchport mode access",
        "switchport access vlan {}".format(vlan),
        "description CONF BY NETMIKO",
    ]

    """ use netmiko to push down configuration to switch"""
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(config)

    print("\n\n*** Configured interface ***\n\n{}".format(interface))

    """ store data in pandas """
    store_data = pd.DataFrame("nan", columns=["IP", "Interface", "vlan"], index=[])
    store_data.at[1, "IP"] = devices["ip"]
    store_data.at[1, "Interface"] = interface
    store_data.at[1, "vlan"] = vlan
    store_data.to_excel("devices.xlsx", index=False)

    print("\n\n*** Data stored in excel document\n\n")
    print("Hello you chose vlan {}".format(vlan))
    return 0


if __name__ == "__main__":
    sys.exit(main())
