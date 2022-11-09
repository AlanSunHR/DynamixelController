# DynamixelController
Python controller interface with improved buck reading and writing for faster communication rate and lower latency.

## Source of communication bottleneck

1. High USB latency time.

There might be a default USB latency time limiting the communication frequency with USB devices (16 ms for example in Ubuntu 18.04).
On ubuntu, you can check the current latency time for your USB device (replace /dev/ttyUSB0 with your device name):

```bash

## Pre-requests




