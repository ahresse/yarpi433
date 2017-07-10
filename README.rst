yarpi433
========

Introduction
------------

Python script for sending 433MHz signals with generic low-cost GPIO RF modules on a Raspberry Pi.
I first sniffed remote controler signal with `gqrx`_ with my rtl-sdr USB key (820T2) tuned around 433MHz.
Once the acquisition were right, I retroengineered the protocol with `audacity`_ which happened to be a simple on-off keying modulated signal.
Lastly, I implemented this into a python script using my Raspberry Pi 1 GPIOs.

Supported hardware
------------------

Most generic 433MHz capable modules connected via GPIO to a Raspberry Pi.

.. figure:: https://cdn.instructables.com/ORIG/FU4/UJYA/HM8DG3Q3/FU4UJYAHM8DG3Q3.jpg
   :alt: 433module

Compatibility
-------------

This is compatible with my garage barrier.

.. figure:: http://image.made-in-china.com/2f0j00pMNTiuPlEsqJ/Automatic-Barrier-Gate-Parking-Barrier-System-PR-B3-4-.jpg
   :alt: automatic_barrier

Dependencies
------------

::

    RPi.GPIO

Installation
------------

On your Raspberry Pi, clone this depository.

Wiring diagram
--------------

Raspberry Pi 1/2(B+)::

                       RPI GPIO HEADER
                  ____________
                 |        ____|__
                 |       |    |  |
                 |     01|  . x  |02
                 |       |  . .  |
                 |       |  . .  |
                 |       |  . .  |
       TX        |   ____|__x .  |
     _______     |  |  __|__x .  |
    |       |    |  | |  |  . .  |
    |    GND|____|__| |  |  . .  |
    |       |    |    |  |  . .  |
    |    VCC|____|    |  |  . .  |
    |       |         |  |  . .  |
    |   DATA|_________|  |  . .  |
    |_______|            |  . .  |
                         |  . .  |
                         |  . .  |
                         |  . .  |
                         |  . .  |
                         |  . .  |
                         |  . .  |
                       39|  . .  |40
                         |_______|

    TX module:
       GND > PIN 09 (GND)
       VCC > PIN 02 (5V)
      DATA > PIN 11 (GPIO17)

Usage
-----

Once you entered the right code and configured the script, you can open the barrier by running:

::

    # python3 TX.py open_code

Open Source
-----------

* The code is licensed under the `GPLv3 Licence`_

.. _gqrx: https://github.com/csete/gqrx
.. _audacity: https://github.com/audacity/audacity
