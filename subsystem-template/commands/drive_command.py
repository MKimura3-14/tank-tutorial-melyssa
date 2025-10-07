from commands2 import Command
from subsystems.drive_subsystem import DriveSubsystem

class RunDrive(Command):
    def __init__(self, subsystem: DriveSubsystem, value: float):
        super().__init__()

        self.subsystem = subsystem
        self.value = value

        self.addRequirements(self.subsystem)

    def execute(self):
        self.subsystem.setDistance(self.value)