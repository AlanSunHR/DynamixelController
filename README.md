# DynamixelController
Python controller interface with improved buck reading and writing for faster communication rate and lower latency.

## Source of communication bottleneck

1. High USB latency time.

    There might be a default USB latency time limiting the communication frequency with USB devices (16 ms for example in Ubuntu 18.04).
    For more information please refere to https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/#usb-latency-setting.

    To change the latency time on ubuntu (replace "ttyUSB0" with your device name):

    ```bash
    cat /sys/bus/usb-serial/devices/ttyUSB0/latency_timer 
    ```

    To manaully change the latency time on ubuntu:
    ```bash
    echo 1 | sudo tee /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
    ```

    NOTE: You have to set the latency time every time you plug you USB device.

1. Low baudrate of Dynamixel bus.

    Change the baudrate of dynamixel actuators to a higher value (4M or higher)

## Pre-requests

1. The package is tested and targeted to run only on ubuntu. (tested on Ubuntu 18.04)
1. Download dynamixel_sdk source code:
    ```bash
    git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
    ```
1. Navigate to DynamixelSDK/python/src.
1. Open the file "port_handler.py". In line 27, change the variable LATENCY_TIMER to the USB latency time you set.
    ```python
    LATENCY_TIMER = 16 # Change the value to the USB latency time
    ```
    Note: This only changes the timeout of the port_handler. If not properly set, the default timeout will be longer and may cause problems with a high communication frequency.

1. Navigate to DynamixelSDK/python. Install the modified package by running:
    ```bash
    python3 setup.py install
    ```

## Install the package
pip install -i https://test.pypi.org/simple/ dynamixel-controller==0.0.12




