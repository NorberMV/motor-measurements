from motor_temperature_analyzer.application.ports.data_reader_port import DataReaderPort


class AnalyzeMotorDataUseCase:
    def __init__(self, data_reader: DataReaderPort):
        self.data_reader = data_reader

    def get_high_temperature_sessions(self, threshold: float = 80.0) -> dict[int, int]:
        """Example: Count measurements above temperature threshold per session."""
        session_counts: dict[int, int] = {}
        for measurement in self.data_reader.read_measurements():
            if measurement.pm_temperature > threshold:
                session_counts[measurement.profile_id] = (
                        session_counts.get(measurement.profile_id, 0) + 1
                )
        return session_counts
