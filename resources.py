import requests
from keys import API_key, solar_API
from datetime import datetime, timedelta

def getCityInfo(city_name):
    apiCall1 = "http://api.openweathermap.org/geo/1.0/direct?q={cityName}&limit={limit}&appid={API_ID}"
    getLatitudeandLongitude = apiCall1.format(cityName=city_name, limit=1, API_ID=API_key)
    latitudeAndLongitude = requests.get(getLatitudeandLongitude).json()
    latitude = latitudeAndLongitude[0]['lat']
    longitude = latitudeAndLongitude[0]['lon']
    current_date = datetime.now().date()
    start_date = current_date - timedelta(days=30)
    
    solcast = "https://api.solcast.com.au/data/historic/radiation_and_weather?latitude={lat}&longitude={lon}&start={StartDate}&duration=P30D&format=json"
    getIrradiance = solcast.format(lat=latitude,lon=longitude,StartDate=start_date)
    headers = {"Authorization": f"Bearer {solar_API}" }
    GHI = requests.get(getIrradiance,headers=headers).json()["estimated_actuals"]
    ghi_by_date = {}
    for entry in GHI:
        date_str = entry["period_end"].split("T")[0]
        date = datetime.strptime(date_str, "%Y-%m-%d").date()

        # Add the GHI value to the corresponding date in the dictionary
        if date in ghi_by_date:
            ghi_by_date[date] += entry["ghi"]
        else:
            ghi_by_date[date] = entry["ghi"]
    
    return ghi_by_date
