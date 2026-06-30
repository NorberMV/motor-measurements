"""
Contains the core data models (entities). Should not know anything about CSV,
databases, or how data is loaded.
MotorMeasurement — represents one row of motor sensor data.
"""
# from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict


# @dataclass(frozen=True)
# class MotorMeasurement:
#     """Domain entity representing one row of motor sensor data."""
#     profile_id: int
#     motor_speed: float
#     torque: float
#     pm: float                    # Permanent magnet temperature
#     stator_winding: float
#     coolant: float = 0.0         # Optional for now
#     ambient: float = 0.0


class MotorMeasurement(BaseModel):
    """Domain entity representing one row of motor sensor data."""

    model_config = ConfigDict(frozen=True) # Makes it immutable

    profile_id: int
    motor_speed: float
    torque: float
    pm: float                    # Permanent magnet temperature
    stator_winding: float
    coolant: float = 0.0         # Optional for now
    ambient: float = 0.0


class MotorMeasurementResponse(BaseModel):
    """..."""
    profile_id: int
    motor_speed: float
    stator_winding: float
