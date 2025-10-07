import commands2.subsystem
import rev
import wpilib
from wpimath.controller import PIDController, ProfiledPIDController
import math
from wpimath.trajectory import TrapezoidProfile


class DriveSubsystem(commands2.Subsystem):
    def __init__(self):
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

        # Encoder distance
        self.encoder_left_1 = self.motor_left_1.getEncoder()
        self.encoder_left_2 = self.motor_left_2.getEncoder()
        self.encoder_right_1 = self.motor_right_1.getEncoder()
        self.encoder_right_2 = self.motor_right_2.getEncoder()

        # Controller
        #self.controller = PIDController(0.02, 0.01, 0.009)
        self.speed_profile = TrapezoidProfile.Constraints(30, 20)
        self.controller = ProfiledPIDController(0.5, 0.01, 0.01, self.speed_profile)

        self.diameter = 6   # inches
        self.target = 0

        self.gear_ratio = 8.46
    
    def default(self):
        pass
    
    def arcadeDrive(self, speed, rotation):
        self.drivetrain.arcadeDrive(speed, rotation)
    
    def tankDrive(self, left_speed, right_speed):
        self.drivetrain.tankDrive(left_speed, right_speed)
    
    def getLeftEncoder(self):
        return self.encoder_left_1.getPosition()

    def getDistance(self):
        # This returns rotations
        left_rot = (self.encoder_left_1.getPosition())/self.gear_ratio
        right_rot = (self.encoder_right_1.getPosition())/self.gear_ratio
        rot = (left_rot+right_rot)/2
        # Convert to distance feet
        distance = rot * math.pi * self.diameter
        return distance

    def setDistance(self, value: float):
        self.target = value

    def periodic(self):
        current = self.getDistance()
        speed = self.controller.calculate(current, self.target)
        print(f"{current:.4f}, {self.target:.4f}, {speed:.4f}")
        self.tankDrive(speed, speed)