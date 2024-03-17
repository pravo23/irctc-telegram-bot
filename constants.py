
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