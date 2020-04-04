class Store:
    def __init__(self, storename : str, numberOfCashiers : int, openingHour : str, closingHour : str, numberOfEmployees : int,
                numberOfSecurityCameras: int, latitude : float, longtitude : float):
        self._storename = storename
        self._numberOfCashiers = numberOfCashiers
        self._openingHour = openingHour
        self._closingHour = closingHour
        self._numberOfEmployees = numberOfEmployees
        self._numberOfSecurityCameras = numberOfSecurityCameras
        self._latitude = latitude
        self._longtitude = longtitude
        
    def __str__(self):
        return ""

    def toDict(self):
        return {
            'storename': self._storename,
            'numberOfCashiers' : self._numberOfCashiers,
            'openingHour' : self._openingHour,
            'closingHour' : self._closingHour,
            'numberOfEmployees' : self._numberOfEmployees,
            'numberOfSecurityCameras' : self._numberOfSecurityCameras,
            'location': self._location
        }