"""
A Port defines what your application needs, without saying how it gets it.
DataReaderPort -- says 'I need something that can give me motor measurements one by one.'
"""
from abc import ABC, abstractmethod
from typing import Iterator

from motor_temperature_analyzer.domain.entities.motor_measurements import MotorMeasurement


class DataReaderPort(ABC):
    @abstractmethod
    def read_measurements(self) -> Iterator[MotorMeasurement]:
        """Yield measurements one by one (lazy loading with generators)."""
        pass
