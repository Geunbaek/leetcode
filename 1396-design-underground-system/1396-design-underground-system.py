from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.user = dict()
        self.result = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.user[id]
        self.result[f"{start[0]}-{stationName}"].append(t - start[1])
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        results = self.result[f"{startStation}-{endStation}"]
        return sum(results) / len(results)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)