from pathlib import Path
import csv

from motor_temperature_analyzer.domain.entities.motor_measurements import MotorMeasurement
from motor_temperature_analyzer.utils import get_csv_path


data_path = get_csv_path()


def read_csv(path: Path, limit: int = 6):
    with open(path, encoding="utf-8") as fh:
        csvreader = csv.DictReader(fh)

        for i, row in enumerate(csvreader):
            if i <= limit:
                print(f"row {i} = {row}")


if __name__ == "__main__":
    read_csv(data_path)
"""
Example output:
row 0 = {'u_q': '-0.45068150758743286', 'coolant': '18.805171966552734', 'stator_winding': '19.086669921875', 'u_d': '-0.3500545918941498', 'stator_tooth': '18.2932186126709', 'motor_speed': '0.0028655678033828735', 'i_d': '0.004419136792421341', 'i_q': '0.0003281021781731397', 'pm': '24.554214477539062', 'stator_yoke': '18.316547393798828', 'ambient': '19.850690841674805', 'torque': '0.18710079789161682', 'profile_id': '17'}
"""
