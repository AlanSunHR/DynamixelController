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

motor40 = XM430W210(40)

dynamixel_controller = DynamixelController("/dev/ttyUSB1", [motor40])

dynamixel_controller.activate_controller()

dynamixel_controller.torque_off()

# dynamixel_controller.set_operating_mode_all("position_control")
dynamixel_controller.set_operating_mode_all("current_based_position_control")

dynamixel_controller.torque_on()

dynamixel_controller.set_profile_velocity_rad([1])
dynamixel_controller.set_goal_position_rad([-1.57])

while True:
    print(dynamixel_controller.read_info())