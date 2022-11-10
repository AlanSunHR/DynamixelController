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

import os
import sys

test_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(test_dir)
package_dir = os.path.join(root_dir, "src", "DynamixelController")

sys.path.append(package_dir)

from dynamixel_controller import DynamixelController
from dynamixel_models import XM430W210

motor10 = XM430W210(10)
motor11 = XM430W210(11)
motor12 = XM430W210(12)

dynamixel_controller = DynamixelController("/dev/ttyUSB1", [motor10, motor11, motor12])

dynamixel_controller.activate_controller()

dynamixel_controller.torque_off()

dynamixel_controller.set_velocity_i_gain([10,20,30])
dynamixel_controller.set_velocity_p_gain([11,22,31])
dynamixel_controller.set_position_d_gain([40,50,60])
dynamixel_controller.set_position_i_gain([41,51,61])
dynamixel_controller.set_position_p_gain([42,52,62])

dynamixel_controller.set_feedforward_2nd_gain([100, 200, 300])
dynamixel_controller.set_feedforward_1st_gain([110, 120, 130])

dynamixel_controller.set_goal_pwm([1,2,3])
dynamixel_controller.set_goal_current_mA([5,6,7])
dynamixel_controller.set_goal_position_rad([0,0,0])
dynamixel_controller.set_goal_velocity([21,22,23])
dynamixel_controller.set_profile_acceleration([70,71,72])
dynamixel_controller.set_profile_velocity_rad([1,1,1])
