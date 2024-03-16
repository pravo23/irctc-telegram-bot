import os
import requests

def fetch_pnr_status(pnr: str):

    HOST = os.environ.get("HOST")
    API_KEY = os.environ.get("API_KEY")
    url = f"https://{HOST}/api/v3/getPNRStatus?pnrNumber={pnr}"
    headers = {
        "X-Rapidapi-Key": API_KEY,
        "X-Rapidapi-Host": HOST,
    }

    response = requests.get(url, headers=headers)
    return response.json()

def pnr_status_message(pnr: str):

    resp = fetch_pnr_status(pnr)

    if resp.get('status') and resp.get('message') == 'Success':
        data = resp['data']['PassengerStatus'][-1]
        return f"Your Booking is *{data['ConfirmTktStatus']}* and Current Status is *{data['CurrentStatus']}*"
    
    return "Unable to fetch the pnr : *{pnr}*"
