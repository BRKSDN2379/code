#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main Netmiko Console Script.

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


__author__ = "Christina Skoglund"
__email__ = "cskoglun@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


"""THIS IS WHERE THE SCRIPT STARTS"""
''' import network module '''
from netmiko import ConnectHandler

''' device information - UPDATE THIS INFORMATION'''
device = {
    'device_type':'cisco_xe',
    'ip':'10.100.83.100',
    'username':'cisco',
    'password':'cisco',
}

''' Standard CLI commands as items in list'''
vlan20 = ["vlan 20", "int range g1/0/1 - 3", "description THIS PORT IS VLAN 20", "switchport mode access", "switchport access vlan 20"]
vlan30 = ["vlan 30", "int range g1/0/4 - 10", "description THIS PORT IS VLAN 30", "switchport mode access", "switchport access vlan 30"]
''' add all commands into one list '''
vlans = vlan20 + vlan30

''' print function '''
print("\n\n *** Configuring vlan 20 for interface g1/0/1 - 3 and vlan 30 for interface g1/0/4 - 10 *** \n\n")

''' netmiko establishses connection and executes configuration '''
connect = ConnectHandler(**device)
output = connect.send_config_set(vlans)

print("\n\n *** Netmiko Python Script Execution completed *** \n\n")
