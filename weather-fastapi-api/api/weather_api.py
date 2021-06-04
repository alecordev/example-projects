import fastapi

from models.location import Location
from models.umbrella_status import UmbrellaStatus
from services import live_weather_services

router = fastapi.APIRouter(prefix="/api")


@router.get("/umbrella", response_model=UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    data = await live_weather_services.get_live_weather_report(location)

    weather = data.get("weather", {})
    category = weather.get("category", "Unknown")
    forecast = data.get("forecast", {})
    temp = forecast.get("temp", 0.0)

    bring = category.lower().strip() == "rain"
    return UmbrellaStatus(bring_umbrella=bring, temp=temp, weather=category)
