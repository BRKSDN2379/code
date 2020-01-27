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
(venv)root:code$ source venv/bin/activate
```

Activate virtual environment if you are running the script on a Windows machine with Windows git-bash: 

```
(venv)root:code$  source venv/Scripts/activate 
```

Install the required libraries to be able to run the scripts: 

```
(venv)root:code$ pip install -r requiements.txt
```
## Running the codes


### Netmiko simple code

Add device information directly in the netmiko_simple.py script and change all 'CHANGE ME' values. 

```
device = {
    'device_type':'cisco_xe',
    'ip':'CHANGE ME',
    'username':'CHANGE ME',
    'password':'CHANGE ME',
}
```


Execute the simple Netmiko code example netmiko_simple.py
```
(venv)root:code$ python netmiko_simple.py
```
Output should be: 

````
(venv) root:code$ python main_netmiko.py 


 *** Configuring vlan 20 for interface g1/0/1 - 3 and vlan 30 for interface g1/0/4 - 10 *** 




 *** Netmiko Python Script Execution completed *** 
````

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds


## Authors & Maintainers

Smart people responsible for the creation and maintenance of this project:

- Christina Skoglund <cskoglun@cisco.com>
- Juulia Santala <jusantal@cisco.com>

## Credits

Credits to be given to Jeremy Cohoe <https://github.com/jeremycohoe>, who has provided the original ZTP script. 

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
