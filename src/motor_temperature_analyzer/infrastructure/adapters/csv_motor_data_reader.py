"""
Adapters -- the actual implementation.
This is where we connect to the real world(CSV files, databases, APIs, etc.
"""
import csv
from pathlib import Path
from typing import Iterator

from motor_temperature_analyzer.application.ports.data_reader_port import DataReaderPort
from motor_temperature_analyzer.domain.entities.motor_measurements import MotorMeasurement


class CSVMotorDataReader(DataReaderPort):
    """Reads motor temperature data from CSV using generators (memory efficient)."""

    def __init__(self, file_path: Path):
        if not file_path.exists():
            raise FileNotFoundError(f"Data file not found: {file_path}")
        self.file_path = file_path

    def read_measurements(self) -> Iterator[MotorMeasurement]:
        with open(self.file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                yield MotorMeasurement(
                    profile_id=int(row["profile_id"]),
                    motor_speed=float(row["motor_speed"]),
                    torque=float(row["torque"]),
                    pm=float(row["pm"]),
                    stator_winding=float(row["stator_winding"]),
                    coolant=float(row.get("coolant", 0)),
                    ambient=float(row.get("ambient", 0)),
                )