
railApiEndpoints = {
    "pnrStatus": "/api/v3/getPNRStatus?pnrNumber={}",
    "searchStation": "/api/v1/searchStation?query={}",
    "searchTrain": "/api/v1/searchTrain?query={}",
    "trainBetweenStations": "/api/v3/trainBetweenStations?fromStationCode={}&toStationCode={}&dateOfJourney={}",
    "liveTrainStatus": "/api/v1/liveTrainStatus?trainNo={}&startDay={}",
    "trainSchedule": "/api/v1/getTrainSchedule?trainNo={}",
    "seatAvailability": "/api/v1/checkSeatAvailability?classType={}&fromStationCode={}&quota={}&toStationCode={}&trainNo={}&date={}",
    "trainClasses": "/api/v1/getTrainClasses?trainNo={}",
    "fetchFair": "/api/v2/getFare?trainNo={}&fromStationCode={}&toStationCode={}",
    "trainByStations": "/api/v3/getTrainsByStation?stationCode={}",
    "liveStations": "/api/v3/getLiveStation?fromStationCode={}&toStationCode={}&hours={}",
}

# TODO : remove sample response after test

sampleResponse = {
  "status": True,
  "message": "Success",
  "timestamp": 1710709623553,
  "data": {
    "user_id": 0,
    "train_start_date": "2024-03-18",
    "train_number": "12398",
    "train_name": "Mahabodhi SF Express",
    "title": "Train starts at 12:50",
    "success": True,
    "std": "2024-03-18 12:50",
    "spent_time": 0.015,
    "source": "NDLS",
    "seo_train_name": "Mahabodhi Express",
    "run_days": "MON,TUE,WED,THU,FRI,SAT,SUN",
    "notification_date": "2024-03-18",
    "new_message": "Train hasn't started yet. But all looks good.",
    "journey_time": 845,
    "is_run_day": True,
    "ir_train_name": "Mahabodhi SF Express",
    "destination": "GAYA",
    "awaiting_update": False,
    "at_src_dstn": True,
    "at_src": True,
    "at_dstn": False
  }
}