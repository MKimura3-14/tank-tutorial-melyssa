# import library for robot programming
import wpilib
import wpilib.drive
from commands2 import CommandScheduler
import rev

from robot_container import RobotContainer

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Define what gamepad I'm using
        self.pad = wpilib.XboxController(0)
        self.robot_container = RobotContainer()

    def teleopInit(self):
        self.robot_container.configure_buttons()

    def robotPeriodic(self):
        CommandScheduler.getInstance().run()

if __name__ == "__main__":
    wpilib.run(MyRobot)