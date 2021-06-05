''' 
testing code for cfBolt drone 
'''

from pycrazyswarm import Crazyswarm
import numpy as np

TAKEOFF_DURATION = 5.5
TIME_DURATION = 5.0

HEIGHT = 0.5
sleepRate = 30


def goCircle(timeHelper, cf, radius, round_num, omega):
    phi = 2*np.pi
    startTime = timeHelper.time()
    t = 0
    pos = cf.position()
    startPos = cf.initialPosition + np.array([0, 0, HEIGHT])
    center_circle = startPos - np.array([radius, 0, 0])
    while omega*t < 2*np.pi*round_num:
        t = timeHelper.time() - startTime

        cmd_x = radius * np.cos(omega * t + phi)
        cmd_y = radius * np.sin(omega * t + phi)
        cmd_z = HEIGHT 

        pos = [cmd_x, cmd_y, cmd_z]
        print("The cmd is: ")
        print("{0}, {1}, {2}".format(cmd_x, cmd_y, cmd_z))

        cf.goTo(pos, 0, 0.1)
        timeHelper.sleepForRate(sleepRate)

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]
    print("press button to start logging data ...")
    swarm.input.waitUntilButtonPressed()

    cf.setParam("usd/logging", 1)   # set "usd.logging" to 1 to start log
    print("press button to take off ...")
    swarm.input.waitUntilButtonPressed()

    cf.takeoff(targetHeight=HEIGHT, duration=5.5)
    swarm.input.waitUntilButtonPressed()
    print("press button to start the circle ...")
    swarm.input.waitUntilButtonPressed()

    # goCircle(timeHelper, cf, radius=1.5, round_num=6.0, omega=0.4)

    print("press button to land ...")
    swarm.input.waitUntilButtonPressed()

    print("landing ...")
    cf.land(targetHeight=0.1, duration=5.5)   # for cf Bolt targetHeight = 0.1
    timeHelper.sleep(TIME_DURATION)

    print("press button to stop logging data ...")
    swarm.input.waitUntilButtonPressed()
    cf.setParam("usd/logging", 0)  # set "usd.logging" to 0 to stop logging


if __name__ == "__main__":
    main()