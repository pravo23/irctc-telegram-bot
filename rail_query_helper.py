import os
import requests
from constants import railApiEndpoints

def get_rail_query_info(url: str) -> dict:
    """
    Sends an HTTP GET request to the specified URL and returns the JSON response.

    Args:
        url (str): The URL to which the GET request is sent.

    Returns:
        dict: A dictionary containing the JSON response from the API.
    """
    HOST = os.environ.get("HOST")
    API_KEY = os.environ.get("API_KEY")
    url = url.format(HOST)
    headers = {
        "X-Rapidapi-Key": API_KEY,
        "X-Rapidapi-Host": HOST,
    }

    response = requests.get(url, headers=headers)
    return response.json()

def fetch_pnr_status(pnr: str) -> dict:
    """
    Fetches the PNR (Passenger Name Record) status from the railway API for the given PNR number.

    Args:
        pnr (str): The PNR number for which the status is requested.

    Returns:
        dict: A dictionary containing the response from the API, including PNR status information.
    """
    fetch_pnr_status_endpoint = railApiEndpoints['pnrStatus'].format(pnr)
    url = f"https://{{}}{fetch_pnr_status_endpoint}"
    return get_rail_query_info(url)

def search_station(station_code: str) -> dict:
    """
    Searches for a railway station by its station code using the railway API.

    Args:
        station_code (str): The station code to search for.

    Returns:
        dict: A dictionary containing the response from the API, including station information.
    """
    search_station_endpoint = railApiEndpoints['searchStation'].format(
        station_code)
    url = f"https://{{}}{search_station_endpoint}"
    return get_rail_query_info(url)

def search_train(train_code: str) -> dict:
    """
    Searches for a train by its train code using the railway API.

    Args:
        train_code (str): The train code to search for.

    Returns:
        dict: A dictionary containing the response from the API, including train information.
    """
    search_train_endpoint = railApiEndpoints['searchTrain'].format(train_code)
    url = f"https://{{}}{search_train_endpoint}"
    return get_rail_query_info(url)

def train_between_stations(
        from_station_code: str,
        to_station_code: str,
        date: str) -> dict:
    """
    Fetches the list of trains running between two stations on a specified date using the railway API.

    Args:
        from_station_code (str): The station code of the starting station.
        to_station_code (str): The station code of the destination station.
        date (str): The date of travel in YYYYMMDD format.

    Returns:
        dict: A dictionary containing the response from the API, including train schedule information.
    """
    train_between_stations_endpoint = railApiEndpoints['trainBetweenStations'].format(
        from_station_code, to_station_code, date)
    url = f"https://{{}}{train_between_stations_endpoint}"
    return get_rail_query_info(url)

def live_train_status(train_code: str, start_day: int) -> dict:
    """
    Fetches the live status of a train using the railway API.

    Args:
        train_code (str): The train code for which the live status is requested.
        start_day (int): The start day from today (0 for today, 1 for tomorrow, and so on).

    Returns:
        dict: A dictionary containing the response from the API, including live train status information.
    """
    live_train_status_endpoint = railApiEndpoints['liveTrainStatus'].format(
        train_code, start_day)
    url = f"https://{{}}{live_train_status_endpoint}"
    return get_rail_query_info(url)

def train_schedule(train_code: str) -> dict:
    """
    Fetches the schedule of a train using the railway API.

    Args:
        train_code (str): The train code for which the schedule is requested.

    Returns:
        dict: A dictionary containing the response from the API, including train schedule information.
    """
    train_schedule_endpoint = railApiEndpoints['trainSchedule'].format(
        train_code)
    url = f"https://{{}}{train_schedule_endpoint}"
    return get_rail_query_info(url)

def fetch_fair(
        train_code: str,
        from_station_code: str,
        to_station_code: str) -> dict:
    """
    Fetches the fare details for a train between two stations using the railway API.

    Args:
        train_code (str): The train code.
        from_station_code (str): The station code of the starting station.
        to_station_code (str): The station code of the destination station.

    Returns:
        dict: A dictionary containing the response from the API, including fare details.
    """
    fetch_fair_endpoint = railApiEndpoints['fetchFair'].format(
        train_code, from_station_code, to_station_code)
    url = f"https://{{}}{fetch_fair_endpoint}"
    return get_rail_query_info(url)

# !Deprecated - unused handlers
# def seat_availability(params):
#     class_type, from_station_code, quota, to_station_code, train_code, date = (
#         params.get(key) for key in [
#             'class_type', 'from_station_code', 'quota', 'to_station_code', 'train_code', 'date'])

#     seat_availability_endpoint = railApiEndpoints['seatAvailability'].format(
#         class_type, from_station_code, quota, to_station_code, train_code, date
#     )
#     url = f"https://{{}}{seat_availability_endpoint}"
#     return get_rail_query_info(url)


