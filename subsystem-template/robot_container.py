import wpilib
from commands2.button import CommandXboxController
from commands.drive_command import RunDrive
from subsystems.drive_subsystem import DriveSubsystem

class RobotContainer:
    def __init__(self):
        self.drive_controller = CommandXboxController(0)
        self.drive_subsystem = DriveSubsystem()

    def configure_buttons(self):
        self.drive_controller.a().onTrue(RunDrive(self.drive_subsystem, 6))
        self.drive_controller.b().onTrue(RunDrive(self.drive_subsystem, -6))
        self.drive_controller.x().onTrue(RunDrive(self.drive_subsystem, 0))