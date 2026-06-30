from pydantic import BaseModel


class MotorMeasurementResponse(BaseModel):
    """..."""
    profile_id: int
    motor_speed: float
    stator_winding: float
