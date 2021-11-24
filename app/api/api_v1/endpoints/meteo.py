"""Route for the weather data."""

from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm.session import Session

from api import deps
from db_session.database import get_db_session
from schemas import schemas
from crud import crud


router = APIRouter()


@router.get("/meteo", response_model=List[schemas.MeteoBase])
async def get_meteo(
    station_id: int,
    db_session: Session = Depends(get_db_session),
    current_user: schemas.User = Depends(deps.get_current_user)
):
    """Give the weather data from the specified station."""
    db_session_meteo = crud.get_meteo(db_session, station_id=station_id)
    if not db_session_meteo:
        raise HTTPException(status_code=404, detail="Weather data not found")
    return db_session_meteo