from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Depends, Query

from motor_temperature_analyzer.infrastructure.adapters.csv_motor_data_reader import CSVMotorDataReader
from motor_temperature_analyzer.presentation.schemas.motor_responses import MotorMeasurementResponse
from motor_temperature_analyzer.application.use_cases.list_profiles import ListProfilesUseCase

from motor_temperature_analyzer.utils import get_csv_path


csv_path = get_csv_path()

app = FastAPI()

app.version = "1.0v"


def get_list_profiles_use_case() -> ListProfilesUseCase:
    csv_path = get_csv_path()
    data_reader = CSVMotorDataReader(csv_path)
    return ListProfilesUseCase(data_reader)


@app.get("/measurements", tags=["Measurements"], 
         response_model=list[MotorMeasurementResponse]
)
async def get_measurements(
    profile_id: Optional[int] = Query(None, description="Filter by profile ID"),
    limit: int = Query(100, ge=1, le=100, description="Max number of records to return"),
    offset: int = Query(0, ge=0),
    use_case: ListProfilesUseCase = Depends(get_list_profiles_use_case),
) -> list[MotorMeasurementResponse]:
    measurements = use_case.execute(
        profile_id=profile_id,
        limit=limit,
        offset=offset
    )

    return [
        MotorMeasurementResponse(
            profile_id=row.profile_id,
            motor_speed=row.motor_speed,
            stator_winding=row.stator_winding,
        )
        for row in measurements
    ]