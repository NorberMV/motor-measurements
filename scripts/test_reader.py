from motor_temperature_analyzer.infrastructure.adapters.csv_motor_data_reader import CSVMotorDataReader
from motor_temperature_analyzer.utils import get_csv_path


data_path = get_csv_path()
reader = CSVMotorDataReader(data_path)
profile_ids = set()

for m in reader.read_measurements():
    profile_ids.add(m.profile_id)
    if len(profile_ids) >= 5:
        break

print(f"Sample profile_ids found: {sorted(profile_ids)}")
