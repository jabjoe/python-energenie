=========
Energenie
=========

Python module to control the `Energenie`_ add-on board for the `Raspberry Pi`_ used for remotely turning power sockets on and off.

This has been tweaked so it can be used outside a persistent Python instance.

This fork of the original uses sysfs instead which means after booting and setting the GPIOs up, it can be run as which ever user is given permissions to the sysfs GPIO files.

Example of setup, maybe in /etc/rc.local

echo 17 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio17/direction
chmod 766 /sys/class/gpio/gpio17/value

echo 27 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio27/direction
chmod 766 /sys/class/gpio/gpio27/value

echo 22 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio22/direction
chmod 766 /sys/class/gpio/gpio22/value

echo 23 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio23/direction
chmod 766 /sys/class/gpio/gpio23/value

echo 24 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio24/direction
chmod 766 /sys/class/gpio/gpio24/value

echo 25 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio25/direction
chmod 766 /sys/class/gpio/gpio25/value


Installation
============

On Raspberry Pi, install the energenie module in pip.

Python 3::

    sudo python3 setup.py install

Usage
=====

Example usage::

    from energenie import switch_on, switch_off, switches_init
    from time import sleep

    # ready switches if this is first run
    switches_init()

    # turn all plug sockets on and off
    switch_on()
    switch_off()

    # turn a plug socket on and off by number
    switch_on(1)
    switch_off(1)

    switch_on(3)
    switch_off(3)

    # turn some plug sockets on, then turn them off after 10 seconds
    switch_on(1)
    switch_on(4)
    sleep(10)
    switch_off(1)
    switch_off(4)

    # get states of which plugs on/off.
    plugs_state_array = get_plug_state()


Contributors
============

* `Ben Nuttall`_
* `Amy Mather`_
* `Gordon Hollingworth`_

Open Source
===========

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues


.. _GPIO Zero: http://gpiozero.readthedocs.io/
.. _Energenie support: http://gpiozero.readthedocs.io/en/stable/api_boards.html#energenie
.. _Energenie: https://energenie4u.co.uk/
.. _Raspberry Pi: http://www.raspberrypi.org/
.. _Ben Nuttall: https://github.com/bennuttall
.. _Amy Mather: https://github.com/minigirlgeek
.. _Gordon Hollingworth: https://github.com/ghollingworth
.. _BSD Licence: http://opensource.org/licenses/BSD-3-Clause
.. _GitHub Issues: https://github.com/bennuttall/energenie
.. _GitHub: https://github.com/bennuttall/energenie/issues
