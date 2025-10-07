// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot;

import edu.wpi.first.util.sendable.SendableRegistry;
import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.XboxController;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;

import com.revrobotics.spark.SparkLowLevel.MotorType;
import com.revrobotics.spark.config.SparkMaxConfig;
import com.revrobotics.spark.SparkMax;
import com.revrobotics.spark.config.SparkBaseConfig.IdleMode;
import com.revrobotics.spark.SparkBase.ResetMode;
import com.revrobotics.spark.SparkBase.PersistMode;


/**
 * The methods in this class are called automatically corresponding to each mode, as described in
 * the TimedRobot documentation. If you change the name of this class or the package after creating
 * this project, you must also update the manifest file in the resource directory.
 */
public class Robot extends TimedRobot {
  private final SparkMax m_leftLeader = new SparkMax(2, MotorType.kBrushless);
  private final SparkMax m_leftFollower = new SparkMax(3, MotorType.kBrushless);
  private final SparkMax m_rightLeader = new SparkMax(4, MotorType.kBrushless);
  private final SparkMax m_rightFollower = new SparkMax(5, MotorType.kBrushless);

  private final DifferentialDrive m_robotDrive =
      new DifferentialDrive(m_leftLeader::set, m_rightLeader::set);
  private final XboxController m_controller = new XboxController(0);

  /** Called once at the beginning of the robot program. */
  public Robot() {
    // For dashboards and LiveWindow
    SendableRegistry.addChild(m_robotDrive, m_leftLeader);
    SendableRegistry.addChild(m_robotDrive, m_leftFollower);
    SendableRegistry.addChild(m_robotDrive, m_rightLeader);
    SendableRegistry.addChild(m_robotDrive, m_rightFollower);

    // This is the 2025 REV config structure
    SparkMaxConfig leftLeaderConfig = new SparkMaxConfig();
    leftLeaderConfig
        .idleMode(IdleMode.kBrake);
    m_leftLeader.configure(leftLeaderConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);

    SparkMaxConfig leftFollowerConfig = new SparkMaxConfig();
    leftFollowerConfig
        .idleMode(IdleMode.kBrake)
        .follow(m_leftLeader);
    m_leftFollower.configure(leftFollowerConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);

    SparkMaxConfig rightLeaderConfig = new SparkMaxConfig();
    rightLeaderConfig
        .inverted(true)
        .idleMode(IdleMode.kBrake);
    m_rightLeader.configure(rightLeaderConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);

    SparkMaxConfig rightFollowerConfig = new SparkMaxConfig();
    rightFollowerConfig
        .inverted(true)
        .idleMode(IdleMode.kBrake)
        .follow(m_rightLeader);
    m_rightFollower.configure(rightFollowerConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);
  }

  /** This function is run once each time the robot enters autonomous mode. */
  @Override
  public void autonomousInit() {}

  /** This function is called periodically during autonomous. */
  @Override
  public void autonomousPeriodic() {}

  /** This function is called once each time the robot enters teleoperated mode. */
  @Override
  public void teleopInit() {}

  /** This function is called periodically during teleoperated mode. */
  @Override
  public void teleopPeriodic() {

    // 1. Read button / joystick
    double left_y = m_controller.getLeftY();
    double right_x = m_controller.getRightX();

    // 2. Calculate
    double speed = left_y;
    double rotation = -right_x;

    // 3. Turn motors
    m_robotDrive.arcadeDrive(speed, rotation);
  }

  /** This function is called once each time the robot enters test mode. */
  @Override
  public void testInit() {}

  /** This function is called periodically during test mode. */
  @Override
  public void testPeriodic() {}
}
