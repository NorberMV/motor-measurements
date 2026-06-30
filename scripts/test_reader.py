from pathlib import Path
from motor_temperature_analyzer.infrastructure.adapters.csv_motor_data_reader import CSVMotorDataReader


data_path = Path("data/measures.csv")
# reader = CSVMotorDataReader(data_path)
#
# count = sum(1 for _ in reader.read_measurements())
# print(f"Total measurements processed: {count}")

# Show first few profile_ids
reader = CSVMotorDataReader(data_path)
profile_ids = set()

for m in reader.read_measurements():
    profile_ids.add(m.profile_id)
    if len(profile_ids) >= 5:
        break

print(f"Sample profile_ids found: {sorted(profile_ids)}")
