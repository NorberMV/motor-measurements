from typing import Iterator, Optional

from motor_temperature_analyzer.application.ports.data_reader_port import DataReaderPort
from motor_temperature_analyzer.domain.entities.motor_measurements import MotorMeasurement


class ListProfilesUseCase:
    def __init__(self, data_reader: DataReaderPort):
        self.data_reader = data_reader

    def execute(
            self,
            profile_id: Optional[int] = None,
            limit: int = 100,
            offset: int = 0,
        ) -> list[MotorMeasurement]:
        """Returns measurements lazily (generator)"""
        results: MotorMeasurement = []
        skipped = 0

        for measurement in self.data_reader.read_measurements():
            if measurement.profile_id is not None and measurement.profile_id != profile_id:
                continue
            # Apply offset (skip records)
            if skipped < offset:
                skipped += 1
                continue

            # Apply limit
            if len(results) >= limit:
                break

            results.append(measurement)
        return results