# def train_classes(train_code):
#     train_classes_endpoint = railApiEndpoints['trainClasses'].format(
#         train_code)
#     url = f"https://{{}}{train_classes_endpoint}"
#     return get_rail_query_info(url)

# def train_by_station(station_code):
#     train_by_station_endpoint = railApiEndpoints['trainByStations'].format(
#         station_code)
#     url = f"https://{{}}{train_by_station_endpoint}"
#     return get_rail_query_info(url)


# def live_stations(from_station_code, to_station_code, hours):
#     live_stations_endpoint = railApiEndpoints['liveStations'].format(
#         from_station_code, to_station_code, hours)
#     url = f"https://{{}}{live_stations_endpoint}"
#     return get_rail_query_info(url)

# methods for the formatted response

def pnr_status_message(pnr: str):

    resp = fetch_pnr_status(pnr)
    if resp.get('status') and resp.get('message') == 'Success':
        data = resp['data']['PassengerStatus'][-1]
        return f"Your Booking is *{data['ConfirmTktStatus']}* and Current Status is *{data['CurrentStatus']}*"

    return "Unable to fetch the pnr : *{pnr}*"


def search_station_response(station_code: str):
    resp = search_station(station_code)
    if resp.get('status') and resp.get('message') == 'Success':
        for station in resp.get('data'):
            if station.get('code') == station_code.upper():
                return f"{station_code} : *{station.get('name')}*"
        return f"No station available with station code: *{station_code}*"

    return f"Could not fetch the data. Try again!"


def search_train_response(train_code: str):
    resp = search_train(train_code)
    if resp.get('status') and resp.get('message') == 'Success':
        for train in resp.get('data'):
            if train.get('train_number') == train_code:
                return f"{train_code} : *{train.get('train_name')}*"

        return f"No train available for the given train number - {train_code}"

    return f"Could not fetch the data. Try again!"


def fetch_fair_response(
        train_code: str,
        from_station_code: str,
        to_station_code: str):
    resp = fetch_fair(train_code, from_station_code, to_station_code)
    # resp = samprleResponse
    total_fare = {'general' - {}, 'tatkal' - {}}

    if resp.get('status') and resp.get('message') == 'Success':
        # Process general data
        for entry in resp['data']['general']:
            class_type = entry['classType']
            fare = entry['fare']
            total_fare['general'].setdefault(class_type, 0)
            total_fare['general'][class_type] += fare

        # Process tatkal data
        for entry in resp['data']['tatkal']:
            class_type = entry['classType']
            fare = entry['fare']
            total_fare['tatkal'].setdefault(class_type, 0)
            total_fare['tatkal'][class_type] += fare
    else:
        return f"Could not fetch fair, Try again!"

    # format the data
    multiline_string = ""

    multiline_string += "Total Fare for General Class:\n"
    for class_type, fare in total_fare['general'].items():
        multiline_string += f"{class_type}- {fare}\n"

    multiline_string += "\nTotal Fare for Tatkal Class:\n"
    for class_type, fare in total_fare['tatkal'].items():
        multiline_string += f"{class_type}- {fare}\n"

    return multiline_string


def live_train_status_response(train_code, start_day=0):
    resp = live_train_status(train_code, start_day)

    if resp.get('status') and resp.get('message') == 'Success':

        return f"Running status of {resp['data'].get('train_name')} (*{resp['data'].get('train_number')}*) - {resp['data'].get('new_message')}"

    return f"Unable to fetch the live status!"


def train_schedule_response(train_code, start_day=0):
    resp = train_schedule(train_code)

    if resp.get('status') and resp.get('message') == 'Success':

        return f"{resp['data'].get('train_name')} (*{resp['data'].get('train_number')}*) - {resp['data'].get('title')}. It starts from *{resp['data'].get('source')}* and terminate at *{resp['data'].get('destination')}*"

    return f"Unable to fetch schedule of train!"


def train_between_station_response(
        from_station_code: str,
        to_station_code: str,
        date: str):
    """
        Fields to be populate -

        train_number
        train_name
        from_station_name
        to_station_name
        from_std
        to_sta
        duration
        train_date
    """
    message = ""
    resp = train_between_stations(from_station_code, to_station_code, date)

    if resp.get('status') and resp.get('message') == 'Success':
        train_data = resp['data']
        # Constructing the message
        for train in train_data:
            train_info = [
                f"Train Number- {train['train_number']}",
                f"Train Name- {train['train_name']}",
                f"From Station- {train['from_station_name']}",
                f"To Station- {train['to_station_name']}",
                f"Departure Time- {train['from_std']}",
                f"Arrival Time- {train['to_sta']}",
                f"Duration- {train['duration']}",
                f"Date- {train['train_date']}"
            ]
        message += '\n'.join(train_info) + "\n\n"
    else:
        return f"Unable to fetch trains between stations!"

    return message if message else "There is no train available between the stations!"
