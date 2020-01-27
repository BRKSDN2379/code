#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ztp_script Console Script.

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

__author__ = "Juulia Santala"
__email__ = "jusantal@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


# Import cli python module. This will let you use the cli commands
# from python.
import cli

#cli.configurep pushes commands to the switch!
cli.configurep(["int vlan 42", "ip address 10.2.0.13 255.255.255.0", "no shut", "end"])
cli.configurep(["ip default-gateway 10.2.0.1", "end"])
cli.configurep(["username admin privilege 15 secret 0 admin"])
cli.configurep(["aaa new-model", "aaa authentication login default local", "end"])
cli.configurep(["aaa authorization exec default local", "aaa session-id common", "end"])

# Save a show command, and use cli.executep to execute it and
# print it on screen.
cli_command = "sh ip int brief"
cli.executep(cli_command)

#Finally, we print a text on screen to show the execution is complete.
print("\n\n *** ZTP Day0 Python Script Execution Complete *** \n\n")
