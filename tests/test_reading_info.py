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

from dynamixel_controller import DynamixelController, XM430W210

motor10 = XM430W210(10)
motor11 = XM430W210(11)
motor12 = XM430W210(12)

motor40 = XM430W210(40)

dynamixel_controller = DynamixelController("/dev/ttyUSB0", [motor40])

dynamixel_controller.activate_controller()

# dynamixel_controller.torque_off()

while True:
    print(dynamixel_controller.read_info_with_unit(pwm_unit="percent", angle_unit="rad", current_unit="mA"))
    # print(dynamixel_controller.read_info())