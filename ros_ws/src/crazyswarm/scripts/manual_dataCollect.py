''' 
Testing code for cfBolt data collection.
Manually move the CF Bolt to collect data
'''
from pycrazyswarm import Crazyswarm

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]
    print("press button to start logging data ...")
    swarm.input.waitUntilButtonPressed()

    cf.setParam("usd/logging", 1)   # set "usd.logging" to 1 to start logging


    print("press button to stop logging data ...")
    swarm.input.waitUntilButtonPressed()

    cf.setParam("usd/logging", 0)  # set "usd.logging" to 0 to stop logging


if __name__ == "__main__":
    main()