"""
Contains the core data models (entities). Should not know anything about CSV,
databases, or how data is loaded.
MotorMeasurement — represents one row of motor sensor data.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class MotorMeasurement:
    """Domain entity representing one row of motor sensor data."""
    profile_id: int
    motor_speed: float
    torque: float
    pm: float                    # Permanent magnet temperature
    stator_winding: float
    coolant: float = 0.0         # Optional for now
    ambient: float = 0.0