
class pav_bhaji:
    def __init__(self, pav, chilli, butter) -> None:
        self.pav = pav
        self.chilli = chilli
        self.butter = butter

    def __add__(self, other):
        return pav_bhaji(self.pav+other.pav, 
                         self.chilli+other.chilli, 
                         self.butter+other.butter)
    
    def __str__(self) -> str:
        pass


vib = pav_bhaji(2, 4, 1)
pranav = pav_bhaji(3, 2, 0)

vinav = vib + pranav

print(vinav.pav)
print(vinav.chilli)
print(vinav.butter)