# tempcloud
gathering temperature and humidity logger data

# caution
Currently the programs written in Python2.
We have a plan to migrate them into Python3 in the near future.

We've checked the execution on the Raspberry Pi 2.
You may run on the Raspbarri Pi 3b but not on the Raspberry Pi 4.

# Required
FDDI base USB trasnmitter (like TOCOS USB).
TOCOS chip with sh11 or sh31 curcuits required to detect temperature and humidity.

# transmission
Transmission executes with a hexadecimal every minute.
Their format manuals ARE TBD. (see source codes for detail).
