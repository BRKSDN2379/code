# LET'S MAKE MONDAY (or rather any day) EXCITING!

In this repository we are sharing all code that has been presented during the breakout session BRKSDN-2379 at Cisco Live Europe 2020 in Barcelona. The main goal with these scripts is to introduce Network Engineers to the power and possibilities of programmability by providing some simple examples. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

1. Python installed in your development environment. 
2. An active virtual environment where you have installed the required modules and libraries.
3. Clone this repository to the environment in which you are working
4. An IOS XE device for testing against

Follow this lab to create your developer environment: <https://developer.cisco.com/learning/modules/dev-setup/dev-win/step/1>

Setup virtual environment: <https://developer.cisco.com/learning/devnet-express/dnav3-track/dnav3-verify/dnav3-verify/step/4>

### Installing

When you have your developer environment up and running, make sure you install all libraries and modules required for your scripts. Make sure you have your virtualenvironment activated before installing them. 

Clone this repository to the environment in which your are working: 
````
root$ git clone https://github.com/BRKSDN2379/code.git
````

Activate virtual environment if you are running the script on a Mac/Linux machine: 

```
(venv) root:code$ source venv/bin/activate
```

Activate virtual environment if you are running the script on a Windows machine with Windows git-bash: 

```
(venv) root:code$  source venv/Scripts/activate 
```

Install the required libraries to be able to run the scripts: 

```
(venv) root:code$ pip install -r requirements.txt
```
## Running the codes


### Netmiko simple code: netmiko_simple.py [Referred to as Step 4 in slides]
Mission of the script: Use Netmiko to create vlan 20 and vlan 30 and configure 10 interfaces on a switch.

Add device information directly in the `netmiko_simple.py` script and change all **'CHANGE ME'** values. 

```
device = {
    'device_type':'cisco_xe',
    'ip':'CHANGE ME',
    'username':'CHANGE ME',
    'password':'CHANGE ME',
}
```


Execute the simple Netmiko code example `netmiko_simple.py`
```
(venv) root:code$ python netmiko_simple.py
```
Output should be: 

````
(venv) root:code$ python main_netmiko.py 


 *** Configuring vlan 20 for interface g1/0/1 - 3 and vlan 30 for interface g1/0/4 - 10 *** 




 *** Netmiko Python Script Execution completed *** 
````
### Netmiko advanced code: netmiko_advanced.py
Mission of the script: Use Netmiko to request data from the device, parse it and identify all inactive access ports. Then randomly pick one of the inactive ports and configure it with a vlan you choose and also configure the chosen port as an access port. 

Add device information directly in the `netmiko_simple.py` script and change all **'CHANGE ME'** values. 

```
    devices = {
        "device_type": "cisco_xe",
        "ip": "CHANGE ME",
        "username": "CHANGE ME",
        "password": "CHANGE ME"
    }
```

Execute the simple Netmiko code example `netmiko_advanced.py`. Make sure to add the vlan you want to configure as an argument, see example below where I add vlan 20 when executing the script. 

```
(venv) root:code$ python netmiko_advanced.py -vlan 20
```
Output should be:
```
(venv) root:code$ python netmiko_advanced.py -vlan 20


*** Configured interface ***

GigabitEthernet1/0/37


*** Data stored in excel document


Hello you chose vlan 20
```

### NETCONF script: netconf_script.py [Referred to as Step 5 in slides]
Mission of the script: Use NETFCONF and YANG models to create vlan 20 and vlan 30 and configure 10 interfaces on a IOS XE switch.

Add device information directly in the `netconf_script.py` script and change all **'CHANGE ME'** values. 

````
DEVICE_TYPE = "cisco_xe"
USERNAME = "CHANGE ME"
PASSWORD = "CHANGE ME"
IP_ADDRESS = "CHANGE ME"

````

Execute the simple NETCONF code example `netconf_script.py`. 

````
(venv) root:code$ python netconf_script.py
````

Part of the output should be:

````
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <name>1/0/10</name>
                <switchport>
                    <access xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch">
                        <vlan><vlan>30</vlan></vlan>
                    </access>
                </switchport>
                <description> Configured by NETCONF </description>
            </GigabitEthernet>
        </interface>
    </native>
</config>
Here is the raw XML data returned from the device.

<?xml version="1.0" ?>
<rpc-reply message-id="urn:uuid:e8d412b7-92d3-4f7d-a3d5-33f54a99d6cf" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <ok/>
</rpc-reply>


10 OK
````
### ZTP script: ztp.py [Referred to as Step 10 in slides]
This script `ztp.py` is intended to be downloaded to and executed in the IOS XE Guestshell during the zero-touch booting process. You need to add it to an HTTP or TFTP server. In this example, we are utilising HTTP server.

Configure DHCP option 67 on the DHCP server (in this example in the router) to point the IOS XE device to your script's HTTP server location. See example below:

````
Router> enable
Router# configure terminal
Router(config)# ip dhcp pool pnp_device_pool
Router(config-dhcp)# network 10.1.0.0 255.255.255.0
Router(config-dhcp)# default-router 10.1.0.1
Router(config-dhcp)# option 67 ascii http://10.1.0.2:8000/ztp.py 
Router(config-dhcp)# end

````
After this, you should be all set to boot your **IOS XE device**! 

## Authors & Maintainers

People responsible for the creation and maintenance of this project:

- Christina Skoglund <cskoglun@cisco.com>
- Juulia Santala <jusantal@cisco.com>

## Credits

Credits to be given to Jeremy Cohoe <https://github.com/jeremycohoe>, who has provided the original ZTP script. 

**Credits to be given to Pedro Oliveira for awesome README.md skills.**

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
