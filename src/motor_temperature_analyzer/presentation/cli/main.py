from pathlib import Path
import typer

from motor_temperature_analyzer.infrastructure.adapters.csv_motor_data_reader import CSVMotorDataReader
from motor_temperature_analyzer.application.use_cases.analyze_motor_data import AnalyzeMotorDataUseCase
from motor_temperature_analyzer.utils import get_csv_path


app = typer.Typer()


@app.command()
def analyze_high_temp(file_path: Path = None, threshold: float = 80.0):
    if file_path is None:
        file_path = get_csv_path()
    reader = CSVMotorDataReader(file_path)
    use_case = AnalyzeMotorDataUseCase(reader)
    result = use_case.get_high_temperature_sessions(threshold)
    print(result)


if __name__ == "__main__":
    app()
