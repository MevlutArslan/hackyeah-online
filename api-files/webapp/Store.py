
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
        self._que = []
        
    def addToQue(self,_personId):
        self._que.append(personId)
    
    def removeFromQue(self,_personId):
        self._que.pop(0)

    def __str__(self):
        return ""

        

