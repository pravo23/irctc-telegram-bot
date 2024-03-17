import os
import requests
from constants import railApiEndpoints

def get_rail_query_info(url : str):
    HOST = os.environ.get("HOST")
    API_KEY = os.environ.get("API_KEY")
    url = url.format(HOST)
    headers = {
        "X-Rapidapi-Key": API_KEY,
        "X-Rapidapi-Host": HOST,
    }

    response = requests.get(url, headers=headers)
    return response.json()

def fetch_pnr_status(pnr: str):
    fetch_pnr_status_endpoint = railApiEndpoints['pnrStatus'].format(pnr)
    url = f"https://{{}}{fetch_pnr_status_endpoint}"
    return get_rail_query_info(url)

def pnr_status_message(pnr: str):

    resp = fetch_pnr_status(pnr)
    if resp.get('status') and resp.get('message') == 'Success':
        data = resp['data']['PassengerStatus'][-1]
        return f"Your Booking is *{data['ConfirmTktStatus']}* and Current Status is *{data['CurrentStatus']}*"
    
    return "Unable to fetch the pnr : *{pnr}*"

def search_station(station_code):
    search_station_endpoint = railApiEndpoints['searchStation'].format(station_code)
    url = f"https://{{}}{search_station_endpoint}"
    return get_rail_query_info(url)

def search_train(train_code):
    search_train_endpoint = railApiEndpoints['searchTrain'].format(train_code)
    url = f"https://{{}}{search_train_endpoint}"
    return get_rail_query_info(url)

def train_between_stations(from_station_code, to_station_code, date):
    train_between_stations_endpoint = railApiEndpoints['trainBetweenStations'].format(from_station_code, to_station_code, date)
    url = f"https://{{}}{train_between_stations_endpoint}"
    return get_rail_query_info(url)

def live_train_status(train_code, start_day):
    live_train_status_endpoint = railApiEndpoints['liveTrainStatus'].format(train_code, start_day)
    url = f"https://{{}}{live_train_status_endpoint}"
    return get_rail_query_info(url)

def train_schedule(train_code):
    train_schedule_endpoint = railApiEndpoints['trainSchedule'].format(train_code)
    url = f"https://{{}}{train_schedule_endpoint}"
    return get_rail_query_info(url)

def seat_availability(params):
    class_type, from_station_code, quota, to_station_code, train_code, date = (
        params.get(key) for key in ['class_type', 'from_station_code', 'quota', 'to_station_code', 'train_code', 'date'])

    seat_availability_endpoint = railApiEndpoints['seatAvailability'].format(
        class_type, from_station_code, quota, to_station_code, train_code, date
    )
    url = f"https://{{}}{seat_availability_endpoint}"
    return get_rail_query_info(url)

def train_classes(train_code):
    train_classes_endpoint = railApiEndpoints['trainClasses'].format(train_code)
    url = f"https://{{}}{train_classes_endpoint}"
    return get_rail_query_info(url)

def fetch_fair(train_code, from_station_code, to_station_code):
    fetch_fair_endpoint = railApiEndpoints['fetchFair'].format(train_code, from_station_code, to_station_code)
    url = f"https://{{}}{fetch_fair_endpoint}"
    return get_rail_query_info(url)

def train_by_station(station_code):
    train_by_station_endpoint = railApiEndpoints['trainByStations'].format(station_code)
    url = f"https://{{}}{train_by_station_endpoint}"
    return get_rail_query_info(url)

def live_stations(from_station_code, to_station_code, hours):
    live_stations_endpoint = railApiEndpoints['liveStations'].format(from_station_code, to_station_code, hours)
    url = f"https://{{}}{live_stations_endpoint}"
    return get_rail_query_info(url)