
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
  "timestamp": 1662275995178,
  "data": {
    "general": [
      {
        "classType": "3A",
        "fare": 505,
        "breakup": [
          {
            "title": "Base Charges",
            "key": "baseFare",
            "cost": 441
          },
          {
            "title": "Reservation Charges",
            "key": "reservationCharges",
            "cost": 40
          },
          {
            "title": "GST",
            "key": "serviceTax",
            "cost": 24
          },
          {
            "title": "Total Amount",
            "key": "total",
            "cost": 505
          }
        ]
      },
      {
        "classType": "SL",
        "fare": 175,
        "breakup": [
          {
            "title": "Base Charges",
            "key": "baseFare",
            "cost": 155
          },
          {
            "title": "Reservation Charges",
            "key": "reservationCharges",
            "cost": 20
          },
          {
            "title": "Total Amount",
            "key": "total",
            "cost": 175
          }
        ]
      },
      {
        "classType": "2A",
        "fare": 710,
        "breakup": [
          {
            "title": "Base Charges",
            "key": "baseFare",
            "cost": 626
          },
          {
            "title": "Reservation Charges",
            "key": "reservationCharges",
            "cost": 50
          },
          {
            "title": "GST",
            "key": "serviceTax",
            "cost": 34
          },
          {
            "title": "Total Amount",
            "key": "total",
            "cost": 710
          }
        ]
      },
      {
        "classType": "2S",
        "fare": 105,
        "breakup": [
          {
            "title": "Base Charges",
            "key": "baseFare",
            "cost": 90
          },
          {
            "title": "Reservation Charges",
            "key": "reservationCharges",
            "cost": 15
          },
          {
            "title": "Total Amount",
            "key": "total",
            "cost": 105
          }
        ]
      }
    ],
    "tatkal": [
      {
        "classType": "3A",
        "fare": 1105,
        "breakup": [
          {
            "title": "Base Charges",
            "key": "baseFare",
            "cost": 712
          },
          {
            "title": "Reservation Charges",
            "key": "reservationCharges",
            "cost": 40
          },
          {
            "title": "GST",
            "key": "serviceTax",
            "cost": 53
          },
          {
            "title": "Tatkal Charges",
            "key": "tatkalCharges",
            "cost": 300
          },
          {
            "title": "Total Amount",
            "key": "total",
            "cost": 1105
          }
        ]
      },
      {
        "classType": "SL",
        "fare": 395,
        "breakup": [
          {
            "title": "Base Charges",
            "key": "baseFare",
            "cost": 275
          },
          {
            "title": "Reservation Charges",
            "key": "reservationCharges",
            "cost": 20
          },
          {
            "title": "Tatkal Charges",
            "key": "tatkalCharges",
            "cost": 100
          },
          {
            "title": "Total Amount",
            "key": "total",
            "cost": 395
          }
        ]
      },
      {
        "classType": "2A",
        "fare": 1540,
        "breakup": [
          {
            "title": "Base Charges",
            "key": "baseFare",
            "cost": 1016
          },
          {
            "title": "Reservation Charges",
            "key": "reservationCharges",
            "cost": 50
          },
          {
            "title": "GST",
            "key": "serviceTax",
            "cost": 74
          },
          {
            "title": "Tatkal Charges",
            "key": "tatkalCharges",
            "cost": 400
          },
          {
            "title": "Total Amount",
            "key": "total",
            "cost": 1540
          }
        ]
      },
      {
        "classType": "2S",
        "fare": 190,
        "breakup": [
          {
            "title": "Base Charges",
            "key": "baseFare",
            "cost": 160
          },
          {
            "title": "Reservation Charges",
            "key": "reservationCharges",
            "cost": 15
          },
          {
            "title": "Tatkal Charges",
            "key": "tatkalCharges",
            "cost": 15
          },
          {
            "title": "Total Amount",
            "key": "total",
            "cost": 190
          }
        ]
      }
    ]
  }
}