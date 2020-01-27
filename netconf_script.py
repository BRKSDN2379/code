#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""netconf script Console Script.

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

__author__ = "Christina Skoglund"
__email__ = "cskoglun@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


'''import modules to code'''
from ncclient import manager
import xmltodict
import xml.dom.minidom

'''XML encoded YANG data - YANG vlan data model and YANG interface data model'''
netconf_add_vlan_to_if = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <vlan>
            <vlan-list xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-vlan"><id>{vlan}</id><name>VLAN {vlan}</name></vlan-list>
        </vlan>
    </native>

    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <name>1/0/{number}</name>
                <switchport>
                    <access xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch">
                        <vlan><vlan>{vlan}</vlan></vlan>
                    </access>
                </switchport>
                <description> Configured by NETCONF </description>
            </GigabitEthernet>
        </interface>
    </native>
</config>"""

''' loop through 10 interfaces and assign vlans'''
for i in range(1,11):
    if i <= 3:
        vlan_id = 20
    else:
        vlan_id = 30
    ''' use ncclient to push down config'''
    netconf_data = netconf_add_vlan_to_if.format(number=i, vlan = vlan_id)
    with manager.connect(
        host="10.100.83.100",
        port="830",
        username="cisco",
        password="cisco",
        hostkey_verify=False
        ) as m:
        netconf_reply = m.edit_config(netconf_data, target = 'running')
    
    '''print status'''
    print("The configuration payload to be sent over NETCONF.\n")
    print(netconf_data)   
    print("Here is the raw XML data returned from the device.\n")
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    print("") 
    print(str(i) + " OK")