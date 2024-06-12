# MIT License

# Copyright (c) 2022 Haoran Sun

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
from dynamixel_controller import DynamixelController, XM430W210
import time

motor10 = XM430W210(10)
motor11 = XM430W210(11)
motor12 = XM430W210(12)
motor20 = XM430W210(20)
motor21 = XM430W210(21)
motor22 = XM430W210(22)
motor30 = XM430W210(30)
motor31 = XM430W210(31)
motor32 = XM430W210(32)
motor40 = XM430W210(40)
motor41 = XM430W210(41)
motor42 = XM430W210(42)
motor_list = [
    motor10, motor20, motor30, motor40,
    motor11, motor12,
    motor21, motor22,
    motor31, motor32,
    motor41, motor42
]

dynamixel_controller = DynamixelController("/dev/ttyUSB0", motor_list, baudrate=2000000, latency_time=1, reverse_direction=True)

dynamixel_controller.activate_controller()

# dynamixel_controller.torque_off()
max_reading_time = 0.0
max_test_time = 10.0 # in seconds
test_start_time = time.time()
while True: # time.time() - test_start_time < max_test_time:
    time_start = time.time()
    result_info = dynamixel_controller.read_info_with_unit(pwm_unit="percent", angle_unit="rad", current_unit="mA", retry=False, fast_read=True)
    print(result_info[1])
    # pos = dynamixel_controller.read_present_position()
    time_elasped = round((time.time() - time_start)*1000.0, 1)
    if time_elasped > max_reading_time:
        max_reading_time = time_elasped
    print(time_elasped, "; Max Read Time", max_reading_time)
    # print(dynamixel_controller.read_info())
    time.sleep(0.02)