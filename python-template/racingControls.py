# import library for robot programming
import wpilib
import wpilib.drive
import rev

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Define what gamepad I'm using
        self.pad = wpilib.XboxController(0)

        # Define drive motors 
        self.motor_left_1 = rev.SparkMax(2, rev.SparkMax.MotorType.kBrushless)
        self.motor_left_2 = rev.SparkMax(3, rev.SparkMax.MotorType.kBrushless)
        self.motor_right_1 = rev.SparkMax(4, rev.SparkMax.MotorType.kBrushless)
        self.motor_right_2 = rev.SparkMax(5, rev.SparkMax.MotorType.kBrushless)

        # Set the right side to be inverted
        self.motor_right_1.setInverted(True)  # Set right 1 inverted
        self.motor_right_2.setInverted(True)  # Set right 2 inverted

        # Combine motors into groups
        self.left_group = wpilib.MotorControllerGroup(self.motor_left_1, self.motor_left_2)
        self.right_group = wpilib.MotorControllerGroup(self.motor_right_1, self.motor_right_2)

        # Define drivetrain
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left_group, self.right_group)
        self.mode = 0

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # This function gets called over and over again during teleoperated mode

        # 1. Read button / joystick
        leftX = self.pad.getLeftX()
        leftY = self.pad.getLeftY()
        rightX = self.pad.getRightX()
        rightTrigger = self.pad.getRightTriggerAxis()
        leftTrigger = self.pad.getLeftTriggerAxis()
        aButton = self.pad.getAButton()
        bButton = self.pad.getBButton()
        xButton = self.pad.getXButton()
        if aButton:
            self.mode = 0
        elif bButton:
            self.mode = 1
        elif xButton:
            self.mode = 2
        if self.mode == 0:
            speed = -(rightTrigger - leftTrigger)/3
            rotation = -(leftX)/3
        elif self.mode == 1:
            speed = leftY/3
            rotation = -(rightX)/3
        elif self.mode == 2:
            speed = leftY/3
            rotation = -(leftX)/3
        
        # 3. Turn motors
        self.drivetrain.arcadeDrive(speed, rotation)


if __name__ == "__main__":
    wpilib.run(MyRobot)