# Web Controled BedsideLamps

This is a project I've been working on that controls my two bedside lamps with led's I've hacked onto them using a Raspberry Pi underneath my bed.

The project is currently using GPIO pin's 17 and 22 but it's easy enough to edit them to your liking.


[Here](http://imgur.com/a/gEdbC) is a album of the project.

## Dependencies

You're going to need [pi-blaster by sarfata](https://github.com/sarfata/pi-blaster).


## Installation

All you need to do is run the [bedsidelamp.py](https://github.com/daned33/bedsidelamp/blob/master/bedsidelamp.py) file.

## How to use

All you need to do is make GET requests to your Raspberry Pi to the port (default:8080) with the attributes of brightness and fade.

The brightness attribute is a percentage value. For example:

* brightness=50 would be 50% brightness.
* brightness=82 would be 82% brightness.
* and so on.

And the fade attribute is the amount of seconds it will take to go from one brightness to another. For example:

* fade=30 would take 30 seconds to get from the current brightness to the new set brightness.
* fade=60 would take one minute.
* fade=300 would take 5 minutes.
* fade=600 would take 10.
* and so on.

*ps. If the fade attribute is missing from the GET request. It defaults to 10 seconds.

## Examples

Here are a few examples.

* `IP:8080/?brightness=70&fade=60`
  * With an initial brightness of 0. This would take one minute to go from 0% to 70% brightness.
  
* `IP:8080/?brightness=5&fade=120`
  * With an initial brightness of 100. This would take two minutes to go from 100% to 5% brightness.
  
* `IP:8080/?brightness=0`
  * With an initial brightness of 75. This would take 10 seconds to go from 0% to 70% brightness.
  * Note! The fade attribute is missing and the program defaults to 10 second fade time.
  
## Extras

I've also created a little driver board that sit's on top of the Raspberry Pi too! I'll probaby upload the schematic at some point when I get a chance.

![bedsidelights](http://i.imgur.com/To0EodLl.jpg)
