YEARS_ON_PLANET: dict[str, float] = {
    "Mercury": 0.2408467,
    "Venus": 0.61519726,
    "Earth": 1.0,
    "Mars": 1.8808158,
    "Jupiter": 11.862615,
    "Saturn": 29.447498,
    "Uranus": 84.016846,
    "Neptune": 164.79132,
}

SECS_PER_YEAR: int = 31557600

class SpaceAge:
    earth_years: float

    def __init__(self, seconds: int):
        self.earth_years = seconds / SECS_PER_YEAR

    def get_years(self, planet: str) -> float:
        return round(self.earth_years / YEARS_ON_PLANET[planet], 2)

    def on_mercury(self) -> float:
        return self.get_years("Mercury")
    
    def on_venus(self) -> float:
        return self.get_years("Venus")
    
    def on_earth(self) -> float:
        return self.get_years("Earth")
    
    def on_mars(self) -> float:
        return self.get_years("Mars")
    
    def on_jupiter(self) -> float:
        return self.get_years("Jupiter")
    
    def on_saturn(self) -> float:
        return self.get_years("Saturn")
    
    def on_uranus(self) -> float:
        return self.get_years("Uranus")
    
    def on_neptune(self) -> float:
        return self.get_years("Neptune")
